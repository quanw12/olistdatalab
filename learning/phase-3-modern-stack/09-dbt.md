# 09 · dbt (data build tool)

**Level:** Intermediate → Advanced · **Weeks:** 15–16 · **Prerequisite:** 03, 05, 06

## Goal
Turn SQL into a tested, documented, dependency-aware project: sources, staging, marts, tests,
incremental models, snapshots, docs and lineage.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [dbt crash course for beginners: Zero to Hero — Data Tech](https://www.youtube.com/watch?v=C6BNAfaeqXY) | All — start here | 1 h 24 |
| [dbt for Data Analytics & Engineering — Full Course — Luke Barousse](https://www.youtube.com/watch?v=1Bf049kXV2g) | Main course; skip parts on a cloud warehouse you don't use | 8 h 29 |
| [How to Build Incremental Models — Kahan Data Solutions](https://www.youtube.com/watch?v=-9RzZRkHay4) | Week 16 | 11 min |
| [How to use dbt Snapshots — Kahan Data Solutions](https://www.youtube.com/watch?v=SNtM_RUa5G4) | Week 16 | 11 min |
| Alternative long course: [DBT — The Ultimate Guide with CI/CD — Ansh Lamba](https://www.youtube.com/watch?v=B8uwFmVt4sU) | If you want a second explanation | 5 h |

Official free course: [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) (uses dbt Cloud; ideas are identical to dbt Core here).

## 2. Read
- [dbt: about models](https://docs.getdbt.com/docs/build/models) · [sources](https://docs.getdbt.com/docs/build/sources) · [data tests](https://docs.getdbt.com/docs/build/data-tests) · [materializations](https://docs.getdbt.com/docs/build/materializations) · [incremental models](https://docs.getdbt.com/docs/build/incremental-models) · [snapshots](https://docs.getdbt.com/docs/build/snapshots)
- [Jinja in dbt](https://docs.getdbt.com/docs/build/jinja-macros) · [dbt-duckdb adapter](https://github.com/duckdb/dbt-duckdb)
- [dbt best-practice project structure](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview)

## 3. Syntax sheet
```sql
-- models/staging/stg_payments.sql : rename + type only, one model per source table
select
    trim(order_id)                 as order_id,
    payment_value::decimal(12, 2)  as payment_value
from {{ source('bronze', 'order_payments') }}

-- models/marts/fct_x.sql : build on other models with ref()
{{ config(materialized='table') }}
select o.order_id, p.total
from {{ ref('stg_orders') }} o
left join {{ ref('int_payments_by_order') }} p using (order_id)

-- incremental: only process new/changed rows on later runs
{{ config(materialized='incremental', unique_key='day', incremental_strategy='delete+insert') }}
select day, count(*) as n from {{ ref('fct_x') }}
{% if is_incremental() %}
where day >= (select max(day) - 3 from {{ this }})     -- lookback for late changes
{% endif %}
group by day
```
```yaml
# models/marts/_marts.yml
models:
  - name: fct_x
    columns:
      - name: order_id
        data_tests: [unique, not_null]
      - name: status
        data_tests:
          - accepted_values:
              arguments:
                values: [paid, refunded]
```
```powershell
dbt build                       # run models + tests in dependency order
dbt build --select fct_orders+  # one model and everything downstream
dbt test --select stg_orders --store-failures
dbt docs generate; dbt docs serve
```

## 4. Practice
Follow the Data Tech crash course with its own example project from scratch (`dbt init`) on DuckDB.

## 5. Apply to the project
Build **your own** dbt project in `labs/09-dbt/` (copy only `profiles.yml` from `dbt/`, nothing else)
on top of the bronze tables from `olist ingest`:
1. `sources.yml` for the bronze tables; staging models for orders, items, payments, customers.
   Hint: cast in staging; normalise status; convert time — read the macro idea in module 01.
2. Two intermediate models: items per order, payments per order.
3. `fct_orders` with one row per order. Add tests: unique/not_null key, accepted statuses,
   and a **singular test** that fails if `fct_orders` row count ≠ `stg_orders` row count.
4. A singular test that reconciles payment money between source and fact to the cent.
5. An incremental `daily_revenue`; run it twice and prove the second run gives the same totals.
6. A snapshot on order status; change one status in the CSV, re-ingest, re-run, query history.
7. `dbt docs serve` → screenshot of your lineage graph.

Then diff your project against `dbt/` and list improvements in both directions.

## 6. Self-check
- view vs table vs incremental vs ephemeral — when each?
- What exactly does `ref()` give you besides the table name?
- A relationships test fails. What does that tell you about the data?

## Done when
- [ ] Your dbt project builds green with the 2 singular tests
- [ ] Incremental + snapshot demonstrated; lineage screenshot committed
