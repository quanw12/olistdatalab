# Day 20 — Orchestration with Prefect flows and tasks


## Why orchestration exists

Your Python functions perform the work. An orchestrator coordinates runs, records task states, retries selected failures and shows logs. It does not make invalid data valid or replace transactions and idempotency.

We use Prefect 3 locally. Keep native PostgreSQL or the Compose database running. Run Prefect and the Python application from the host course environment; packaging a production orchestration server is beyond this month.

Install python -m pip install "prefect>=3,<4". Open two terminals, activate the same Python 3.13 environment in both. In terminalA run prefect server start; keep it open. In terminalB set:

~~~powershell
$env:PREFECT_API_URL = "http://127.0.0.1:4200/api"
~~~

Open http://127.0.0.1:4200 to inspect runs. The local UI is a view of run state, not proof the database has correct data.

## Decorator syntax

A decorator wraps a function to add behavior:

~~~python
from prefect import flow, task, get_run_logger

@task(retries=0)
def double_number(value):
    return value * 2

@flow(name="number-demo")
def number_demo():
    result = double_number(6)
    get_run_logger().info("result=%s", result)
    return result

if __name__ == "__main__":
    number_demo()
~~~

@flow marks the coordinated run; @task marks an observable unit. Return values carry data between direct calls. Start with sequential calls; task submission and parallelism are optional later.

## Choose task boundaries carefully

Wrap extract, transform, and database-load stages. Keep load_records, refresh_mart and checkpoint in ONE task using one transaction. Splitting those into independently successful tasks would break your atomic boundary.

Disable task caching for side-effecting pipeline stages in this introductory wrapper, for example using cache_policy=None, so an apparent retry/replay actually exercises the writes and their idempotency. Do not pass open database connections between tasks; create them inside the load task.

## One retry owner

Your extractor already makes at most three HTTP attempts. Keep Prefect retries=0 around that extractor; otherwise three task attempts times three HTTP attempts could cause nine requests. A teaching demo task may use retries=2 and retry_delay_seconds=1 to illustrate three total attempts. Do not apply that policy blindly to validation errors.

If your business function returns a failure object instead of raising, Prefect may mark the task completed. Convert real failure outcomes to raised errors; handle quarantine warnings explicitly.

Read: [Prefect flows](https://docs.prefect.io/v3/concepts/flows), [tasks](https://docs.prefect.io/v3/concepts/tasks), [flow API](https://reference.prefect.io/prefect/flows/).
