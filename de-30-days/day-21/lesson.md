# Day 21 — Mini-project 3: schedule and observe repeated runs


## Scheduling is a separate process

A flow can run once from Python. A deployment gives it a reusable execution configuration. A schedule requests runs at chosen times. A runner must be alive to execute those requests. Your laptop is not an always-on production platform.

For this lab use flow.serve, which keeps a local runner alive. After creating your weather_flow on Day 20, create serve.py. Syntax on a small example:

~~~python
from prefect import flow

@flow
def heartbeat_example():
    print("One scheduled demonstration")

if __name__ == "__main__":
    heartbeat_example.serve(
        name="local-demo",
        interval=300,
        limit=1,
    )
~~~

interval is seconds. limit=1 limits concurrency in this runner; it is not a universal database lock across unrelated processes. Keep only one course runner active. Read [the serve API](https://reference.prefect.io/prefect/flows/#prefect.flows.Flow.serve).

## Two terminals, two roles

TerminalA runs prefect server start. TerminalB has the same environment, correct PREFECT_API_URL, PG variables and capstone working directory, then runs python serve.py. Keep both running during the exercise.

Register weather-lab with fixture parameters and a five-minute interval. Use fixed absolute paths or deliberately resolve relative paths from the file location so scheduling does not depend on an accidental terminal directory. Do not use live requests every few seconds.

## Monitor outcomes, not just green icons

Record run ID, scheduled/start/end times, duration, input/accepted/rejected counts, final stored count and error summary. A task can finish while producing no useful data; counts and data checks are separate evidence.

Watch at least two scheduled runs plus one manual trigger from the UI. Then stop the runner with Ctrl+C, observe that local work stops, and restart it. serve normally pauses its schedule on shutdown; verify the UI state when restarting. Do not assume missed runs magically backfill all missing observations.

Cron schedules express calendar times; timezone must be explicit, and DST can matter. This month uses an interval to avoid that extra complexity. Historical backfill remains an explicit replay command.

## Mini-project boundary

You now have acquisition, validation, files, database/mart loading, idempotency, containers and orchestration. This mini-project integrates them; it does not require installing another scheduler.

Read: [Prefect deployments](https://docs.prefect.io/v3/concepts/deployments), [schedules](https://docs.prefect.io/v3/concepts/schedules).
