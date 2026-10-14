# Lesson references

[Home](../README.md) · [Study method](study.md) · [Focused resources](resources.md)

Open the **lesson** first, implement, then use **one** official link for the syntax you need. Links below match `lesson.md` in each folder; this page is the full index.

## Foundation (Days 01–30)

| Day | Open when stuck on… | Reference |
|---|---|---|
| 01 | `csv`, loops, dict rows | [Python tutorial](https://docs.python.org/3.13/tutorial/), [csv](https://docs.python.org/3.13/library/csv.html) |
| 02 | functions, collections | [tutorial datastructures](https://docs.python.org/3.13/tutorial/datastructures.html) |
| 03 | JSON, time parsing | [json](https://docs.python.org/3.13/library/json.html), [datetime](https://docs.python.org/3.13/library/datetime.html) |
| 04–05 | pandas IO, merge, groupby | [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) |
| 06 | HTTP, CLI | [Requests quickstart](https://requests.readthedocs.io/en/stable/user/quickstart/), [Open-Meteo](https://open-meteo.com/en/docs) |
| 07 | modules, Git | [modules](https://docs.python.org/3.13/tutorial/modules.html), [Pro Git](https://git-scm.com/book/en/v2) |
| 08–11 | SQL DDL, joins, windows | [PostgreSQL 18 tutorial](https://www.postgresql.org/docs/18/tutorial.html) |
| 12 | grain, constraints | [DDL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [fact grain](https://www.kimballgroup.com/2008/11/fact-tables/) |
| 13–17 | Psycopg, transactions, ETL | [Psycopg usage](https://www.psycopg.org/psycopg3/docs/basic/usage.html), [INSERT](https://www.postgresql.org/docs/18/sql-insert.html) |
| 18–19 | Docker, Compose | [Docker get started](https://docs.docker.com/get-started/), [Compose services](https://docs.docker.com/reference/compose-file/services/) |
| 20–21 | Prefect | [Flows](https://docs.prefect.io/v3/concepts/flows), [Tasks](https://docs.prefect.io/v3/concepts/tasks), [Schedules](https://docs.prefect.io/v3/concepts/schedules) |
| 22 | pytest | [pytest how-to](https://docs.pytest.org/en/stable/how-to/index.html) |
| 23–24 | quality, EXPLAIN, optional cloud | [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox) |
| 25 | charts | [matplotlib pyplot](https://matplotlib.org/stable/tutorials/pyplot.html) |
| 26 | CI | [GitHub Actions Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) |
| 27 | structured verification | [json](https://docs.python.org/3.13/library/json.html) |
| 28–30 | architecture, portfolio | [capstone contract](../01-foundation/capstone/contract.md), [assessment](assessment.md) |

Day-level detail also appears in [01-foundation/lessons.md](../01-foundation/lessons.md) and [01-foundation/resources.md](../01-foundation/resources.md).

## Python course (56 units)

Chapters 1–8: [Bro Code video](https://www.youtube.com/watch?v=Rq5gJVxz55Q) timestamps in each `lesson.md` plus [Python 3.13 docs](https://docs.python.org/3.13/).

Chapters 9–14: each `02-python/**/lesson.md` ends with a **Reference** line. Chapter index: [02-python/README.md](../02-python/README.md).

## Linux (LE01–LE22)

Each lesson links one primary manual page (GNU Bash, coreutils, Docker, Git, GitHub Actions). Index: [03-linux/README.md](../03-linux/README.md).

## Data Engineering (DE01–DE29)

| Lesson | Topic | Reference |
|---|---|---|
| DE01 | OLTP vs OLAP | [IBM OLAP/OLTP](https://www.ibm.com/think/topics/olap-vs-oltp) |
| DE02 | task breakdown | [study method](study.md) (no extra API) |
| DE03 | pdb, profiling | [pdb](https://docs.python.org/3.13/library/pdb.html), [profile](https://docs.python.org/3.13/library/profile.html) |
| DE04 | contracts | [JSON Schema concepts](https://json-schema.org/understanding-json-schema) (optional read) |
| DE05 | grain, SCD | [PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html) |
| DE06 | transactions | [PostgreSQL INSERT](https://www.postgresql.org/docs/18/sql-insert.html), [transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html) |
| DE07 | plans | [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [indexes](https://www.postgresql.org/docs/18/indexes.html) |
| DE08 | corrections/tombstones | [Python dataclasses](https://docs.python.org/3.13/library/dataclasses.html) (typed records in exercise) |
| DE09 | cursors/windows | [datetime timezone](https://docs.python.org/3.13/library/datetime.html#datetime.timezone) |
| DE10 | reconciliation | [pytest](https://docs.pytest.org/en/stable/) (patterns from Ch 11) |
| DE11 | observability | [logging](https://docs.python.org/3.13/library/logging.html) |
| DE12 | DuckDB layers | [DuckDB Python](https://duckdb.org/docs/stable/clients/python/overview) |
| DE13 | dbt models | [dbt models](https://docs.getdbt.com/docs/build/models) |
| DE14 | dbt tests | [data tests](https://docs.getdbt.com/docs/build/data-tests) |
| DE15 | incremental | [incremental models](https://docs.getdbt.com/docs/build/incremental-models), [dbt-duckdb](https://github.com/duckdb/dbt-duckdb) |
| DE16 | DAG ordering | [graph basics](https://docs.python.org/3.13/library/graphlib.html) |
| DE17 | Prefect retries | [Prefect retries](https://docs.prefect.io/v3/how-to-guides/workflows/retries) |
| DE18 | Airflow (optional) | [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html) |
| DE19 | cloud cost | [BigQuery cost practices](https://docs.cloud.google.com/bigquery/docs/best-practices-costs) |
| DE20 | BigQuery (optional) | [sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox) |
| DE21 | Spark (optional) | [PySpark getting started](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) |
| DE22 | secrets, privacy | [OWASP secrets](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) |
| DE23–DE26 | metrics, capstone, assignment | Lesson contracts + [assessment](assessment.md) |
| DE27 | profiling | [csv](https://docs.python.org/3.13/library/csv.html), [datetime](https://docs.python.org/3.13/library/datetime.html) |
| DE28 | backup/restore | [pg_dump](https://www.postgresql.org/docs/18/app-pgdump.html), [pg_restore](https://www.postgresql.org/docs/18/app-pgrestore.html) |
| DE29 | applications | [interviews](interviews.md) |

## Part 5 extensions

| Track | References |
|---|---|
| Labs LAB01–08 | [PostgreSQL](https://www.postgresql.org/docs/18/), [Requests](https://requests.readthedocs.io/), prior DE lessons |
| Cloud CL01–CL08 | [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs), [GCS upload](https://docs.cloud.google.com/storage/docs/uploading-objects), [BigQuery load](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-json) |
| AI Data AI01–AI08 | [SQLite FTS5](https://www.sqlite.org/fts5.html), local lesson contracts |
| Streaming ST01–ST08 | [Kafka quickstart](https://kafka.apache.org/39/getting-started/quickstart/), [Debezium PostgreSQL](https://debezium.io/documentation/reference/3.3/connectors/postgresql.html) |

Full extension source notes: [05-extensions/sources.md](../05-extensions/sources.md).
