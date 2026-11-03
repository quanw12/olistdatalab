---
tags: [decourse, dbt, transformation]
module: 09
---

# dbt: Models, Tests and Incremental

> [!info] Learning goals
> After this note you can: explain what dbt does and does not do; structure a project into sources, staging, intermediate and marts; use `source()`, `ref()` and Jinja; choose a materialization; write generic and singular tests and source freshness checks; build incremental models and snapshots (SCD2); run selected parts of the DAG; and know why "running twice gives the same result" does not prove an incremental model is correct.

## 1. What dbt is

dbt (data build tool) turns a folder of `SELECT` statements into a tested, documented **dependency graph** that runs inside your warehouse (DuckDB, Postgres, BigQuery, Snowflake…). You write the transformation as a SELECT; dbt wraps it in the DDL (`CREATE TABLE AS`, `CREATE VIEW`, `MERGE`) for your adapter, runs models in dependency order, and runs tests.

dbt does **not** extract or load data (that is ingestion), schedule itself (that is Airflow or dbt Cloud), or know whether your business metric is right. It makes SQL projects maintainable: version control, modularity, tests, docs and environments.

## 2. Project layout

```text
dbt/
  dbt_project.yml          # project name, model paths, default materializations
  profiles.yml             # connection per target (dev/prod)  — keep secrets in env vars
  models/
    staging/               # 1:1 with source tables: rename, cast, light cleaning
      _sources.yml
      stg_orders.sql
      stg_payments.sql
    intermediate/          # reusable joins/aggregations, not exposed to users
      int_payments_per_order.sql
    marts/                 # facts and dimensions for consumers
      fct_orders.sql
      dim_sellers.sql
      _marts.yml           # docs + tests
  tests/                   # singular tests (SQL returning violating rows)
  macros/                  # reusable Jinja functions
  snapshots/               # SCD2 snapshots
  seeds/                   # small CSVs versioned with code (e.g. status mappings)
```

Naming convention: `stg_` (staging), `int_` (intermediate), `fct_` (facts), `dim_` (dimensions). Staging models are the only ones that read sources directly.

## 3. Models, `source()` and `ref()`

```sql
-- models/staging/stg_payments.sql
select
    order_id,
    cast(payment_sequential as integer)        as payment_sequential,
    payment_type,
    cast(payment_value as decimal(12, 2))      as amount
from {{ source('bronze', 'order_payments') }}
```

```sql
-- models/marts/fct_orders.sql
with payments as (
    select order_id, sum(amount) as payment_total
    from {{ ref('stg_payments') }}
    group by order_id
)
select o.order_id, o.customer_id, o.purchase_date_local, p.payment_total
from {{ ref('stg_orders') }} o
left join payments p using (order_id)
```

- `source('bronze', 'order_payments')` points to a raw table declared in YAML, so dbt knows lineage and can check its freshness.
- `ref('stg_payments')` declares a dependency **and** resolves the right schema for the current target (e.g., `dev_alice.stg_payments` vs `prod.stg_payments`). Never hard-code table names between models; without `ref` dbt cannot order the DAG.
- `{{ … }}` is **Jinja**: dbt compiles it to plain SQL before running. Inspect the result in `target/compiled/`.

```yaml
# models/staging/_sources.yml
version: 2
sources:
  - name: bronze
    schema: bronze
    loaded_at_field: _loaded_at
    freshness:
      warn_after: {count: 24, period: hour}
      error_after: {count: 48, period: hour}
    tables:
      - name: order_payments
      - name: orders
```

## 4. Materializations

| Materialization | Choose when | Cost |
|---|---|---|
| `view` | Light logic, always fresh, rarely queried | Recomputed on every query |
| `table` | Read often; full rebuild is affordable | Storage and rebuild time |
| `incremental` | Large inputs and you can identify changes correctly | Complexity: watermarks, deletes, backfills |
| `ephemeral` | Helper CTE inlined into downstream models | Large compiled SQL, no relation to debug |
| snapshot | Track changes of a mutable source as SCD2 | Storage; runs on its own schedule |

Configure per folder in `dbt_project.yml` (`staging: +materialized: view`, `marts: +materialized: table`) or per model with `{{ config(materialized='table') }}`.

## 5. Tests

**Generic tests** are declared in YAML and reused:

```yaml
# models/marts/_marts.yml
version: 2
models:
  - name: fct_orders
    description: One row per order. Money in BRL, DECIMAL(12,2).
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: customer_id
        tests:
          - relationships: {to: ref('dim_customers'), field: customer_id}
      - name: order_status
        tests:
          - accepted_values:
              values: [created, approved, invoiced, processing, shipped, delivered, canceled, unavailable]
```

**Singular tests** are SQL files in `tests/` that return the violating rows; zero rows = pass:

```sql
-- tests/assert_payments_reconcile.sql
select abs(src.total - mart.total) as diff
from (select sum(payment_value) as total from {{ source('bronze', 'order_payments') }}) src,
     (select sum(payment_total) as total from {{ ref('fct_orders') }}) mart
where abs(src.total - mart.total) > 0.01
```

The logic behind a singular test can be tried in plain DuckDB:

```sql
-- runnable
-- expect: [["o2", 2]]
WITH fct_orders(order_id) AS (VALUES ('o1'), ('o2'), ('o2'))
SELECT order_id, count(*) AS n
FROM fct_orders
GROUP BY order_id HAVING count(*) <> 1;    -- dbt fails the test because a row came back
```

