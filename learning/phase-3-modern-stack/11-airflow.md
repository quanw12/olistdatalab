# 11 · Orchestration with Apache Airflow

**Level:** Advanced · **Weeks:** 19–20 · **Prerequisite:** 08, 09, 10

## Goal
Schedule the pipeline with dependencies, retries, alerting and backfills, and understand why every
task must be safe to re-run.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Learn Apache Airflow in 10 Minutes — Darshil Parmar](https://www.youtube.com/watch?v=5peQThvQmQk) | Overview first | 13 min |
| [Write your first DAG in Airflow 3 — Data with Marc](https://www.youtube.com/watch?v=dX6p-EwnkP4) | All (Airflow 3 syntax, same as this repo) | 20 min |
| [Airflow Tutorial for Beginners (2026) — Ansh Lamba](https://www.youtube.com/watch?v=IiczxlbQb8s) | Main course | 6 h 11 |
| [Airflow Tutorial — Full Course in 2 Hours — coder2j](https://www.youtube.com/watch?v=K9AnJ9_ZAXE) | Optional, clear but **Airflow 2**: imports differ | 2 h |

## 2. Read
- [Airflow: core concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html) · [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) · [DAG runs, catchup, backfill](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html)
- [Upgrading to Airflow 3](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html) — for translating Airflow 2 tutorials
- [Astronomer: DAG writing best practices](https://www.astronomer.io/docs/learn/dag-best-practices)

## 3. Syntax sheet
```python
from datetime import datetime, timedelta
from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

@dag(schedule="0 6 * * *", start_date=datetime(2026, 1, 1), catchup=False,
     max_active_runs=1,
     default_args={"retries": 2, "retry_delay": timedelta(minutes=2)})
def my_pipeline():
    extract = BashOperator(task_id="extract", bash_command="olist ingest")

    @task
    def check(**context):
        print("running for", context["logical_date"])

    extract >> check()

my_pipeline()
```
```bash
airflow dags list
airflow dags test my_pipeline 2026-01-05            # run once locally, no scheduler
airflow tasks test my_pipeline extract 2026-01-05   # one task
airflow backfill create --dag-id my_pipeline --from-date 2026-01-01 --to-date 2026-01-03   # Airflow 3
```

## 4. Practice
A toy DAG with 3 Python tasks passing a small value via return/XCom, one task that fails
randomly, `retries=3`. Watch the retries in the UI.

## 5. Apply to the project
1. `docker compose up -d airflow`; the admin password is in `docker compose logs airflow`.
   Open http://localhost:8080 and trigger `olist_daily`. Read every task log.
2. Write **your own** DAG `labs/11-airflow/my_olist_dag.py` (mount it by adding it to the
   DAGs folder or setting `AIRFLOW__CORE__DAGS_FOLDER`): ingest → fx → dbt build → serve,
   with retries and `max_active_runs=1`. Compare with `orchestration/dags/olist_daily.py`.
3. `on_failure_callback` that appends a line to `logs/alerts.log` (later: a Discord/Slack webhook).
4. A `quality_gate` task that queries `audit.quality_results` for the current run and fails on
   too many warnings. Hint: `@task` + `duckdb.connect(read_only=True)`.
5. Backfill 3 past dates and explain in your notes what `logical_date` meant for each run.

## 6. Self-check
- What is `logical_date` and why is it not "now"?
- A task failed at 03:00 — how do you find out, fix, and recover without duplicating data?
- Why `max_active_runs=1` here?

## Done when
- [ ] Your DAG runs green in Docker with callback and quality gate
- [ ] Backfill done and explained · **Gate 3** passed
