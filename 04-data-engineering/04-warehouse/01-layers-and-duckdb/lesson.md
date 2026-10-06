# Warehouse layers and a local analytical engine

## Understand it

ETL transforms before loading; ELT loads then transforms in the analytical destination. Raw preserves source evidence, staging establishes types, current selects revisions, and a mart exposes business grain. DuckDB is an embedded analytical engine for this lab, separate from PostgreSQL transactions. Parquet preserves types and supports column-oriented reads; CSV is interoperable but weakly typed.

## Syntax and trace

~~~python
import duckdb
with duckdb.connect() as con:
    print(con.execute("SELECT sum(x) FROM (VALUES (10), (20)) t(x)").fetchone())
~~~

The local query returns (30,). A file-backed connection persists; an in-memory connection disappears on close.

## Engineering connection

Practise analytical transformations locally before adding a cloud account.

[Reference](https://duckdb.org/docs/stable/clients/python/overview). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

