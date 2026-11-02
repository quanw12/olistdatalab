# 06 · Orchestration with Apache Airflow

**Time:** week 8 · **Stack:** Airflow 3, Docker Compose

## Why
Pipelines run on schedules with dependencies, retries and history. Airflow is still the most
requested orchestrator; Dagster and Prefect use the same ideas.

## Learn
- DAG, task, operator, schedule, `logical_date`, catchup, backfill — [Airflow concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html)
- Retries, SLAs/alerts, `max_active_runs`, pools
- Why tasks must be idempotent; why heavy work should not run inside the scheduler

## Read in this repo
- `orchestration/dags/olist_daily.py`, `orchestration/Dockerfile`, the `airflow` service in `docker-compose.yml`.

## Build
1. `docker compose up -d airflow`, open http://localhost:8080 (the admin password is printed in
   the container logs). Trigger `olist_daily`. **Check:** all tasks green; screenshot for README.
2. Add an `on_failure_callback` that writes a line to `logs/alerts.log` (later: Slack/Discord webhook).
3. Make `ingest` take the run's date (`{{ ds }}`) and pass it to the CLI as a partition to load;
   then run a backfill for 3 past dates with `airflow dags backfill`.
4. Add a `data_quality_gate` task that queries `audit.quality_results` and fails on any warning
   above a threshold.
5. Optional: rewrite the DAG with the TaskFlow API (`@task`) and compare.

## Break it
- Kill the container during `dbt_build`. Restart, clear the task. Does the rerun produce the same tables?
- Set `max_active_runs=2` and trigger twice. What happens with DuckDB, and why the limit exists.

## Interview questions
- What is `logical_date`, and why is it not "now"?
- A task failed at 03:00. Walk me through how you find out, fix and recover.
- Catchup and backfill: when do you want them?

## Done when
- [ ] DAG runs green in Docker, failure callback and quality gate merged
- [ ] A backfill done and explained in your notes
