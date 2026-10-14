# Foundation lesson index

[Start Day 01](day-01/guide.md) · [References](../docs/lesson-references.md) · [Progress](progress.md)

Each row is one lesson. Budget 2.5–4 hours (more for mini-projects). Finish the core task before the next dependent day.

| Day | Lesson | Deliverable | Primary references |
|---|---|---|---|
| [01](day-01/guide.md) | Python and CSV cleaning | `clean.csv` + rejection counts | [Python tutorial](https://docs.python.org/3.13/tutorial/), [csv](https://docs.python.org/3.13/library/csv.html) |
| [02](day-02/guide.md) | Functions, lists, dicts, sets | Structured summary | [Data structures](https://docs.python.org/3.13/tutorial/datastructures.html) |
| [03](day-03/guide.md) | JSON, config, datetime | JSON snapshot | [json](https://docs.python.org/3.13/library/json.html), [datetime](https://docs.python.org/3.13/library/datetime.html) |
| [04](day-04/guide.md) | pandas cleaning | Validated DataFrame | [pandas intro](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) |
| [05](day-05/guide.md) | pandas join/aggregate | City summary | [merge](https://pandas.pydata.org/docs/user_guide/merging.html), [groupby](https://pandas.pydata.org/docs/user_guide/groupby.html) |
| [06](day-06/guide.md) | CLI and HTTP | Weather fetch CLI | [Requests](https://requests.readthedocs.io/en/stable/user/quickstart/), [argparse](https://docs.python.org/3.13/library/argparse.html) |
| [07](day-07/guide.md) | Mini-project 1 | Offline pipeline | [json](https://docs.python.org/3.13/library/json.html), [Pro Git](https://git-scm.com/book/en/v2) |
| [08](day-08/guide.md) | PostgreSQL DDL | Constrained tables | [PostgreSQL tutorial](https://www.postgresql.org/docs/18/tutorial.html) |
| [09](day-09/guide.md) | SQL joins/NULL | Ten queries | [SELECT](https://www.postgresql.org/docs/18/tutorial-select.html), [JOIN](https://www.postgresql.org/docs/18/tutorial-join.html) |
| [10](day-10/guide.md) | CTEs, CASE, dates | Ten reports | [datetime types](https://www.postgresql.org/docs/18/datatype-datetime.html) |
| [11](day-11/guide.md) | Window functions | Eight queries | [Window tutorial](https://www.postgresql.org/docs/18/tutorial-window.html) |
| [12](day-12/guide.md) | Dimensional model | Mart DDL + reports | [Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [Kimball grain](https://www.kimballgroup.com/2008/11/fact-tables/) |
| [13](day-13/guide.md) | Load from Python | Idempotent load | [Psycopg params](https://www.psycopg.org/psycopg3/docs/basic/params.html) |
| [14](day-14/guide.md) | Loader package + mart | Reusable package | [modules](https://docs.python.org/3.13/tutorial/modules.html) |
| [15](day-15/guide.md) | HTTP retries | Bounded retry proof | [Requests advanced](https://requests.readthedocs.io/en/stable/user/advanced/) |
| [16](day-16/guide.md) | ETL layers | raw/clean/reject + manifest | [pathlib](https://docs.python.org/3.13/library/pathlib.html), [zoneinfo](https://docs.python.org/3.13/library/zoneinfo.html) |
| [17](day-17/guide.md) | Incremental/backfill | Correction vs rebuild | [INSERT](https://www.postgresql.org/docs/18/sql-insert.html) |
| [18](day-18/guide.md) | Docker basics | Containerized Postgres | [Docker install](https://docs.docker.com/desktop/setup/install/windows-install/) |
| [19](day-19/guide.md) | Compose | Stack with persistence | [Compose file](https://docs.docker.com/reference/compose-file/services/) |
| [20](day-20/guide.md) | Prefect flows | Flow/task run | [Prefect flows](https://docs.prefect.io/v3/concepts/flows) |
| [21](day-21/guide.md) | Scheduled runs | Served deployment | [Prefect schedules](https://docs.prefect.io/v3/concepts/schedules) |
| [22](day-22/guide.md) | pytest | Meaningful tests | [pytest how-to](https://docs.pytest.org/en/stable/how-to/index.html) |
| [23](day-23/guide.md) | Data quality | Fixed-clock freshness | [aggregates](https://www.postgresql.org/docs/18/functions-aggregate.html) |
| [24](day-24/guide.md) | Warehouse concepts | EXPLAIN + optional BQ | [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [BQ sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox) |
| [25](day-25/guide.md) | Reporting | Honest charts | [matplotlib](https://matplotlib.org/stable/tutorials/pyplot.html) |
| [26](day-26/guide.md) | GitHub Actions | CI test job | [Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) |
| [27](day-27/guide.md) | Verified AI | Reject false claims | [json](https://docs.python.org/3.13/library/json.html) |
| [28](day-28/guide.md) | Architecture | Runbook + contracts | [capstone contract](capstone/contract.md) |
| [29](day-29/guide.md) | Rehearsal | Recovery evidence | Prior days' runbooks |
| [30](day-30/guide.md) | Portfolio | Demo + retrospective | [interviews](../docs/interviews.md) |

## Milestones

- **Day 07:** reproducible weather snapshot.
- **Day 14:** loader + SQL mart.
- **Day 21:** scheduled orchestration.
- **Day 30:** portfolio ready for Gate E/F practice.
