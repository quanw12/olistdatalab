---
tags: [decourse, sql, modeling]
module: 03
---

# JOIN, Grain and Fan-out

> [!info] Learning goals
> After this note you can: state the grain of any table; predict how many rows a join returns; choose between INNER, LEFT, FULL, semi- and anti-joins; explain and prevent fan-out by aggregating to the target grain first; put filters in `ON` vs `WHERE` correctly; and write tests that prove a join did not duplicate or lose rows.

> [!info] Before every JOIN
> Write one sentence: "one row in this table means …", and name the key that is unique on each side. A join can be syntactically fine and still multiply money.

## 1. Grain: what one row means

The **grain** of a table is the level of detail of one row.

| Olist table | Grain (one row = …) | Unique key |
|---|---|---|
| `orders` | one order | `order_id` |
| `order_items` | one item line within an order | `(order_id, order_item_id)` |
| `order_payments` | one payment instalment/method of an order | `(order_id, payment_sequential)` |
| `order_reviews` | one review (an order can have several) | `review_id` (not unique in the raw data!) |
| `geolocation` | one coordinate sample for a zip prefix | none — many rows per zip |

Grain is the single most important thing to know before joining or aggregating. Metrics are only correct when computed at the right grain.

## 2. How many rows does a join return?

For each pair of rows where the `ON` condition is true, the join emits one row. So for a given key with *m* rows on the left and *n* on the right, an inner join emits **m × n** rows.

| Relationship | Rows per key | Safe for summing left-side values? |
|---|---|---|
| 1 : 1 | 1 | yes |
| 1 : n (parent to children) | n | parent values repeat n times |
| n : m | n × m | both sides repeat — almost always a bug |

### Join types

```sql
-- runnable
-- expect: [[3, 4, 4, 5, 2, 1]]
WITH a(id) AS (VALUES (1), (2), (3)),
     b(id) AS (VALUES (2), (3), (3), (4))
SELECT
  (SELECT count(*) FROM a INNER JOIN b USING (id))            AS inner_rows,  -- 2 once, 3 twice
  (SELECT count(*) FROM a LEFT JOIN b USING (id))             AS left_rows,   -- + unmatched 1
  (SELECT count(*) FROM a RIGHT JOIN b USING (id))            AS right_rows,  -- + unmatched 4
  (SELECT count(*) FROM a FULL OUTER JOIN b USING (id))       AS full_rows,   -- + both unmatched
  (SELECT count(*) FROM a WHERE EXISTS (SELECT 1 FROM b WHERE b.id = a.id))     AS semi_rows,
  (SELECT count(*) FROM a WHERE NOT EXISTS (SELECT 1 FROM b WHERE b.id = a.id)) AS anti_rows;
```

| Join | Keeps | Typical use |
|---|---|---|
| `INNER JOIN` | only matching pairs | enrich when a match is mandatory |
| `LEFT JOIN` | every left row, NULLs if no match | keep all orders even without payments |
| `FULL OUTER JOIN` | everything from both sides | reconciliation: find rows missing on either side |
| **Semi-join** `WHERE EXISTS` | left rows that have a match, **once each** | "orders that have at least one review" without duplication |
| **Anti-join** `WHERE NOT EXISTS` | left rows without a match | orphans, missing data, deletes |
| `CROSS JOIN` | every combination | date spine × seller grid |

Note the semi-join: `EXISTS` never multiplies rows, unlike `INNER JOIN` with a 1:n table.

## 3. Fan-out: the bug that multiplies money

```sql
-- runnable
-- expect: [[4, 200]]
WITH orders(id) AS (VALUES ('o1')),
items(order_id, item_id) AS (VALUES ('o1', 1), ('o1', 2)),
payments(order_id, amount) AS (VALUES ('o1', 60), ('o1', 40))
SELECT count(*) AS joined_rows, sum(p.amount) AS wrong_total
FROM orders o
JOIN items i ON o.id = i.order_id
JOIN payments p ON o.id = p.order_id;
-- Expected: 4 rows and a wrong total of 200; the real payment total is only 100.
```

Two independent 1:n relationships from the same parent produce 2 × 2 = 4 rows for o1, and each payment appears twice. `DISTINCT` after the fact does not fix it, and `SUM(DISTINCT amount)` is also wrong whenever two legitimate payments have the same value.

### The fix: aggregate to the target grain first

```sql
-- runnable
-- expect: [["o1", 2, 100], ["o2", null, null]]
WITH orders(id) AS (VALUES ('o1'), ('o2')),
items(order_id, item_id) AS (VALUES ('o1', 1), ('o1', 2)),
payments(order_id, amount) AS (VALUES ('o1', 60), ('o1', 40)),
item_summary AS (
    SELECT order_id, count(*) AS item_count FROM items GROUP BY order_id
),
payment_summary AS (
    SELECT order_id, sum(amount) AS payment_total FROM payments GROUP BY order_id
)
SELECT o.id, i.item_count, p.payment_total
FROM orders o
LEFT JOIN item_summary i ON o.id = i.order_id
LEFT JOIN payment_summary p ON o.id = p.order_id
ORDER BY o.id;
-- Expected: ('o1',2,100), ('o2',NULL,NULL).
```

Each summary is at the **order** grain (one row per order_id), so joining them to `orders` is 1:1 and nothing repeats. This "pre-aggregate in CTEs, then join" pattern is how you build fact tables.

## 4. Filters in ON vs WHERE with LEFT JOIN

