# 02 · SQL and data modelling

**Time:** weeks 2–3 · **Stack:** SQL, DuckDB, star schema, window functions (Oracle/Postgres comparison)

## Why
SQL is the most tested skill in DE interviews. Modelling (grain, facts, dimensions) is what
separates a data engineer from someone who only writes queries.

## Learn
- Grain, facts, dimensions, slowly changing dimensions — Kimball's *The Data Warehouse Toolkit* ch. 1–3, or [Kimball techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
- Joins and fan-out, `GROUP BY`, `HAVING`, CTEs, window functions (`ROW_NUMBER`, `LAG`, running totals)
- DuckDB SQL: `ASOF JOIN`, `QUALIFY`, `GROUP BY ALL` — [DuckDB docs](https://duckdb.org/docs/sql/introduction)
- You know Oracle: write down 5 differences (e.g. `ROWNUM` vs `LIMIT`, `NVL` vs `COALESCE`, `DUAL`, date math, `MERGE`).

## Read in this repo
- `docs/data-contract.md` — the grain table.
- `dbt/models/marts/fct_orders.sql` — why items and payments are pre-aggregated.
- `dbt/models/intermediate/int_fx_daily.sql` — an `ASOF JOIN` with a tolerance.

Open the warehouse: `pip install duckdb` gives a CLI too, or use DBeaver with the DuckDB driver.

## Build
Write each query in `analysis/` (new folder) as a `.sql` file with the question as a comment:
1. Monthly payments (BRL and USD) and month-over-month growth with `LAG`.
2. Top 10 categories by item revenue, and each one's share of total (window `SUM() OVER ()`).
3. Repeat-purchase rate: share of `customer_unique_id` with 2+ orders.
4. For each seller, their rank by revenue within their state (`RANK() OVER (PARTITION BY ...)`).
5. Median delivery days per customer state, delivered orders only.
6. Show the fan-out bug: join orders → items → payments directly, compare `sum(payment_value)` to the correct total. **Check:** you can explain the exact difference.

## Break it
- Change `fct_orders` to join raw items instead of `int_order_items_by_order`. Run `dbt build`.
  Which test fails, and with which numbers?

## Interview questions
- What is the grain of `fct_orders`? Of `fct_order_items`? Why both?
- `customer_id` vs `customer_unique_id`: which do you count for "customers" and why?
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK`.
- How would you model an order whose status changes over time? (SCD2 / snapshot)

## Done when
- [ ] Six queries committed, results checked by a second method
- [ ] You can draw the star schema from memory
- [ ] You can explain the fan-out with numbers
