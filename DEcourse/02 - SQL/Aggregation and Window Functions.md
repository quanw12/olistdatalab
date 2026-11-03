---
tags: [decourse, sql, analytics]
module: 03
---

# Aggregation and Window Functions

> [!info] Learning goals
> After this note you can: aggregate with `GROUP BY` and filter groups with `HAVING`; explain how window functions differ from aggregates; write running totals, moving averages, percent-of-total, ranking, `LAG/LEAD` and "latest row per key" queries; choose between `ROWS` and `RANGE` frames; build a date spine so time-series metrics are honest; and compute month-over-month growth and retention correctly.

## 1. Aggregation collapses rows

`GROUP BY` turns many rows into one row per group. Every column in `SELECT` must either be in `GROUP BY` or wrapped in an aggregate.

```sql
-- runnable
-- expect: [["A", 2, 30, 15.0], ["B", 1, 30, 30.0]]
WITH sales(seller, day, amount) AS (
    VALUES ('A', DATE '2026-01-01', 10), ('A', DATE '2026-01-02', 20),
           ('B', DATE '2026-01-01', 30)
)
SELECT seller, count(*) AS n, sum(amount) AS revenue, avg(amount) AS average
FROM sales GROUP BY seller HAVING sum(amount) >= 30 ORDER BY seller;
-- Expected: A,2,30,15.0; B,1,30,30.0.
```

Common aggregates: `count(*)`, `count(col)`, `count(DISTINCT col)`, `sum`, `avg`, `min`, `max`, `median`/`quantile_cont` (DuckDB), `string_agg`, `list` (DuckDB), `bool_or`. Remember: `COUNT(col)` skips NULLs; `MIN/MAX` on text sort alphabetically, which is not a business order of statuses.

`WHERE` filters rows before grouping; `HAVING` filters groups after grouping ([[SELECT NULL and CASE]]).

### Grouping by time

```sql
-- runnable
-- expect: [["2018-01-01", 2, 150], ["2018-02-01", 1, 20]]
WITH orders(ts, amount) AS (
    VALUES (TIMESTAMP '2018-01-05 10:00', 100), (TIMESTAMP '2018-01-31 23:00', 50),
           (TIMESTAMP '2018-02-01 08:00', 20)
)
SELECT CAST(date_trunc('month', ts) AS DATE) AS month, count(*) AS orders, sum(amount) AS revenue
FROM orders GROUP BY 1 ORDER BY 1;
```

`date_trunc('month', ts)` maps every timestamp to the first instant of its month. Truncate the **business-local** timestamp, not the UTC one, when reporting per local day/month ([[Datetime Decimal and Timezones]]).

## 2. Window functions keep every row

A window function computes a value **for each row** using a set of related rows (the *window*), without collapsing them.

```text
function(...) OVER (
    PARTITION BY ...   -- split rows into independent groups (like GROUP BY, but rows stay)
    ORDER BY ...       -- order inside each partition
    ROWS/RANGE ...     -- the frame: which rows around the current row are included
)
```

```sql
-- runnable
-- expect: [["2026-01-01", 10, 10, 10.0, null], ["2026-01-02", 20, 30, 15.0, 10], ["2026-01-03", 30, 60, 25.0, 20]]
WITH daily(day, revenue) AS (
    VALUES (DATE '2026-01-01', 10), (DATE '2026-01-02', 20),
           (DATE '2026-01-03', 30)
)
SELECT day, revenue,
       sum(revenue) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running,
       avg(revenue) OVER (ORDER BY day ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS moving_2_rows,
       lag(revenue) OVER (ORDER BY day) AS previous
FROM daily ORDER BY day;
-- Expected running: 10,30,60; moving: 10,15,25; previous: NULL,10,20.
```

- `PARTITION BY seller` computes the window separately for each seller — unlike `GROUP BY`, the number of rows does not change.
- Without `PARTITION BY`, the whole result is one partition.
- Two rows with the same `ORDER BY` value are **peers**; if their order affects the result (ranking, `lag`, running totals with `ROWS`), add a tie-breaker column.

### Percent of total and share within a group

```sql
-- runnable
-- expect: [["A", "SP", 60, 60.0, 75.0], ["B", "SP", 20, 20.0, 25.0], ["C", "RJ", 20, 20.0, 100.0]]
WITH s(seller, state, revenue) AS (VALUES ('A', 'SP', 60), ('B', 'SP', 20), ('C', 'RJ', 20))
SELECT seller, state, revenue,
       100.0 * revenue / sum(revenue) OVER ()                      AS pct_of_total,
       100.0 * revenue / sum(revenue) OVER (PARTITION BY state)    AS pct_of_state
FROM s ORDER BY seller;
```

`OVER ()` means "all rows". This is impossible with plain `GROUP BY` without a second query and a join.

## 3. Frames: ROWS vs RANGE

The frame decides which rows around the current row are aggregated.