A `unique` test proves the key is unique; it does not prove you chose the right grain or that no rows are missing — add row-count and reconciliation tests. Use `severity: warn` for checks that should not block, and `--store-failures` to keep failing rows in a table for investigation.

## 6. Commands

```bash
dbt debug --profiles-dir .                         # connection and config check
dbt build --profiles-dir .                         # run + test everything in DAG order
dbt build --profiles-dir . --select fct_orders+    # a model and everything downstream
dbt build --profiles-dir . --select +fct_orders    # a model and everything upstream
dbt test  --profiles-dir . --select fct_orders --store-failures
dbt source freshness --profiles-dir .
dbt docs generate --profiles-dir . && dbt docs serve --profiles-dir .
dbt build --profiles-dir . --full-refresh          # rebuild incremental models from scratch
```

The repo's `olist transform` command orchestrates build and export. When calling dbt directly, check `DUCKDB_PATH` so you do not run against the wrong warehouse.

## 7. Incremental models

```sql
-- models/marts/fct_daily_revenue.sql
{{ config(materialized='incremental', unique_key='order_date', incremental_strategy='delete+insert') }}

select purchase_date_local as order_date, sum(payment_total) as revenue
from {{ ref('fct_orders') }}
{% if is_incremental() %}
where purchase_date_local >= (select max(order_date) - interval 3 day from {{ this }})
{% endif %}
group by 1
```

- First run (or `--full-refresh`): `is_incremental()` is false, the whole table is built.
- Later runs: only the filtered rows are computed and merged by `unique_key` using the adapter's strategy (`append`, `merge`, `delete+insert`, `insert_overwrite`).
- `{{ this }}` refers to the existing table.

**Why this example is not fully correct:** the 3-day lookback is on `order_date`, so an order from 30 days ago corrected today is never reprocessed. And if every order of a day is deleted, the `delete+insert` strategy deletes only keys present in the new batch — the stale day remains. "Running twice gives the same result" proves idempotency, not correctness. The proper fix (track affected keys/partitions by change time, rebuild exactly those, and compare with a full refresh) is the subject of [[Incremental CDC and Backfill]] and module 19. Do not simply increase the lookback without understanding the source.

## 8. Snapshots (SCD2)

```sql
-- snapshots/sellers_snapshot.sql
{% snapshot sellers_snapshot %}
{{ config(target_schema='snapshots', unique_key='seller_id',
          strategy='check', check_cols=['seller_city', 'seller_state']) }}
select * from {{ source('bronze', 'sellers') }}
{% endsnapshot %}
```

`dbt snapshot` compares the source with the stored history and adds `dbt_valid_from` / `dbt_valid_to` columns — an SCD2 table ([[Data Modeling and SCD2]]). Strategy `timestamp` uses an `updated_at` column; `check` compares listed columns. Snapshots only see changes at the moments they run.

## 9. Macros and packages

Macros are Jinja functions for repeated SQL, e.g. a cents-to-currency conversion or a surrogate key. Packages like `dbt_utils` (`generate_surrogate_key`, `date_spine`, `equal_rowcount`) and `dbt_expectations` add tested helpers; install with `packages.yml` + `dbt deps`.

## 10. Applying it to Olist

Module 09 runs the real Olist data early: source vs fact counts, reconciliation to the cent, key tests, docs and lineage. Then change an order older than 30 days and compare the incremental daily mart with a full refresh. Practise snapshots on simulated seller changes.

## 11. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Hard-coded table names instead of `ref` | Wrong order, wrong environment | Always `ref`/`source` |
| Business logic in staging | Hard to reuse and test | Staging = rename/cast only |
| Only `unique`/`not_null` tests | Wrong grain or lost rows unnoticed | Row-count and reconciliation tests |
| Lookback on business date | Old corrections missed | Change-time tracking; compare with full refresh |
| Never running `--full-refresh` in CI/dev | Drift between incremental and truth | Periodic full rebuild comparison |
| Running against the wrong target | Overwrites the wrong data | Check `dbt debug` / env vars first |

## 12. Exercises

1. Build `stg_orders`, `stg_payments` and `fct_orders` for Olist with tests for grain, relationships and payment reconciliation.
2. Write a singular test that fails if any order has items but no payment, with `severity: warn`.
3. Make the daily revenue mart incremental, update a 30-day-old order, and compare with `--full-refresh` using a two-way `EXCEPT ALL`.
4. Create a snapshot of sellers and simulate two changes; check the validity ranges.

## 13. Review questions

> [!question]- What does `ref()` give you besides the table name?
> A declared dependency (so dbt builds models in the right order and draws lineage) and environment-aware resolution of the schema/database.

> [!question]- Does a passing `unique` test prove the grain is correct?
> No. It proves uniqueness of that column. The grain could still be wrong (wrong key chosen) or rows could be missing; add count and reconciliation tests.

> [!question]- Snapshot vs incremental fact?
> A snapshot records history of a mutable entity (SCD2 dimension). An incremental fact processes only new or changed events to save compute; it does not keep versions unless you design it to.

> [!question]- Why can an incremental model be idempotent but still wrong?
> Re-running the same window gives the same output, but changes outside the window (old corrections, deletes) are never processed.

Related: [[Data Modeling and SCD2]], [[CTE Dedup and Incremental SQL]], [[Incremental CDC and Backfill]], [[Module 09 - dbt]]. Sources: [dbt models](https://docs.getdbt.com/docs/build/models), [dbt data tests](https://docs.getdbt.com/docs/build/data-tests), [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models), [dbt snapshots](https://docs.getdbt.com/docs/build/snapshots).
