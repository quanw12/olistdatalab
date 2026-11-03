---
tags: [decourse, sql, databases]
module: 03
---

# Transactions, Indexes and EXPLAIN

> [!info] Learning goals
> After this note you can: explain ACID and what a transaction does and does not protect; use `BEGIN/COMMIT/ROLLBACK`; describe isolation levels and the anomalies they prevent; observe locking and deadlocks; explain how a B-tree index works and when it helps or hurts; and read a query plan with `EXPLAIN (ANALYZE)` to find the real bottleneck.

## 1. Transactions and ACID

A **transaction** groups several statements into one unit: either all of them take effect, or none do.

| Letter | Property | Meaning |
|---|---|---|
| A | Atomicity | All or nothing — no half-applied transfer |
| C | Consistency | Constraints (keys, checks) hold before and after |
| I | Isolation | Concurrent transactions do not see each other's half-done work (to a configurable degree) |
| D | Durability | Once committed, the change survives a crash |

```sql
-- runnable
-- expect: [[1, 100], [2, 0]]
CREATE TABLE account(id INTEGER PRIMARY KEY, balance INTEGER);
INSERT INTO account VALUES (1,100), (2,0);
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 10 WHERE id = 1;
UPDATE account SET balance = balance + 10 WHERE id = 2;
ROLLBACK;
SELECT * FROM account ORDER BY id;
-- Expected: (1,100), (2,0): no half-applied transaction.
```

Replace `ROLLBACK` with `COMMIT` and both updates persist together.

```sql
-- runnable
-- expect: [[1, 90], [2, 10]]
CREATE TABLE account(id INTEGER PRIMARY KEY, balance INTEGER);
INSERT INTO account VALUES (1,100), (2,0);
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 10 WHERE id = 1;
UPDATE account SET balance = balance + 10 WHERE id = 2;
COMMIT;
SELECT * FROM account ORDER BY id;
```

What a transaction does **not** do:

- It does not span systems. A database commit and a Parquet file write are two separate operations; a crash in between leaves them inconsistent. Design retries that repair either side ([[Ingestion Contracts and Idempotency]]).
- It does not roll back by itself in your code: when a statement fails, the client must issue `ROLLBACK` (Python drivers do this when you use the connection as a context manager or call `rollback()` in `except`).
- Long transactions hold locks and old row versions, slowing other readers and writers.

### Publishing a table atomically

Readers should never see an empty or half-loaded table. Common pattern: load into a staging table, then swap inside one transaction:

```sql
BEGIN;
DELETE FROM mart.daily_revenue WHERE day >= DATE '2018-01-01' AND day < DATE '2018-01-08';
INSERT INTO mart.daily_revenue SELECT * FROM staging.daily_revenue_batch;
COMMIT;
```

Each table is atomic on its own, but two marts published in two transactions can be seen by a reader at different versions. If consumers need a consistent set, publish all of them in one transaction or expose a version pointer.

## 2. Isolation and concurrency

Isolation levels trade correctness against concurrency (PostgreSQL names):

| Level | Prevents | Still possible |
|---|---|---|
| Read Committed (PostgreSQL default) | Dirty reads (seeing uncommitted data) | Non-repeatable reads, phantoms, lost updates in read-modify-write code |
| Repeatable Read | + non-repeatable reads (snapshot for the whole transaction) | Some write-skew anomalies; may raise serialization errors you must retry |
| Serializable | Behaves as if transactions ran one at a time | Serialization failures — the app must retry |

**Lost update** example: two sessions read balance 100, each adds 10 in Python and writes 110 — one update is lost. Fixes: do it in one statement (`SET balance = balance + 10`), lock the row (`SELECT … FOR UPDATE`), or use a version column (optimistic locking).

### Locks and deadlocks

Writers lock the rows they change until commit. A second writer to the same row **waits**. A **deadlock** happens when A holds row 1 and waits for row 2 while B holds row 2 and waits for row 1; PostgreSQL detects it and aborts one transaction. Prevent it by always locking rows in the same order and keeping transactions short.

## 3. Upserts in PostgreSQL

```sql
-- PostgreSQL; create the table in a lab schema before practising.
CREATE TABLE lab_orders(order_id text PRIMARY KEY, version bigint, amount numeric(12,2));
INSERT INTO lab_orders VALUES ('o1',2,120)
ON CONFLICT (order_id) DO UPDATE
SET version = EXCLUDED.version, amount = EXCLUDED.amount
WHERE EXCLUDED.version > lab_orders.version;
```

Send version 1 after version 2: the amount must stay 120. Equal versions with different content need a conflict rule; `ON CONFLICT` is not a solution for every concurrency problem. The same pattern runs in DuckDB (see [[CTE Dedup and Incremental SQL]]).

## 4. Indexes

Without an index, finding `order_id = 'o1'` means reading every row (**sequential scan**, O(n)). A **B-tree index** keeps the key values sorted in a balanced tree with pointers to rows, so a lookup takes O(log n) steps — a few page reads even for millions of rows.

```sql
CREATE INDEX idx_orders_customer ON orders (customer_id);
CREATE INDEX idx_items_order_seller ON order_items (order_id, seller_id);   -- composite
```

When an index helps (row stores like PostgreSQL):

