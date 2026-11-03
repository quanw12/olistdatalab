---
tags: [decourse, sql, foundations]
module: 03
---

# SELECT, NULL and CASE

> [!info] Learning goals
> After this note you can: explain the logical order in which SQL evaluates a query; filter with `WHERE` and `HAVING` correctly; reason with three-valued logic (TRUE / FALSE / UNKNOWN); handle `NULL` with `IS NULL`, `COALESCE`, `NULLIF` and `IS DISTINCT FROM`; classify rows with `CASE`; cast types safely; and avoid the `NOT IN` + `NULL` trap.

All runnable examples use **DuckDB** (`pip install duckdb`, then `duckdb.sql("...")` in Python, or the `duckdb` CLI). Almost everything here is standard SQL and works the same in PostgreSQL.

## 1. What SQL is

SQL is **declarative**: you describe the result you want ("total payments per status for amounts above zero"), and the engine decides *how* to compute it — which index to use, in what order to join, whether to parallelise. That is why the same query runs on a laptop with DuckDB and on terabytes in BigQuery.

A table is a set of rows with the same columns. A query takes tables in and produces a new table out. Thinking "table in → table out" for every clause makes complex queries easy to read.

## 2. Writing order vs evaluation order

```sql
-- order of writing:  SELECT … FROM … JOIN … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT
-- order of running:  FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT
```

Consequences you will hit:

- `WHERE` runs **before** grouping, so it cannot use aggregates: `WHERE count(*) > 1` is an error. Filter groups with `HAVING`.
- Column aliases defined in `SELECT` do not exist yet in `WHERE` in standard SQL (DuckDB is lenient; PostgreSQL is not). Repeat the expression or use a CTE.
- `ORDER BY` runs after `SELECT`, so it *can* use aliases.
- `LIMIT` without `ORDER BY` returns arbitrary rows — never rely on it for "the first" anything.

```sql
-- runnable
-- expect: [["delivered", 2, 75.0]]
WITH payments(order_id, status, amount) AS (
    VALUES ('o1', 'delivered', 100), ('o2', 'delivered', 50),
           ('o3', 'canceled', 20), ('o4', 'delivered', 0)
)
SELECT status, count(*) AS n, avg(amount) AS avg_amount
FROM payments
WHERE amount > 0                 -- row filter, before grouping: drops o4
GROUP BY status
HAVING count(*) > 1              -- group filter, after grouping: drops 'canceled'
ORDER BY n DESC;
```

`WITH name(columns) AS (VALUES …)` builds a small inline table — the pattern used in every example so you can run them without creating tables.

## 3. NULL means "unknown", not zero

`NULL` marks a missing or unknown value. Any comparison with `NULL` is neither true nor false but **UNKNOWN**, and `WHERE` keeps only rows where the condition is **TRUE**.

```sql
-- runnable
-- expect: [[null, true, true, true, false, null]]
SELECT NULL = NULL                      AS equals_null,       -- UNKNOWN, not TRUE
       NULL IS NULL                     AS is_null,
       NULL IS NOT DISTINCT FROM NULL   AS null_safe_equal,
       TRUE OR NULL                     AS true_or_unknown,   -- TRUE regardless
       FALSE AND NULL                   AS false_and_unknown, -- FALSE regardless
       1 + NULL                         AS arithmetic;        -- NULL propagates
```

Three-valued logic truth table (U = UNKNOWN):

| a | b | a AND b | a OR b | NOT a |
|---|---|---|---|---|
| T | U | U | T | F |
| F | U | F | U | T |
| U | U | U | U | U |

### Aggregates and NULL

```sql
-- runnable
-- expect: [[3, 2, 100, 50.0]]
WITH payments(order_id, amount) AS (
    VALUES ('o1', 100), ('o2', NULL), ('o3', 0)
)
SELECT count(*) AS rows_total,
       count(amount) AS known_amounts,
       sum(amount) AS total,
       avg(amount) AS average_known
FROM payments;
-- Expected: (3, 2, 100, 50.0)
```

