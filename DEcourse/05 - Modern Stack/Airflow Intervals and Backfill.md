---
tags: [decourse, airflow, orchestration]
module: 11
---

# Airflow: Intervals and Backfill

> [!info] Learning goals
> After this note you can: explain what an orchestrator does; define DAGs, tasks, operators and dependencies; understand schedules, data intervals and logical dates; reason about catchup and backfill; pass the interval into your processing code so every run is reproducible; use retries, timeouts, callbacks and quality gates; and avoid the classic Airflow anti-patterns.

## 1. What an orchestrator does

A pipeline is several steps with dependencies: ingest → dbt build → tests → export → notify. An orchestrator:

- **schedules** runs (every day at 06:00 UTC);
- runs tasks in **dependency order**, in parallel where possible;
- **retries** failed tasks and records history (what ran, when, how long, logs);
- lets you **backfill** past periods and rerun failed parts;
- alerts on failures.

It should not do the heavy data processing itself — that belongs in the warehouse, dbt, Spark or a container. Airflow coordinates; workers call out to the real engines.

## 2. Core concepts

| Concept | Meaning |
|---|---|
| DAG | Directed acyclic graph of tasks; a Python file defines it |
| Task | One unit of work (an operator instance) |
| Operator | Template for a task: `BashOperator`, `PythonOperator`/`@task`, provider operators (Postgres, BigQuery, Docker…) |
| DAG run | One execution of the DAG for one data interval |
| Task instance | One task in one DAG run, with state: queued, running, success, failed, up_for_retry, skipped |
| Scheduler | Creates DAG runs and queues tasks |
| Executor / workers | Actually run the tasks |
| XCom | Small metadata passed between tasks (a path, a count) — not DataFrames |

## 3. Data intervals: the most important idea

A DAG run processes a **data interval** `[data_interval_start, data_interval_end)`. A daily schedule creates a run for 2026-01-01 00:00 → 2026-01-02 00:00, which starts **after** the interval ends (the data must exist first). The *logical date* is the interval start for interval-based schedules.

| Value | Example for the 1 Jan daily run |
|---|---|
| `data_interval_start` | 2026-01-01T00:00:00+00:00 |
| `data_interval_end` | 2026-01-02T00:00:00+00:00 |
| Actual start time | 2026-01-02T06:00 (or days later during a backfill) |

So code must use the **interval**, never `now()` or "latest". A task that reads "the latest data" produces different results when rerun or backfilled; a task that processes exactly `[start, end)` from a pinned input produces the same result every time.

```python
# runnable
from datetime import datetime, timedelta, timezone

def partitions_for(start: datetime, end: datetime) -> list[str]:
    """Daily partitions inside the half-open interval [start, end)."""
    if start.tzinfo is None or end.tzinfo is None:
        raise ValueError("intervals must be timezone-aware")
    days, current = [], start
    while current < end:
        days.append(current.date().isoformat())
        current += timedelta(days=1)
    return days

start = datetime(2026, 1, 1, tzinfo=timezone.utc)
end = datetime(2026, 1, 4, tzinfo=timezone.utc)
assert partitions_for(start, end) == ["2026-01-01", "2026-01-02", "2026-01-03"]
assert partitions_for(start, start) == []
```

A 3-day backfill must produce exactly 3 partitions, and rerunning the same interval must give the same result.

## 4. A DAG that passes the interval

```python
# Pattern (Airflow 3): the lab CLI below is one you write yourself, not an existing olist command.
from datetime import datetime, timezone
from airflow.sdk import dag
from airflow.providers.standard.operators.bash import BashOperator

@dag(schedule='0 6 * * *', start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
     catchup=False, max_active_runs=1)
def lab_partition_pipeline():
    BashOperator(
        task_id='build_partition',
        bash_command='python labs/11-airflow/partition_job.py '
                     '--start "{{ data_interval_start }}" '
                     '--end "{{ data_interval_end }}"',
    )

lab_partition_pipeline()
```

- `{{ data_interval_start }}` is a Jinja template filled in per run.
- Your CLI parses timezone-aware ISO datetimes and processes `[start, end)`. Never insert user-provided text into a Bash command.
- The schedule `0 6 * * *` is cron syntax (minute hour day month weekday). With a UTC `start_date`, 06:00 UTC is 13:00 in Vietnam — be explicit about timezones.
- `max_active_runs=1` prevents two runs writing at once to a single local writer; it is not a general concurrency solution.

