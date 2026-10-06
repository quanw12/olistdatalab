# A complete retail pipeline portfolio

## Understand it

A portfolio should connect business requirements to code, data guarantees, tests and recovery. Use one coherent stack and one trustworthy project. Separate data ingestion, authoritative current state, warehouse transformations, quality gates and orchestration. A diagram and tool list are not executable evidence.

## Syntax and trace

~~~text
fixed source batches -> contract/quarantine -> PostgreSQL history/current/ledger
    -> recoverable export -> DuckDB/dbt current + customer mart
    -> reconciliation gate -> report
Prefect coordinates; Git/CI and Docker package tested components.
~~~

PostgreSQL commit and export/warehouse publication are separate boundaries with explicit recovery. One writer avoids conflicting state builds in this learning project.

## Engineering connection

Combine your existing weather and Python practice into a defensible new-domain deliverable.

Original practice contract; review [sources.md](../../sources.md) for context.

