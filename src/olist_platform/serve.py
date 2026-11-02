"""Publish the gold marts to PostgreSQL, the serving database for BI tools (Metabase, Superset).

DuckDB is the build engine; Postgres is where many users and tools read concurrently. Each table
is rebuilt under a temporary name and swapped in, so dashboards never see a half-loaded table.
"""

from __future__ import annotations

import logging

import duckdb

from olist_platform.transform import GOLD_TABLES

logger = logging.getLogger(__name__)


def publish_to_postgres(con: duckdb.DuckDBPyConnection, dsn: str,
                        tables: list[str] = GOLD_TABLES) -> None:
    con.execute("INSTALL postgres")
    con.execute("LOAD postgres")
    con.execute(f"ATTACH '{dsn}' AS pg (TYPE postgres)")
    try:
        con.execute("CREATE SCHEMA IF NOT EXISTS pg.marts")
        for table in tables:
            con.execute(f"DROP TABLE IF EXISTS pg.marts.{table}__new")
            con.execute(f"CREATE TABLE pg.marts.{table}__new AS SELECT * FROM marts.{table}")
            con.execute(
                f"CALL postgres_execute('pg', 'BEGIN; "
                f"DROP TABLE IF EXISTS marts.{table}; "
                f"ALTER TABLE marts.{table}__new RENAME TO {table}; COMMIT;')"
            )
            logger.info("published marts.%s", table)
    finally:
        con.execute("DETACH pg")