- `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` — the current row and the 6 **physical rows** before it.
- `RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW` — all rows whose `ORDER BY` **value** lies within 6 days before the current value (and all peers with the same value).

```sql
-- runnable
-- expect: [["2026-01-01", 10, 10], ["2026-01-03", 40, 30]]
WITH daily(day, revenue) AS (VALUES (DATE '2026-01-01', 10), (DATE '2026-01-03', 30))
SELECT day,
       sum(revenue) OVER (ORDER BY day ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)                 AS rows_sum,
       sum(revenue) OVER (ORDER BY day RANGE BETWEEN INTERVAL 1 DAY PRECEDING AND CURRENT ROW)   AS range_sum
FROM daily ORDER BY day;
```

On 3 January, "1 preceding row" is 1 January (two days ago), but "1 preceding day" (2 January) has no data. A "7-row moving average" is a 7-**day** average only if there is exactly one row per day, including days with no sales.

Default frames are a trap: with `ORDER BY` and no frame, the default is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. That is why `last_value(x) OVER (ORDER BY day)` returns the *current* row's value, not the last in the partition. Write `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` when you mean the whole partition.

### Date spine: make missing days explicit

```sql
-- runnable
-- expect: [["2026-01-01", 10], ["2026-01-02", 0], ["2026-01-03", 30]]
WITH sales(day, amount) AS (VALUES (DATE '2026-01-01', 10), (DATE '2026-01-03', 30)),
spine AS (
    SELECT CAST(d AS DATE) AS day
    FROM generate_series(DATE '2026-01-01', DATE '2026-01-03', INTERVAL 1 DAY) t(d)
)
SELECT spine.day, coalesce(sum(sales.amount), 0) AS revenue
FROM spine LEFT JOIN sales ON sales.day = spine.day
GROUP BY spine.day ORDER BY spine.day;
```

Here `COALESCE(…, 0)` is honest: a day with no orders really had zero revenue. Build the spine first, then compute moving averages and `lag` over it.

## 4. Ranking and top-N

```sql
-- runnable
-- expect: [["A", 1, 1, 1], ["B", 2, 1, 1], ["C", 3, 3, 2]]
WITH scores(seller, revenue) AS (VALUES ('A',100), ('B',100), ('C',50))
SELECT seller,
       row_number() OVER (ORDER BY revenue DESC, seller) AS row_n,
       rank() OVER (ORDER BY revenue DESC) AS rank_n,
       dense_rank() OVER (ORDER BY revenue DESC) AS dense_n
FROM scores ORDER BY seller;
-- Expected: A 1,1,1; B 2,1,1; C 3,3,2.
```

| Function | Ties | Gaps after ties | Use |
|---|---|---|---|
| `row_number()` | broken arbitrarily unless you add a tie-breaker | — | dedup, exactly N rows |
| `rank()` | same rank | yes (1,1,3) | competition ranking |
| `dense_rank()` | same rank | no (1,1,2) | "top 3 revenue levels" |
| `ntile(4)` | — | — | quartiles |

"Top 10 sellers" can mean 10 rows (`row_number`) or everyone in the top 10 revenue levels (`dense_rank`). Decide whether ties are kept.

### Latest row per key with QUALIFY

```sql
-- runnable
-- expect: [["o1", "delivered"], ["o2", "shipped"]]
WITH events(order_id, status, event_time, event_id) AS (
    VALUES ('o1', 'shipped',   TIMESTAMP '2018-01-02 10:00', 1),
           ('o1', 'delivered', TIMESTAMP '2018-01-05 09:00', 2),
           ('o2', 'shipped',   TIMESTAMP '2018-01-03 12:00', 3)
)
SELECT order_id, status FROM events
QUALIFY row_number() OVER (PARTITION BY order_id ORDER BY event_time DESC, event_id DESC) = 1
ORDER BY order_id;
```

`QUALIFY` filters on window results (DuckDB, BigQuery, Snowflake). In PostgreSQL wrap the window in a CTE and filter with `WHERE rn = 1`. Deduplication rules are covered in [[CTE Dedup and Incremental SQL]].

## 5. LAG, LEAD and period-over-period

```sql
-- runnable
-- expect: [["2018-01-01", 100, null], ["2018-02-01", 150, 50.0], ["2018-03-01", 0, -100.0], ["2018-04-01", 30, null]]
WITH monthly(month, revenue) AS (
    VALUES (DATE '2018-01-01', 100), (DATE '2018-02-01', 150),
           (DATE '2018-03-01', 0), (DATE '2018-04-01', 30)
), compared AS (
    SELECT month, revenue, lag(revenue) OVER (ORDER BY month) AS previous FROM monthly
)
SELECT month, revenue, round(100.0 * (revenue - previous) / NULLIF(previous, 0), 1) AS growth_pct
FROM compared ORDER BY month;
```

