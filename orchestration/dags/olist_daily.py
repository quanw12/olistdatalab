"""Daily Olist batch: ingest -> fx -> dbt build -> publish -> (weekly) retrain.

Each task calls the same CLI you run by hand, so the DAG only adds what an orchestrator is for:
order, schedule, retries, alerting and a history of runs. Every CLI step is idempotent (unchanged
files are skipped, tables are swapped atomically), so retrying a task or clearing a run is safe.
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import ShortCircuitOperator
from airflow.sdk import dag

PROJECT = os.getenv("OLIST_PROJECT_DIR", "/opt/olist")
OLIST = f"cd {PROJECT} && python -m olist_platform"

DEFAULT_ARGS = {
    "owner": "data-eng",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "retry_exponential_backoff": True,
}


@dag(
    dag_id="olist_daily",
    schedule="0 6 * * *",
    start_date=datetime(2026, 11, 1),
    catchup=False,
    max_active_runs=1,  # one writer at a time: DuckDB allows a single writer
    default_args=DEFAULT_ARGS,
    tags=["olist", "batch"],
)
def olist_daily():
    ingest = BashOperator(task_id="ingest", bash_command=f"{OLIST} ingest")
    fx = BashOperator(task_id="fx_rates", bash_command=f"{OLIST} fx")
    transform = BashOperator(task_id="dbt_build", bash_command=f"{OLIST} transform")
    publish = BashOperator(task_id="publish_postgres", bash_command=f"{OLIST} serve")

    is_monday = ShortCircuitOperator(
        task_id="is_monday",
        # Airflow passes the run context; logical_date is the date the run is for.
        python_callable=lambda **context: context["logical_date"].weekday() == 0,
    )
    retrain = BashOperator(task_id="retrain_late_delivery", bash_command=f"{OLIST} ml-train")

    ingest >> fx >> transform >> [publish, is_monday]
    is_monday >> retrain


olist_daily()
