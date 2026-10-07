# Incremental transformations and correctness before pruning

Incremental materialization controls how dbt writes a model. It does not choose
the correct source versions for you. Event time, source version and extraction time
are different boundaries. A max-event-time filter can miss a late correction.
Deleting an entity from an aggregate input can also leave an old target total.

## Required syntax

~~~sql
{{ config(materialized='incremental',
          unique_key='sensor_id',
          incremental_strategy='delete+insert') }}
-- Supply your own SELECT, at the model's declared grain.
~~~

| Construct | What you must decide |
|---|---|
| config(...) | Materialization and an adapter-supported update strategy. |
| unique_key | The target row identity; it is not itself a database uniqueness test. |
| ref('model_name') | The upstream relation/dependency. |
| is_incremental() | True for an existing incremental model without full refresh; only add a filter when its correctness is justified. |
| dbt run --full-refresh | Rebuild for comparison; retain before/after evidence. |

The assignment starts conservatively: reconcile the entire current entity state,
including deletion state, before attempting scan pruning. Explain separately
whether target writes and source reads are incremental. Never label a full source
scan as a source-read optimization.

Before implementing, predict how a correction to an old event day and a deletion
affect the target. Choose tests that would catch an append-only answer. The exercise
specifies the retail interfaces; it does not provide your SELECT.

[Adapter reference](https://github.com/duckdb/dbt-duckdb).
[Incremental models](https://docs.getdbt.com/docs/build/incremental-models).
