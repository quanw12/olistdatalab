---
tags: [decourse, sql, incremental]
module: 03
---

# CTE, Dedup and Incremental SQL

> [!info] Learning goals
> After this note you can: structure queries as a chain of named CTEs; tell exact duplicates from multiple versions of the same entity; select the latest version per key correctly, including deletes (tombstones); write watermark filters with half-open intervals and lookback; upsert idempotently; and prove that an incremental result equals a full rebuild.

## 1. CTEs: name each step

A **Common Table Expression** (`WITH name AS (…)`) gives a name to an intermediate result. A long query becomes a readable pipeline:

```sql
WITH
orders   AS (SELECT … FROM raw_orders WHERE …),          -- clean
payments AS (SELECT order_id, sum(amount) … GROUP BY 1),  -- aggregate to order grain
joined   AS (SELECT … FROM orders LEFT JOIN payments …)   -- combine
SELECT * FROM joined;
```

- Each CTE should do one thing: filter, cast, aggregate or join. Name it after what it *contains* (`paid_orders`), not what it does (`step2`).
- A CTE is a naming tool. It does **not** guarantee materialisation or speed; engines may inline it. If you need to reuse an expensive result many times, create a table.
- You can debug a CTE chain by temporarily ending with `SELECT * FROM <some middle CTE>`.
- dbt models are essentially CTE chains split into files ([[dbt Models Tests and Incremental]]).

## 2. Two kinds of "duplicates"

| Kind | Example | Correct treatment |
|---|---|---|
| **Exact duplicates** | the same file loaded twice; every column identical | Remove with `DISTINCT` or by load id; better, prevent with idempotent loads ([[Ingestion Contracts and Idempotency]]) |
| **Multiple versions** | order o1 at version 1 (amount 100), then version 2 (amount 120) | Keep the latest by a reliable version/sequence; keep history elsewhere if needed |
| **Key collision** | two different customers share one id | Not a dedup problem — a modelling or source bug; escalate |

Deduplication is a business rule: write down the key, the ordering column and the tie-breaker.

## 3. Latest version, including deletes

```sql
-- runnable
-- expect: [["o1", 120]]
WITH events(order_id, version, amount, is_deleted) AS (
    VALUES ('o1',1,100,false), ('o1',2,120,false),
           ('o2',1,50,false), ('o2',2,50,true)
), ranked AS (
    SELECT *, row_number() OVER (PARTITION BY order_id ORDER BY version DESC) AS rn
    FROM events
)
SELECT order_id, amount FROM ranked
WHERE rn = 1 AND NOT is_deleted ORDER BY order_id;
-- Expected: only ('o1',120).
```

You must pick the latest version **before** filtering deletes. Look at what goes wrong in the other order:

```sql
-- runnable
-- expect: [["o1", 120], ["o2", 50]]
WITH events(order_id, version, amount, is_deleted) AS (
    VALUES ('o1',1,100,false), ('o1',2,120,false),
           ('o2',1,50,false), ('o2',2,50,true)
), ranked AS (
    SELECT *, row_number() OVER (PARTITION BY order_id ORDER BY version DESC) AS rn
    FROM events WHERE NOT is_deleted          -- WRONG: filters the tombstone first
)
SELECT order_id, amount FROM ranked WHERE rn = 1 ORDER BY order_id;
-- o2 comes back to life from its old version.
```

A **tombstone** is a record saying "this key was deleted". Keep tombstones in the state table so that a late-arriving older event cannot resurrect the key.

Ordering column choices, from best to worst: a source sequence/version number (monotonic per key) → a change-log position (LSN) → an `updated_at` timestamp (ties and clock skew possible) → load time (only tells you when *you* saw it). If two rows tie on the ordering column with different content, that is a conflict to report, not to resolve randomly — add an event id as tie-breaker and alert.

## 4. Incremental processing

A **full rebuild** recomputes everything from the source every run: simple and correct, but slow and costly on big data. An **incremental** run processes only what changed since last time. It is faster but must handle:

1. **Which rows changed?** — a watermark, CDC log or snapshot diff.
2. **Late data** — rows arriving after their period was processed.
3. **Updates** — a changed row must replace its old version, not be added.
4. **Deletes** — rows that vanished from the source.
5. **Moved rows** — an order whose date changed affects two partitions.

### Watermarks with half-open intervals

```sql
-- runnable
-- expect: [[[1], [2, 3]]]
WITH src(id, updated_at) AS (
    VALUES (1, TIMESTAMP '2026-01-01 23:59:59'),
           (2, TIMESTAMP '2026-01-02 00:00:00'),
           (3, TIMESTAMP '2026-01-02 12:00:00')
)
SELECT
  (SELECT list(id ORDER BY id) FROM src
     WHERE updated_at >= TIMESTAMP '2026-01-01' AND updated_at < TIMESTAMP '2026-01-02') AS batch_1,
  (SELECT list(id ORDER BY id) FROM src
     WHERE updated_at >= TIMESTAMP '2026-01-02' AND updated_at < TIMESTAMP '2026-01-03') AS batch_2;
```

Half-open intervals `[lower, upper)` tile time without gaps or overlaps: the row at exactly midnight belongs to exactly one batch. With `BETWEEN` (closed on both sides), row 2 would be processed twice.

In application code, bind the bounds as parameters, never by string concatenation:

```sql
-- Pattern: :lower and :upper are bound by the caller (placeholder syntax depends on the driver).
SELECT * FROM source_orders
WHERE updated_at >= :lower AND updated_at < :upper;
```

Watermark caveats:

