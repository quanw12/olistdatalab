# 03 · SQL from zero

> **Theory notes:** [[SELECT NULL and CASE]] · [[JOIN Grain and Fan-out]] · [[Aggregation and Window Functions]] · [[CTE Dedup and Incremental SQL]] · [[Transactions Indexes and EXPLAIN]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 4–6 · **Prerequisites:** 01

## Goal
Answer business questions in SQL without help: filtering, joins, aggregation, CTEs, CASE, dates,
window functions. SQL is the most tested skill in every data interview.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [SQL Full Course for Beginners (30 h) — Data with Baraa](https://www.youtube.com/watch?v=SSKVgrwhzus) | Main course. Weeks 4–5: basics → joins → aggregations. Week 6: CTEs, subqueries, window functions | 30 h |
| [SQL Joins Basics (Visually Explained) — Data with Baraa](https://www.youtube.com/watch?v=aY7z4HcHm5M) | If joins feel unclear | 40 min |
| [SQL Window Functions Basics — Data with Baraa](https://www.youtube.com/watch?v=o666k19mZwE) | Before the window exercises | 57 min |
| [DuckDB Tutorial for Beginners — MotherDuck](https://www.youtube.com/watch?v=ZX5FdqzGT1E) | The engine this repo uses | 11 min |

Baraa uses SQL Server. The SQL is ~95% the same in DuckDB/PostgreSQL; the differences are listed below.
You already know Oracle — note its differences too.

## 2. Read
- [DuckDB SQL introduction](https://duckdb.org/docs/stable/sql/introduction) · [Window functions](https://duckdb.org/docs/stable/sql/functions/window_functions) · [ASOF join](https://duckdb.org/docs/stable/guides/sql_features/asof_join)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) (chapters 2–3)

## 3. Syntax sheet
```sql
-- order of writing:  SELECT … FROM … JOIN … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT
-- order of running:  FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

SELECT status, count(*) AS n, round(avg(amount), 2) AS avg_amount
FROM payments
WHERE amount > 0
GROUP BY status
HAVING count(*) > 10
ORDER BY n DESC;

-- CTE + CASE + LEFT JOIN that keeps rows without a match
WITH paid AS (
    SELECT order_id, sum(amount) AS total FROM payments GROUP BY order_id
)
SELECT o.order_id,
       coalesce(p.total, 0) AS total,          -- think: is 0 really right here?
       CASE WHEN p.order_id IS NULL THEN 'no payment' ELSE 'paid' END AS state
FROM orders o
LEFT JOIN paid p ON p.order_id = o.order_id;

-- window functions: a value per row, computed over a group of rows
SELECT seller_id, month, revenue,
       sum(revenue)  OVER (PARTITION BY seller_id ORDER BY month) AS running_total,
       lag(revenue)  OVER (PARTITION BY seller_id ORDER BY month) AS prev_month,
       rank()        OVER (PARTITION BY month ORDER BY revenue DESC) AS rank_in_month
FROM seller_month;

-- keep the latest row per key
SELECT * FROM events
QUALIFY row_number() OVER (PARTITION BY order_id ORDER BY event_time DESC) = 1;  -- DuckDB
```

| Concept | SQL Server (Baraa) | DuckDB / PostgreSQL | Oracle |
|---|---|---|---|
| first N rows | `SELECT TOP 10` | `LIMIT 10` | `FETCH FIRST 10 ROWS ONLY` |
| null default | `ISNULL(x, 0)` | `coalesce(x, 0)` | `NVL(x, 0)` |
| date part | `DATEPART(month, d)` | `month(d)` / `extract(month FROM d)` | `EXTRACT(MONTH FROM d)` |
| string concat | `a + b` | `a \|\| b` | `a \|\| b` |

## 4. Practice
- [LeetCode Top SQL 50](https://leetcode.com/studyplan/top-sql-50/): ~5 problems per week from now on, until the end of the roadmap.
- [SQLBolt](https://sqlbolt.com/) lessons 1–12 if Baraa's pace is too fast.

## 5. Apply to the project
Generate data and open it in SQL:
```powershell
olist sample --orders 5000
olist ingest                          # loads bronze.* tables into data/warehouse/olist.duckdb
duckdb data/warehouse/olist.duckdb    # CLI: winget install DuckDB.cli — or use DBeaver
```
Bronze columns are all text. Cast as you go (`price::DECIMAL(12,2)`, `strptime(ts, '%Y-%m-%d %H:%M:%S')`).
Write each answer as `analysis/q01.sql` … with the question as a comment:

1. How many orders per status? Per purchase month?
2. Top 10 sellers by item revenue (`order_items`). Hint: `GROUP BY seller_id`, sum `price`.
3. Average number of items per order — careful: orders with 0 items exist. Which join keeps them?
4. Orders whose total payment differs from the sum of their items + freight. Hint: aggregate
   each side **in its own CTE first**, then join the two summaries.
5. Customers (people, not `customer_id`!) with more than one order. Hint: read `customers` columns.
6. Month-over-month growth of payments with `lag()`.
7. For every seller, rank within their state by revenue.
8. **The fan-out trap:** join orders → items → payments in one query and `sum(payment_value)`.
   Compare with the true total. Explain the difference in one sentence in the file.

## 6. Self-check
- Why does `WHERE` not work with `count(*)` but `HAVING` does?
- `INNER` vs `LEFT` join: which rows disappear?
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` — draw a 5-row example.

## Done when
- [ ] Baraa SQL course up to window functions done
- [ ] 8 queries in `analysis/`, question 8 explained
- [ ] 15+ LeetCode SQL problems solved
