# dbt models, refs and dependency structure

## Understand it

dbt manages SQL transformations and dependencies. A model contains SELECT; materialization decides view/table. ref connects resources and resolves relation names. Seeds are small version-controlled CSV lab inputs, not production ingestion. dbt does not fetch APIs or replace the source loader.

## Syntax and trace

~~~sql
{{ config(materialized='table') }}
-- Toy pattern; some_active_orders must exist before running this.
select customer_id, sum(amount_cents) as total_cents
from {{ ref('some_active_orders') }}
group by customer_id
~~~

Jinja renders before SQL runs. ref uses the resource name without .sql.

## Engineering connection

Review a reproducible transformation graph instead of manual SQL copies.

[Reference](https://docs.getdbt.com/docs/build/models). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

