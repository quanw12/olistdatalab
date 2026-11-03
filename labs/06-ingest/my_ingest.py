"""Lab 06 — your own idempotent, contract-checked loader for the orders file.

Make `pytest labs/06-ingest -v` green. Write `contract.yml` next to this file first; its shape:

    table: orders
    columns: [order_id, customer_id, order_status, ...all 8 columns...]
    primary_key: [order_id]
    not_null: [...]
    accepted_values:
      order_status: [...the 8 statuses...]
    timestamps: [...the 5 timestamp columns...]
    timestamp_format: "%Y-%m-%d %H:%M:%S"

Tables your code must create in the DuckDB connection it is given:
    orders                -> the published table (all text + lineage columns)
    orders__candidate     -> temporary, checked before publishing
    audit_manifest        -> (table_name, file_sha256, row_count, loaded_at)
"""

from __future__ import annotations

from pathlib import Path

import duckdb


class ContractError(RuntimeError):
    """The file broke the contract; nothing was published."""


def load_contract(path: Path) -> dict:
    """Read the YAML contract into a dict. Hint: yaml.safe_load."""
    raise NotImplementedError


def check_header(csv_path: Path, contract: dict) -> list[str]:
    """Compare the CSV header with contract["columns"].

    Missing contracted column -> raise ContractError naming the columns.
    Extra columns -> return their names (the caller logs them).
    Hint: csv.reader + next() gives the header row.
    """
    raise NotImplementedError


def load_candidate(con: duckdb.DuckDBPyConnection, csv_path: Path, contract: dict) -> int:
    """Create (or replace) <table>__candidate from the CSV and return its row count.

    Only the contracted columns, all as text (all_varchar), plus:
        _source_file (file name), _file_sha256, _loaded_at (timestamp)
    Hint: SELECT "col1", "col2", ..., ? AS _source_file ... FROM read_csv(?, all_varchar = true)
    """
    raise NotImplementedError


def run_checks(con: duckdb.DuckDBPyConnection, relation: str,
               contract: dict) -> list[tuple[str, str, int]]:
    """Return (check_name, severity, failed_rows) for every check, passing ones included.

    Check names the tests look for:
        "primary_key_unique"                         error
        "not_null(<col>)"            per column      error
        "accepted_values(<col>)"     per column      error  (compare lower(trim(value)))
        "parseable_timestamp(<col>)" per column      error  (blank is allowed; try_strptime)
        "delivered_without_delivery_date"            warn
    Hint: each check is one `SELECT count(*) ... WHERE <row is bad>`.
    A blank value: NULLIF(TRIM(x), '') IS NULL
    """
    raise NotImplementedError


def ingest(con: duckdb.DuckDBPyConnection, csv_path: Path, contract: dict) -> str:
    """Load one file. Return "loaded" or "skipped".

    1. sha256 of the file; if audit_manifest already has it for this table -> "skipped"
    2. check_header -> load_candidate -> run_checks
    3. any failing error check -> drop the candidate, raise ContractError naming the checks;
       the previously published table must stay untouched
    4. otherwise, in ONE transaction: drop old table, rename candidate, insert manifest row
    """
    raise NotImplementedError