```sql
-- runnable
-- expect: [[2, 1]]
WITH orders(id) AS (VALUES ('o1'), ('o2')),
     payments(order_id, method) AS (VALUES ('o1', 'card'), ('o2', 'voucher'))
SELECT
  (SELECT count(*) FROM orders o
     LEFT JOIN payments p ON o.id = p.order_id AND p.method = 'card') AS filter_in_on,
  (SELECT count(*) FROM orders o
     LEFT JOIN payments p ON o.id = p.order_id
     WHERE p.method = 'card')                                          AS filter_in_where;
```

- A condition in `ON` decides **which right rows match**; all left rows survive (o2 gets NULLs).
- A condition in `WHERE` runs **after** the join and removes rows where `p.method` is NULL — silently turning the LEFT JOIN into an INNER JOIN.

If you want to keep every parent, put right-side conditions in `ON`, or write an explicit NULL policy like `WHERE p.method = 'card' OR p.order_id IS NULL`.

## 5. Other join hazards

- **NULL keys never match**: `NULL = NULL` is UNKNOWN, so rows with NULL keys drop out of inner joins.
- **Type mismatches**: joining `'00123'` (text) to `123` (integer) either fails or matches unexpectedly after implicit casts. Cast keys deliberately in staging.
- **Whitespace and case**: `'SP'` ≠ `'sp '`. Normalise keys once, in staging.
- **Non-unique dimension rows**: joining facts to a dimension that has two rows per key (e.g. geolocation per zip, or overlapping SCD2 versions) fans out. Make the dimension unique first: aggregate (average lat/long per zip) or pick a documented rule.
- **Range joins** (`ON fact.ts >= dim.valid_from AND fact.ts < dim.valid_to`) are correct only if the ranges do not overlap ([[Data Modeling and SCD2]]).

## 6. Proving a join is correct

Never trust a join without tests. Typical checks:

```sql
-- 1. The fact table has exactly one row per order (grain test)
SELECT order_id, count(*) FROM fct_orders GROUP BY order_id HAVING count(*) > 1;   -- expect 0 rows

-- 2. Row count preserved by a LEFT JOIN to a dimension
SELECT (SELECT count(*) FROM stg_orders) - (SELECT count(*) FROM fct_orders);       -- expect 0

-- 3. Money reconciles with the source
SELECT (SELECT sum(payment_value) FROM stg_payments) - (SELECT sum(payment_total) FROM fct_orders);  -- expect 0

-- 4. No orphans: every item belongs to a known order
SELECT count(*) FROM stg_items i WHERE NOT EXISTS (SELECT 1 FROM stg_orders o WHERE o.order_id = i.order_id);
```

In dbt these become `unique`, `not_null` and `relationships` tests plus custom reconciliation tests ([[dbt Models Tests and Incremental]]). Note that matching totals do not prove every order received the right amount — money could be shifted between orders — so combine total checks with per-key checks.

## 7. Applying it to Olist

`orders`, `order_items` and `order_payments` have different grains. To build `fct_orders` at the order grain: aggregate items per order (count, price sum, freight sum) and payments per order (payment total, number of instalments) in separate CTEs, then LEFT JOIN both to orders. Test: row count equals orders, `order_id` unique, total payments equal the source. For geolocation, which has many points per zip prefix, decide an aggregation policy (e.g., median lat/long per prefix) before joining it to customers — do not pick an arbitrary row.

## 8. Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Joining two 1:n tables to the same parent | Inflated sums | Pre-aggregate each to the parent grain |
| `SUM(DISTINCT amount)` as a fix | Undercounts equal legitimate values | Fix the grain instead |
| Right-side filter in `WHERE` after LEFT JOIN | Lost parents | Move the condition into `ON` |
| Inner join where a match is optional | Rows silently disappear | LEFT JOIN + count unmatched |
| Joining to a non-unique dimension | Duplicated facts | Make the dimension unique; test it |
| Trusting a join without row-count checks | Bugs reach dashboards | Grain, count and reconciliation tests |

## 9. Exercises

1. Add two payments of 50 to the same order; show that `SUM(DISTINCT amount)` returns 50 instead of 100.
2. Add an orphan payment (order_id not in orders) and find it with an anti-join. Then find it again with a FULL OUTER JOIN.
3. Write a query that reports, for `order_reviews`, how many `review_id` values appear more than once and on how many different orders.
4. Explain why a matching grand total does not prove every order got the right money.

> [!example]- Answer for 4
> Errors can cancel out: 10 moved from order A to order B leaves the total unchanged. You need per-key comparisons (e.g., `EXCEPT ALL` between expected and actual per order) in addition to totals.

## 10. Review questions

> [!question]- What is the grain of `order_items`, and why does it matter when you join it to payments?
> One item line per order (`order_id`, `order_item_id`). Payments are also 1:n per order, so joining both to orders without aggregating creates items × payments rows per order and duplicates money.

> [!question]- How does a semi-join differ from an inner join?
> A semi-join (`EXISTS`) returns each left row at most once, no matter how many matches exist; an inner join returns one row per matching pair.

> [!question]- Why does a WHERE condition on the right table turn a LEFT JOIN into an INNER JOIN?
> Unmatched left rows have NULLs in the right columns; the WHERE condition evaluates to UNKNOWN for them and removes them.

> [!question]- What three tests would you write for a new fact table?
> Uniqueness of the grain key, row count against the driving table, and reconciliation of key measures (e.g., money) against the source — plus orphan checks for foreign keys.

Related: [[Data Modeling and SCD2]], [[Aggregation and Window Functions]], [[Testing Logging and CI]], [[Module 03 - SQL]]. Sources: [PostgreSQL table expressions and joins](https://www.postgresql.org/docs/current/queries-table-expressions.html), [DuckDB joins](https://duckdb.org/docs/stable/sql/query_syntax/from.html).
