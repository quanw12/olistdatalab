# Incremental transformations and correctness before pruning

## Understand it

Incremental materialization updates a target, but correct source selection and replacement remain your responsibility. A max event-time filter misses late data. Appending aggregate totals preserves old corrections/deletes. First reconcile entity state against full rebuild; only then optimize scanning.

## Syntax and trace

~~~sql
{{ config(materialized='incremental', unique_key='id',
          incremental_strategy='delete+insert') }}
-- Conservative full-current-state input, including tombstones.
select * from {{ ref('latest_changes') }}
~~~

Scanning all latest state can be correct without saving source-read work. This is a conservative baseline, not a pruning optimization.

## Engineering connection

Correct revision semantics matter more than an incremental label.

[Reference](https://github.com/duckdb/dbt-duckdb). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

