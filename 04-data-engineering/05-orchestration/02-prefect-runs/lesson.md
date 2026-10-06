# Prefect runs, retry ownership and backfill rehearsal

## Understand it

Wrap working functions with Prefect rather than duplicating logic. Task and inner HTTP retries can multiply attempts; assign one owner. Use explicit fixed intervals for reproducible backfills. A schedule needs a running execution mechanism; this lab first runs manually against fixtures.

## Syntax and trace

~~~python
from prefect import flow, task
@task(retries=1, retry_delay_seconds=1, cache_policy=None)
def toy(value):
    if value < 0:
        raise ConnectionError("deliberate toy failure")
    return value
@flow
def manual_demo(value=1):
    return toy(value)
if __name__ == "__main__":
    manual_demo()
~~~

Positive succeeds. Negative remains negative on retry and fails again; a retry is not a repair.

## Engineering connection

Match orchestration state to the loader's durable data evidence.

[Reference](https://docs.prefect.io/v3/how-to-guides/workflows/retries). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