- Selective filters returning a small fraction of rows (`WHERE order_id = …`).
- Join keys on the inner side of nested-loop joins.
- `ORDER BY … LIMIT` on the indexed column.
- A composite index `(a, b)` helps filters on `a` or on `a` and `b` — not on `b` alone (leftmost-prefix rule).

When it does not:

- Small tables, or filters that match a large share of rows — a sequential scan is cheaper; the planner is right to ignore the index.
- Functions on the column (`WHERE lower(email) = …`) unless you create an expression index.
- Every index costs storage and slows every INSERT/UPDATE/DELETE.

Columnar analytical engines (DuckDB, BigQuery, Snowflake) mostly do **not** rely on B-tree indexes. They use column pruning, min/max statistics per row group/block, partitioning and clustering instead ([[Performance and Storage]]). Do not carry PostgreSQL index advice over to them.

## 5. Reading query plans

`EXPLAIN` shows the plan the optimiser chose; `EXPLAIN ANALYZE` **runs** the query and adds actual times and row counts.

```sql
-- PostgreSQL pattern; ANALYZE executes the query, so use a SELECT on lab data.
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, amount FROM lab_orders WHERE order_id = 'o1';
```

What to look at:

1. **Scan types:** Seq Scan, Index Scan, Index Only Scan, Bitmap Heap Scan.
2. **Join types:** Nested Loop (small inner side or indexed), Hash Join (equality joins on larger inputs), Merge Join (sorted inputs).
3. **Estimated vs actual rows:** a big mismatch means bad statistics (`ANALYZE table`) or a misleading predicate, and usually a bad plan.
4. **Sorts and hashes spilling to disk**, and **buffers** (pages read from cache vs disk).
5. Where the time goes: plans are trees; the node with the largest actual time is the bottleneck.

DuckDB has `EXPLAIN` and `EXPLAIN ANALYZE` too, showing operators like `SEQ_SCAN`, `HASH_JOIN`, `HASH_GROUP_BY`, with row counts per operator. BigQuery shows an execution graph with bytes processed per stage.

Benchmark honestly: same data, same query, warm vs cold cache stated, several runs, and the plan before/after.

## 6. Two-session lab (PostgreSQL)

1. Session A: `BEGIN; UPDATE lab_orders SET amount = amount + 1 WHERE order_id = 'o1';` (do not commit).
2. Session B: `UPDATE lab_orders SET amount = amount + 1 WHERE order_id = 'o1';` — observe that it waits.
3. In a third session, find the blocker:
   ```sql
   SELECT pid, state, wait_event_type, query, pg_blocking_pids(pid) AS blocked_by
   FROM pg_stat_activity WHERE datname = current_database();
   ```
4. Commit A and watch B continue. Then provoke a deadlock with two keys locked in opposite order and read the error message.

Never kill processes on a shared server casually; in your lab, `SELECT pg_cancel_backend(pid)` cancels a query and `pg_terminate_backend(pid)` ends the session.

## 7. Applying it to Olist

The loader publishes each table in a transaction; Postgres serves the marts to the dashboard through a read-only role ([[Docker PostgreSQL and Serving]]). In module 10 you run `EXPLAIN ANALYZE` before and after adding an index for a dashboard filter and record both plans.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Assuming DB + file writes are atomic together | Inconsistent outputs after a crash | Repairable, idempotent retries |
| Read-modify-write in application code | Lost updates | Single UPDATE, row locks or version checks |
| `DROP` + `CREATE` to republish | Lost grants and indexes; readers see a missing table | Swap in a transaction, re-apply grants, test |
| Indexing everything | Slow writes, wasted space | Index for measured query patterns |
| Trusting `EXPLAIN` estimates | Wrong diagnosis | `EXPLAIN ANALYZE`, compare estimated vs actual |
| PostgreSQL index advice in BigQuery | No effect | Partitioning/clustering instead |

## 9. Exercises

1. Run the rollback example, then make the second update violate a `CHECK (balance >= 0)` constraint inside a transaction. What happens to the first update?
2. In PostgreSQL, load 1 million rows, run `EXPLAIN ANALYZE` for a lookup by a non-indexed column, add an index, run it again. Record both plans and times.
3. Reproduce a lost update with two Python connections, then fix it three different ways.
4. Explain why the planner ignores your index on a 200-row table.

## 10. Review questions

> [!question]- How is atomicity different from isolation?
> Atomicity: a transaction's changes happen all together or not at all. Isolation: what concurrent transactions can see of each other's work while they run.

> [!question]- Can a reader see two marts from two different publishes?
> Yes, if they were published in separate transactions. Publish them together or use a version pointer if consistency across tables matters.

> [!question]- Why can DROP/CREATE break consumers even if the data is correct?
> It removes grants and indexes, and readers may hit a moment where the table does not exist.

> [!question]- What does a large gap between estimated and actual rows suggest?
> Stale or missing statistics or a predicate the planner cannot estimate, which often leads to a poor join or scan choice.

Related: [[Docker PostgreSQL and Serving]], [[Delivery and Reproducibility]], [[Performance and Storage]], [[Module 03 - SQL]]. Sources: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html), [Use The Index, Luke](https://use-the-index-luke.com/).
