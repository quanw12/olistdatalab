# Airflow concepts and orchestration transfer

## Understand it

Transfer dependency/retry/interval reasoning rather than collecting orchestrators. Airflow DAGs define workflows, tasks execute steps and data intervals identify processing periods under a timetable. Airflow 3 TaskFlow uses its public SDK; old tutorials may have different imports and installation commands.

## Syntax and trace

~~~python
from datetime import datetime, timezone
from airflow.sdk import dag, task
@dag(schedule=None, start_date=datetime(2026,1,1,tzinfo=timezone.utc), catchup=False)
def transfer_demo():
    @task
    def count_rows():
        return 2
    @task
    def report(value):
        return {"count": value}
    report(count_rows())
transfer_demo()
~~~

This is dependency syntax only. schedule=None is manual; Python syntax validation is not scheduler evidence.

## Engineering connection

Explain tool equivalence while retaining Prefect in the main capstone.

[Reference](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