- `lag(x, k)` = value k rows **before**; `lead(x, k)` = k rows **after**; both accept a default for the edges.
- `NULLIF(previous, 0)` avoids division by zero: growth after a zero month is undefined, not infinite.
- `lag` looks at the previous **row**, not the previous **month**. If a month is missing, the comparison silently jumps two months — build a month spine first.

## 6. Retention and cohorts

Retention answers "of the customers who first bought in month M, what share bought again in month M+k?"

```sql
-- runnable
-- expect: [["2018-01-01", 0, 3, 100.0], ["2018-01-01", 1, 1, 33.3], ["2018-01-01", 2, 1, 33.3]]
WITH orders(customer, order_month) AS (
    VALUES ('c1', DATE '2018-01-01'), ('c1', DATE '2018-02-01'),
           ('c2', DATE '2018-01-01'), ('c2', DATE '2018-01-01'),
           ('c3', DATE '2018-01-01'), ('c3', DATE '2018-03-01')
), firsts AS (
    SELECT customer, min(order_month) AS cohort FROM orders GROUP BY customer
), activity AS (
    SELECT DISTINCT o.customer, f.cohort,
           datediff('month', f.cohort, o.order_month) AS month_number
    FROM orders o JOIN firsts f USING (customer)
), sizes AS (
    SELECT cohort, count(*) AS cohort_size FROM firsts GROUP BY cohort
)
SELECT a.cohort, a.month_number, count(*) AS active_customers,
       round(100.0 * count(*) / s.cohort_size, 1) AS retention_pct
FROM activity a JOIN sizes s USING (cohort)
GROUP BY a.cohort, a.month_number, s.cohort_size
ORDER BY a.cohort, a.month_number;
```

Key points: count **distinct people**, not orders (c2's two January orders count once); the denominator is the fixed cohort size; and recent cohorts have not been observed long enough for later months — mark those cells as "not yet observable", not 0%. In Olist the person is `customer_unique_id`; `customer_id` is a new id per order.

## 7. Performance notes

Each distinct `PARTITION BY … ORDER BY` needs a sort (or hash partitioning plus sort). In distributed engines that means a shuffle ([[Spark Partitions Shuffle and Skew]]). Reuse the same window specification (`WINDOW w AS (PARTITION BY seller ORDER BY day)`) and filter rows *before* the window when possible. A window over the whole table without `PARTITION BY` runs on a single thread/worker in many engines.

## 8. Applying it to Olist

Revenue per month (local date), seller rank within each state, share of revenue by category, repeat customers by `customer_unique_id`, and a 7-day moving average of orders over a date spine.

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Moving average over rows with gaps | Not a true N-day average | Date spine or `RANGE` with an interval |
| `last_value` with the default frame | Returns the current row | Explicit full frame |
| `row_number()` without a tie-breaker | Non-deterministic dedup | Add a unique column to `ORDER BY` |
| `lag` across missing months | Wrong growth | Month spine |
| Counting orders for retention | Overstates returning customers | `count(DISTINCT person)` |
| Cohort denominator changing with month | Inconsistent percentages | Fixed cohort size |

## 10. Exercises

1. Add a missing day and two sellers with equal revenue. Predict `ROWS` vs `RANGE` sums and each ranking function before running.
2. Compute each seller's revenue rank within their state and keep the top 3 per state with `QUALIFY`.
3. Compute a 7-day moving average of daily Olist orders over a date spine.
4. Build the cohort table for Olist with `customer_unique_id`. Which cohorts are not fully observable yet?

> [!example]- Hint for 2
> `QUALIFY dense_rank() OVER (PARTITION BY seller_state ORDER BY revenue DESC) <= 3` keeps ties; use `row_number()` with a tie-breaker if you need exactly 3 rows.

## 11. Review questions

> [!question]- How does `OVER` differ from `GROUP BY`?
> `GROUP BY` collapses each group into one row; a window function adds a computed value to every row while keeping all rows.

> [!question]- Why can `lag` produce a wrong month-over-month growth?
> It takes the previous row. If a month has no row, the "previous" value is from two months earlier. A month spine fixes this.

> [!question]- When does a window function become expensive?
> When it forces large sorts or shuffles: big partitions, many different window specifications, or no `PARTITION BY` on a large table.

> [!question]- Why is `COALESCE(sum, 0)` honest on a date spine but not on a payments join?
> On a spine, a day without rows really had zero sales. For a payment that might exist but is missing, zero fabricates a fact.

Related: [[CTE Dedup and Incremental SQL]], [[SELECT NULL and CASE]], [[BI Metrics and Data Products]], [[Module 03 - SQL]]. Sources: [DuckDB window functions](https://duckdb.org/docs/stable/sql/functions/window_functions.html), [PostgreSQL window tutorial](https://www.postgresql.org/docs/current/tutorial-window.html), [DuckDB QUALIFY](https://duckdb.org/docs/stable/sql/query_syntax/qualify.html).
