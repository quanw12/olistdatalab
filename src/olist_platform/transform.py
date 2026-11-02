"""Run the dbt project and publish the gold marts as Parquet."""

from __future__ import annotations

import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path

import duckdb

from olist_platform.config import PROJECT_DIR

logger = logging.getLogger(__name__)

DBT_DIR = PROJECT_DIR / "dbt"
GOLD_TABLES = [
    "fct_orders", "fct_order_items", "dim_customers", "dim_sellers", "dim_products", "dim_date",
    "mart_daily_revenue", "mart_seller_performance",
]


def dbt_executable() -> str:
    """Prefer the dbt next to this Python (same virtualenv), else whatever is on PATH."""
    scripts = Path(sys.executable).parent
    for name in ("dbt.exe", "dbt"):
        if (scripts / name).exists():
            return str(scripts / name)
    found = shutil.which("dbt")
    if not found:
        raise RuntimeError('dbt not found: pip install -e ".[dbt]"')
    return found


def run_dbt(duckdb_path: Path, command: str = "build", full_refresh: bool = False) -> None:
    """Run `dbt <command>` against the pipeline's DuckDB file. Raises if dbt fails."""
    args = [dbt_executable(), command, "--project-dir", str(DBT_DIR), "--profiles-dir",
            str(DBT_DIR)]
    if full_refresh:
        args.append("--full-refresh")
    env = {**os.environ, "DUCKDB_PATH": str(duckdb_path)}
    logger.info("running %s", " ".join(args[:2]))
    result = subprocess.run(args, env=env, cwd=DBT_DIR, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"dbt {command} failed with exit code {result.returncode}")


def export_gold(con: duckdb.DuckDBPyConnection, lake_dir: Path) -> dict[str, int]:
    """Copy every mart to lake/gold/<table>.parquet so other engines (Spark, BI) can read it."""
    counts = {}
    gold = lake_dir / "gold"
    gold.mkdir(parents=True, exist_ok=True)
    for table in GOLD_TABLES:
        target = gold / f"{table}.parquet"
        tmp = target.with_suffix(".parquet.tmp")
        con.execute(f"COPY marts.{table} TO '{tmp.as_posix()}' (FORMAT parquet)")
        tmp.replace(target)
        counts[table] = con.execute(f"SELECT count(*) FROM marts.{table}").fetchone()[0]
    logger.info("gold exported: %s", counts)
    return counts
