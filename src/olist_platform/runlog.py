"""Logging and run bookkeeping shared by every pipeline step."""

from __future__ import annotations

import logging
import uuid
from datetime import UTC, datetime
from pathlib import Path

import duckdb

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def setup_logging(log_dir: Path, step: str) -> None:
    """Log to the console and to logs/<step>.log, so a scheduler and a human both see the run."""
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_dir / f"{step}.log", encoding="utf-8"),
        ],
        force=True,
    )


def new_run_id() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]


def connect(duckdb_path: Path) -> duckdb.DuckDBPyConnection:
    duckdb_path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(duckdb_path))
    con.execute("CREATE SCHEMA IF NOT EXISTS bronze")
    con.execute("CREATE SCHEMA IF NOT EXISTS audit")
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS audit.pipeline_runs (
            run_id VARCHAR, step VARCHAR, status VARCHAR,
            started_at TIMESTAMPTZ, finished_at TIMESTAMPTZ, detail VARCHAR
        )
        """
    )
    return con


def record_run(
    con: duckdb.DuckDBPyConnection,
    run_id: str,
    step: str,
    status: str,
    started_at: datetime,
    detail: str = "",
) -> None:
    con.execute(
        "INSERT INTO audit.pipeline_runs VALUES (?, ?, ?, ?, ?, ?)",
        [run_id, step, status, started_at, datetime.now(UTC), detail],
    )