- **Lookback / overlap:** re-reading the last N hours or days catches late rows, but then the same row arrives twice, so the write must be an **upsert/merge by key**, never a plain append.
- **Equal timestamps** at the boundary need a tie-breaker (e.g., `(updated_at, id)` as a composite watermark).
- **Hard deletes** never appear in an `updated_at` query. You need source tombstones, CDC, or a periodic full snapshot diff.
- Filtering on a **business date** (e.g., `order_date >= current_date - 3`) misses corrections to old orders. Filter on when the row *changed*.

## 5. Idempotent writes: upsert

An operation is **idempotent** if running it twice gives the same result as running it once. Re-runs, retries and overlapping lookbacks are only safe with idempotent writes.

```sql
-- runnable
-- expect: [["o1", 2, 120], ["o2", 1, 50]]
CREATE TABLE current_orders(order_id VARCHAR PRIMARY KEY, version INTEGER, amount INTEGER);
INSERT INTO current_orders VALUES ('o1', 2, 120);
-- a late, older version arrives, then a brand-new order; then the batch is replayed
INSERT INTO current_orders VALUES ('o1', 1, 100), ('o2', 1, 50)
ON CONFLICT (order_id) DO UPDATE
SET version = EXCLUDED.version, amount = EXCLUDED.amount
WHERE EXCLUDED.version > current_orders.version;
INSERT INTO current_orders VALUES ('o1', 1, 100), ('o2', 1, 50)
ON CONFLICT (order_id) DO UPDATE
SET version = EXCLUDED.version, amount = EXCLUDED.amount
WHERE EXCLUDED.version > current_orders.version;
SELECT * FROM current_orders ORDER BY order_id;
```

The `WHERE EXCLUDED.version > …` guard stops the late version 1 from overwriting version 2, and replaying the batch changes nothing. Other idempotent patterns: `MERGE INTO` (SQL standard, supported by BigQuery, Snowflake, PostgreSQL 15+, recent DuckDB) and **partition overwrite** (delete the whole `[start, end)` partition and re-insert it inside one transaction).

## 6. Proving incremental = full rebuild

The gold standard test: build the table incrementally, build it again from scratch, and compare in **both directions**.

```sql
-- runnable
-- expect: [[0, 0]]
WITH incremental_result(order_id, day, amount) AS (VALUES ('o1', DATE '2026-01-01', 120), ('o3', DATE '2026-01-02', 10)),
     full_result(order_id, day, amount)        AS (VALUES ('o3', DATE '2026-01-02', 10), ('o1', DATE '2026-01-01', 120))
SELECT
  (SELECT count(*) FROM (SELECT * FROM incremental_result EXCEPT ALL SELECT * FROM full_result)) AS only_in_incremental,
  (SELECT count(*) FROM (SELECT * FROM full_result EXCEPT ALL SELECT * FROM incremental_result)) AS only_in_full;
```

`EXCEPT ALL` respects duplicates (plain `EXCEPT` would hide a doubled row). Comparing only totals can miss money moved between orders; compare by key and column, and decide how NULLs and decimals should compare. Remember that if an order's date changes, both the old day and the new day must be recomputed.

## 7. Applying it to Olist

The Olist CSVs are snapshots, so the reference pipeline loads full snapshots. In module 09 the dbt models add an incremental lookback, and in module 19 you build a proper change-handling lab: versions, tombstones, moved dates and replay, always verified against a full rebuild.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Filtering deletes before ranking | Deleted keys come back | Rank first, then drop tombstones |
| `row_number()` without a tie-breaker | Random winner | Version + event id |
| `BETWEEN` for batch bounds | Boundary rows processed twice | Half-open intervals |
| Append with lookback | Duplicates | Upsert/merge by key |
| Watermark on business date | Corrections to old rows missed | Watermark on change time / CDC |
| Comparing only totals | Hidden misallocation | Two-way `EXCEPT ALL` by key |

## 9. Exercises

1. Replay the event list three times, add an update to a 30-day-old order, a delete, a changed date and two events with the same timestamp. Write the expected state by hand first, then the query.
2. Rewrite the upsert as a `MERGE INTO` statement (check your engine's documentation).
3. Build a daily totals table incrementally for 3 days, then rebuild it fully, and run the two-way `EXCEPT ALL`.
4. When is a full rebuild simpler and more trustworthy than a complicated incremental model?

> [!example]- Discussion for 4
> When the data is small enough to rebuild within the time and cost budget, when the source cannot reliably tell you what changed (no tombstones, unreliable timestamps), or when correctness matters more than freshness. Many teams rebuild nightly and run incrementals only intraday.

## 10. Review questions

> [!question]- Why must ranking happen before removing tombstones?
> The tombstone is the latest version. Removing it first makes an older live version the "latest" and resurrects a deleted key.

> [!question]- Why do lookback windows require upserts?
> The overlapping window reads some rows again; appending would duplicate them, while an upsert by key replaces them.

> [!question]- How can a timestamp watermark miss data?
> Hard deletes leave no row to read; rows with equal timestamps at the boundary can be skipped; clock skew or late commits can give a row an `updated_at` older than the watermark.

> [!question]- What does `EXCEPT ALL` catch that `EXCEPT` misses?
> Different numbers of identical rows, e.g. a row duplicated in one result.

Related: [[Incremental CDC and Backfill]], [[dbt Models Tests and Incremental]], [[Aggregation and Window Functions]], [[Module 03 - SQL]]. Sources: [DuckDB WITH clause](https://duckdb.org/docs/stable/sql/query_syntax/with.html), [DuckDB INSERT … ON CONFLICT](https://duckdb.org/docs/stable/sql/statements/insert.html), [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models).