`COUNT(*)` counts rows; `COUNT(column)`, `SUM`, `AVG`, `MIN`, `MAX` skip NULLs. So `AVG` here is 100 / 2 = 50, not 100 / 3. `SUM` over an empty set or all-NULL values returns **NULL**, not 0. Whether the average should include the missing payment as 0 is a business decision, not a SQL detail.

## 4. CASE: classify rows

```sql
-- runnable
-- expect: [["o1", "paid"], ["o2", "missing"], ["o3", "zero"]]
WITH orders(id, amount) AS (VALUES ('o1', 10), ('o2', NULL), ('o3', 0))
SELECT id,
       CASE WHEN amount IS NULL THEN 'missing'
            WHEN amount = 0 THEN 'zero' ELSE 'paid' END AS state
FROM orders
ORDER BY id;
-- Expected: o1 paid; o2 missing; o3 zero.
```

`CASE` returns the first branch whose condition is TRUE; if none matches and there is no `ELSE`, it returns NULL. Put the `IS NULL` branch first: `amount = 0` is UNKNOWN for NULL and would fall through to `ELSE 'paid'` if it were checked first without a null branch.

`CASE` inside aggregates builds pivots ("conditional aggregation"):

```sql
-- runnable
-- expect: [[2, 1, 150]]
WITH orders(status, amount) AS (
    VALUES ('delivered', 100), ('delivered', 50), ('canceled', 20)
)
SELECT count(*) FILTER (WHERE status = 'delivered')            AS delivered_orders,
       sum(CASE WHEN status = 'canceled' THEN 1 ELSE 0 END)    AS canceled_orders,
       sum(amount) FILTER (WHERE status = 'delivered')         AS delivered_amount
FROM orders;
```

`FILTER (WHERE …)` is the standard, clearer form (PostgreSQL and DuckDB support it; BigQuery uses `COUNTIF` / `CASE`).

## 5. The NOT IN trap

```sql
-- runnable
-- expect: [[0, 1]]
WITH a(id) AS (VALUES (1), (2)),
     b(id) AS (VALUES (1), (NULL))
SELECT
  (SELECT count(*) FROM a WHERE id NOT IN (SELECT id FROM b))                         AS not_in_rows,
  (SELECT count(*) FROM a WHERE NOT EXISTS (SELECT 1 FROM b WHERE b.id = a.id))       AS not_exists_rows;
```

`2 NOT IN (1, NULL)` means `2 <> 1 AND 2 <> NULL` = `TRUE AND UNKNOWN` = UNKNOWN, so the row is dropped. One NULL in the subquery makes `NOT IN` return nothing. Use `NOT EXISTS` (or a LEFT JOIN anti-join) for "rows without a match".

## 6. Working with NULL deliberately

| Need | Syntax | Note |
|---|---|---|
| Test missing | `x IS NULL` / `x IS NOT NULL` | Never `x = NULL` |
| Blank string → NULL | `NULLIF(TRIM(x), '')` | Raw files often send `''` for missing |
| Deliberate fallback | `COALESCE(x, fallback)` | First non-NULL argument; decide if the fallback is honest |
| Safe division | `numerator / NULLIF(denominator, 0)` | Returns NULL instead of an error |
| NULL-safe comparison | `a IS DISTINCT FROM b` | TRUE when one is NULL and the other is not; essential when detecting changed rows |
| Sort NULLs explicitly | `ORDER BY x DESC NULLS LAST` | Defaults differ between engines |

```sql
-- runnable
-- expect: [["o1", false], ["o2", true], ["o3", true]]
WITH old_v(id, status) AS (VALUES ('o1', 'shipped'), ('o2', NULL), ('o3', 'shipped')),
     new_v(id, status) AS (VALUES ('o1', 'shipped'), ('o2', 'delivered'), ('o3', NULL))
SELECT o.id, o.status IS DISTINCT FROM n.status AS changed
FROM old_v o JOIN new_v n USING (id)
ORDER BY o.id;
```

With plain `<>`, o2 and o3 would give UNKNOWN and a change-detection query would miss them.

## 7. Types and casting

Raw (bronze) columns are often all text. Cast in staging, and decide what happens to values that do not parse.

