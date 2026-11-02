"""Landing CSV -> bronze.

For every table in the contract:
1. hash the file; skip it if this exact file was already loaded (idempotent re-runs),
2. check the header against the contract (schema drift stops the run),
3. load all columns as text into a candidate table plus lineage columns,
4. run the contract checks on the candidate,
5. only if no error-level check failed, swap the candidate in as bronze.<table> and write the
   same rows to the Parquet lake for Spark and other engines.

Bronze keeps every value as text, exactly as received. Typing and cleaning happen in dbt staging,
so a bad value is visible and testable instead of silently lost at load time.
"""

from __future__ import annotations

import csv
import hashlib
import logging
from datetime import UTC, datetime
from pathlib import Path

import duckdb

from olist_platform.contracts import Contract, TableContract
from olist_platform.quality import CheckResult, run_checks

logger = logging.getLogger(__name__)


class ContractError(RuntimeError):
    """The source broke its contract; nothing was published for this table."""


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return [c.strip() for c in next(csv.reader(f), [])]


def check_schema(contract: TableContract, header: list[str]) -> list[str]:
    """Return extra columns (logged); raise when a contracted column is missing."""
    missing = [c for c in contract.columns if c not in header]
    if missing:
        raise ContractError(f"{contract.name}: missing columns {missing}")
    return [c for c in header if c not in contract.columns]


def _ensure_audit_tables(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS audit.ingest_manifest (
            run_id VARCHAR, table_name VARCHAR, source_file VARCHAR, file_sha256 VARCHAR,
            row_count BIGINT, loaded_at TIMESTAMPTZ
        )
        """
    )
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS audit.quality_results (
            run_id VARCHAR, table_name VARCHAR, check_name VARCHAR, severity VARCHAR,
            failed_rows BIGINT, checked_at TIMESTAMPTZ
        )
        """
    )


def already_loaded(con: duckdb.DuckDBPyConnection, table: str, sha: str) -> bool:
    row = con.execute(
        "SELECT 1 FROM audit.ingest_manifest WHERE table_name = ? AND file_sha256 = ? LIMIT 1",
        [table, sha],
    ).fetchone()
    exists = con.execute(
        "SELECT count(*) FROM information_schema.tables "
        "WHERE table_schema = 'bronze' AND table_name = ?",
        [table],
    ).fetchone()[0]
    return row is not None and exists == 1


def ingest_table(
    con: duckdb.DuckDBPyConnection,
    contract: TableContract,
    path: Path,
    lake_dir: Path,
    run_id: str,
    timestamp_format: str,
    force: bool = False,
) -> tuple[str, list[CheckResult]]:
    """Load one file. Return ("loaded" | "skipped", check results)."""
    _ensure_audit_tables(con)
    sha = sha256_of(path)
    if not force and already_loaded(con, contract.name, sha):
        logger.info("%s: unchanged file %s, skipped", contract.name, sha[:12])
        return "skipped", []

    extra = check_schema(contract, read_header(path))
    if extra:
        logger.warning("%s: extra columns ignored: %s", contract.name, extra)

    candidate = f"bronze.{contract.name}__candidate"
    columns = ", ".join(f'"{c}"' for c in contract.columns)
    con.execute(
        f"""
        CREATE OR REPLACE TABLE {candidate} AS
        SELECT {columns},
               ?::VARCHAR AS _source_file,
               ?::VARCHAR AS _file_sha256,
               ?::VARCHAR AS _run_id,
               ?::TIMESTAMPTZ AS _ingested_at
        FROM read_csv(?, header = true, all_varchar = true)
        """,
        [path.name, sha, run_id, datetime.now(UTC), str(path)],
    )
    results = run_checks(con, contract, candidate, timestamp_format)
    for r in results:
        if not r.passed:
            log = logger.error if r.severity == "error" else logger.warning
            log("%s: %s failed on %d rows", contract.name, r.check, r.failed_rows)
    con.executemany(
        "INSERT INTO audit.quality_results VALUES (?, ?, ?, ?, ?, ?)",
        [[run_id, r.table, r.check, r.severity, r.failed_rows, datetime.now(UTC)]
         for r in results],
    )
    errors = [r for r in results if r.severity == "error" and not r.passed]
    if errors:
        con.execute(f"DROP TABLE {candidate}")
        raise ContractError(
            f"{contract.name}: {len(errors)} contract check(s) failed, bronze not updated: "
            + ", ".join(r.check for r in errors)
        )

    row_count = con.execute(f"SELECT count(*) FROM {candidate}").fetchone()[0]
    con.execute("BEGIN TRANSACTION")
    con.execute(f"DROP TABLE IF EXISTS bronze.{contract.name}")
    con.execute(f"ALTER TABLE {candidate} RENAME TO {contract.name}")
    con.execute(
        "INSERT INTO audit.ingest_manifest VALUES (?, ?, ?, ?, ?, ?)",
        [run_id, contract.name, path.name, sha, row_count, datetime.now(UTC)],
    )
    con.execute("COMMIT")

    target = lake_dir / "bronze" / contract.name / f"{contract.name}.parquet"
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".parquet.tmp")
    con.execute(f"COPY bronze.{contract.name} TO '{tmp.as_posix()}' (FORMAT parquet)")
    tmp.replace(target)
    logger.info("%s: loaded %d rows from %s", contract.name, row_count, path.name)
    return "loaded", results


def ingest_all(
    con: duckdb.DuckDBPyConnection,
    contract: Contract,
    landing_dir: Path,
    lake_dir: Path,
    run_id: str,
    force: bool = False,
) -> dict[str, str]:
    """Ingest every contracted file. Fails on the first table that breaks its contract."""
    outcome: dict[str, str] = {}
    for table in contract.tables.values():
        path = landing_dir / table.file
        if not path.exists():
            if table.required:
                raise ContractError(f"{table.name}: required file not found: {path}")
            logger.info("%s: optional file %s not present", table.name, table.file)
            outcome[table.name] = "absent"
            continue
        status, _ = ingest_table(con, table, path, lake_dir, run_id,
                                 contract.timestamp_format, force)
        outcome[table.name] = status
    return outcome
