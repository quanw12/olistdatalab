# 05 · dbt

**Time:** weeks 6–7 · **Stack:** dbt Core, dbt-duckdb, Jinja, tests, incremental models, docs

## Why
dbt is in most modern DE job posts. It turns SQL into a tested, documented, dependency-aware
project.

## Learn
- `ref`, `source`, materializations (view, table, ephemeral, incremental) — [dbt docs](https://docs.getdbt.com/docs/build/materializations)
- Generic tests vs singular tests; `--store-failures`
- Incremental strategies (`append`, `delete+insert`, `merge`) and the lookback window
- Snapshots (SCD type 2)
- `dbt docs generate` / lineage graph

## Read in this repo
- `dbt/dbt_project.yml`, `dbt/profiles.yml`
- `dbt/models/staging/*` — one model per source table, only renaming/typing
- `dbt/models/marts/mart_daily_revenue.sql` — incremental with lookback
- `dbt/tests/assert_money_reconciles.sql`

Run by hand: `cd dbt; $env:DUCKDB_PATH="..\data\warehouse\olist.duckdb"; dbt build --profiles-dir .`

## Build
1. `dbt docs generate && dbt docs serve` — screenshot the lineage graph for the README.
2. Add a snapshot of `stg_orders` on `order_status` (SCD2). Simulate a status change in the
   sample CSV, re-run, query the history.
3. Add `mart_category_monthly` (category × month revenue, review score) with tests.
4. Add `int_customer_orders` with each customer's order number (`ROW_NUMBER`), and a
   `is_repeat_customer` flag in `fct_orders`.
5. Install `dbt_utils` via `packages.yml` and replace the hand-written `unique_combination`.
6. Add a source freshness block and a model contract (`contract: enforced: true`) on `fct_orders`.

## Break it
- Run `mart_daily_revenue` incrementally after changing an old order's status in the CSV. Is the
  change picked up? What lookback would you need for the real data?

## Interview questions
- View vs table vs incremental: how do you choose?
- How do you test a dbt model? What does a failing `relationships` test tell you?
- What is an SCD type 2 and how does dbt build one?

## Done when
- [ ] Snapshot, new marts, `dbt_utils`, contract merged; `dbt build` green
- [ ] Lineage screenshot in the README