```sql
-- runnable
-- expect: [[12.5, null, "2018-01-15"]]
SELECT TRY_CAST('12.50' AS DECIMAL(12, 2))                    AS price,
       TRY_CAST('abc' AS INTEGER)                             AS bad_number,   -- NULL instead of an error
       CAST(strptime('2018-01-15 22:30:00', '%Y-%m-%d %H:%M:%S') AS DATE) AS purchase_date;
```

- `CAST(x AS type)` (or `x::type`) **fails** the whole query on a bad value — good for contracts you must enforce.
- `TRY_CAST` (DuckDB; `SAFE_CAST` in BigQuery) returns NULL instead — good for staging, but **count** how many non-blank inputs became NULL and report them as parse failures.
- Use `DECIMAL(p, s)` for money, never `FLOAT`/`DOUBLE` (see [[Datetime Decimal and Timezones]]).

## 8. Everyday filters

```sql
WHERE status IN ('delivered', 'shipped')
  AND purchase_ts >= TIMESTAMP '2018-01-01' AND purchase_ts < TIMESTAMP '2018-02-01'  -- half-open range
  AND customer_city ILIKE 'sao%'          -- case-insensitive pattern (PostgreSQL/DuckDB)
  AND price BETWEEN 10 AND 100            -- inclusive on both ends
```

Prefer half-open ranges (`>= start AND < end`) for timestamps: `BETWEEN '2018-01-01' AND '2018-01-31'` silently drops everything after midnight on the 31st.

## 9. Applying it to Olist

Olist does not distinguish "no payment" from "payment of zero": keep NULL, and report the number of orders without payment in the dashboard instead of hiding them with `COALESCE(…, 0)`. Bronze columns are text, so staging uses `TRY_CAST` plus a count of rejected values per column.

## 10. Common mistakes

| Mistake | What goes wrong | Fix |
|---|---|---|
| `x = NULL` | Always UNKNOWN; returns no rows | `x IS NULL` |
| `NOT IN (subquery)` with NULLs | Returns zero rows | `NOT EXISTS` |
| `COALESCE(amount, 0)` before `AVG` | Changes the metric's meaning | Decide the rule; keep NULL by default |
| `<>` to detect changes | Misses NULL ↔ value changes | `IS DISTINCT FROM` |
| `BETWEEN` on timestamps | Drops the last day's afternoon | Half-open range |
| `LIMIT` without `ORDER BY` | Non-deterministic rows | Always order first |

## 11. Exercises

1. Add an order with a missing amount and predict `AVG` with and without `COALESCE(amount, 0)`. Write both queries and explain which metric each one represents.
2. Write a query that counts, per column, how many non-blank text values fail `TRY_CAST` to their target type.
3. Find orders with no matching payment using `NOT EXISTS`, then with `LEFT JOIN … WHERE p.order_id IS NULL`. Do they agree?
4. Explain why `WHERE count(*) > 1` fails but `HAVING count(*) > 1` works.

> [!example]- Solution for 4
> `WHERE` is evaluated per row, before `GROUP BY` creates groups, so no aggregate exists yet. `HAVING` is evaluated per group after aggregation.

## 12. Review questions

> [!question]- What does `WHERE` do with a condition that evaluates to UNKNOWN?
> It drops the row: only TRUE passes.

> [!question]- Why can `NOT IN` return no rows at all?
> If the list contains NULL, every `x <> NULL` comparison is UNKNOWN, so `NOT IN` is never TRUE.

> [!question]- When is `COALESCE(x, 0)` correct?
> Only when the business rule says a missing value truly means zero (for example, no refund row means zero refunded). Otherwise it fabricates data and changes averages.

> [!question]- When would you use `CAST` instead of `TRY_CAST`?
> When a bad value must stop the pipeline (contract enforcement). `TRY_CAST` is for staging where failures are collected and reported.

Related: [[JOIN Grain and Fan-out]], [[Aggregation and Window Functions]], [[BI Metrics and Data Products]], [[Module 03 - SQL]]. Sources: [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html), [DuckDB NULL values](https://duckdb.org/docs/stable/sql/data_types/nulls.html), [DuckDB FILTER clause](https://duckdb.org/docs/stable/sql/query_syntax/filter.html).