TaskFlow style (Python tasks):

```python
from airflow.sdk import dag, task

@dag(schedule="@daily", start_date=datetime(2026, 1, 1, tzinfo=timezone.utc), catchup=False)
def olist_like():
    @task
    def ingest(data_interval_start=None, data_interval_end=None) -> str:
        return run_ingest(data_interval_start, data_interval_end)   # returns a path (small XCom)

    @task
    def quality_gate(path: str) -> None:
        if count_rows(path) == 0:
            raise ValueError(f"empty partition {path}")             # fail the run loudly

    quality_gate(ingest())
```

## 5. Catchup and backfill

- **catchup=True:** when a DAG is enabled with a `start_date` in the past, Airflow creates a run for every missed interval. Useful for history, dangerous by surprise (hundreds of runs at once).
- **Backfill:** explicitly run a range of past intervals, e.g. after a bug fix (`airflow backfill create --dag-id … --from-date … --to-date …` in Airflow 3; check your version's CLI).
- **Clear / rerun:** clearing a task instance reruns it for the same interval.

A backfill is only meaningful if the tasks are interval-aware and idempotent. Rerunning a DAG that reads "latest" does not recreate history ([[Incremental CDC and Backfill]]).

## 6. Task design checklist

- **Deterministic input:** path, version and interval fixed per run; a retry does not pick up a different source file.
- **Idempotent output:** overwrite the partition; a clear publish status.
- **Small XComs:** pass paths and counts, not data.
- **No heavy work at parse time:** the scheduler imports DAG files constantly; no API calls or data reads at module level.
- **Bounded retries and timeouts:** `retries=2`, `retry_delay`, `execution_timeout`. Remember nested retries multiply ([[API Retry Pagination and Replay]]).
- **Failure callbacks** that name dataset, run, interval and runbook link.
- **Quality gates** as tasks: fail the run when data is missing or wrong, so "green" means "data is good", not just "code exited 0".
- **Sensors / data-aware scheduling** (assets/datasets) to wait for upstream data instead of guessing times.

## 7. What the reference repo has

The reference DAG `olist_daily` reruns a local snapshot; it has no partition CLI like the example above. Use it to learn dependencies; your own lab must add interval handling before you claim a backfill works.

## 8. Applying it to Olist

Module 11 mandatory exercise: write `partition_job.py` taking `--start/--end` and a pinned input version, wire it into a DAG with `data_interval_start/end`, backfill 3 days and prove: exactly 3 partitions, each containing only its day; rerunning an interval yields the same hash/counts/money; a failure after the write but before task success is handled by the retry.

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Using `now()` / "latest" in tasks | Backfills and reruns produce wrong data | Use the data interval |
| Heavy code at DAG parse time | Slow scheduler, surprise API calls | Move into tasks |
| Large data in XCom | Metadata DB bloat, failures | Pass paths |
| `catchup=True` by accident | Hundreds of runs | Default `catchup=False`; backfill deliberately |
| Green DAG without data checks | Missing partitions unnoticed | Quality-gate tasks and freshness checks |
| Naive datetimes / unclear timezone | Off-by-one-day partitions | Aware datetimes, explicit UTC |

## 10. Exercises

1. Create input for three days with a fixed version; backfill three intervals and check each output contains only its day.
2. Rerun the same interval and compare hash, counts and money.
3. Inject a failure after the write but before the task succeeds; verify the retry produces a correct, non-duplicated partition.
4. Add a quality gate that fails when a partition is empty and an `on_failure_callback` that logs dataset, interval and runbook.

## 11. Review questions

> [!question]- How does the logical date differ from "now"?
> The logical date/data interval identifies which period of data a run processes; "now" is when it happens to execute, which differs during backfills, retries and delays.

> [!question]- When does catchup create many runs?
> When a DAG with `catchup=True` is enabled or resumed with a `start_date` (or pause) far in the past: one run per missed interval.

> [!question]- How can a job be green while a partition is missing?
> If tasks only check that code exited 0. Without a data quality gate or freshness check on expected partitions, missing data is invisible.

> [!question]- Why must XComs stay small?
> They are stored in Airflow's metadata database; large payloads slow or break it. Pass references (paths, ids) instead.

Related: [[Incremental CDC and Backfill]], [[Observability and Recovery]], [[Module 11 - Airflow]]. Sources: [Airflow DAG runs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html), [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), [Airflow templates reference](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html).
