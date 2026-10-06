# Focused resources

Use the daily lesson first. Open one reference for your current problem; do not start several full courses at once. Software references were reviewed on 2026-10-06; releases and service limits can change.

| Days | Resource | Focus |
|---|---|---|
| 01–03 | [Python 3.13 tutorial](https://docs.python.org/3.13/tutorial/) | Functions, collections, modules, files, exceptions |
| 01–03 | [CSV](https://docs.python.org/3.13/library/csv.html), [JSON](https://docs.python.org/3.13/library/json.html), [datetime](https://docs.python.org/3.13/library/datetime.html) | Apply one syntax example to one weather row |
| All | [Pro Git](https://git-scm.com/book/en/v2) | Working tree, staging, commits, branches, remotes, stash |
| 04–05,25 | [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | Read/write, filter, merge, group |
| 06,15 | [Requests](https://requests.readthedocs.io/en/stable/user/quickstart/), [Open-Meteo](https://open-meteo.com/en/docs) | params, status, JSON, timeouts |
| 08–12 | [PostgreSQL 18 tutorial](https://www.postgresql.org/docs/18/tutorial.html) | Tables, joins, aggregates, transactions, windows |
| 08–10 | [SQLBolt](https://sqlbolt.com/) | Optional SELECT/JOIN/NULL/aggregate drills; dialect details differ |
| 12 | [Kimball fact-table grain](https://www.kimballgroup.com/2008/11/fact-tables/) | Define exactly what one row represents |
| 13–17 | [Psycopg 3](https://www.psycopg.org/psycopg3/docs/basic/usage.html) | Connections, parameters, transaction ownership |
| 16 | [zoneinfo](https://docs.python.org/3.13/library/zoneinfo.html) | Named zones and UTC conversion |
| 18–19 | [Docker introduction](https://docs.docker.com/get-started/), [PostgreSQL containers](https://docs.docker.com/guides/postgresql/) | Images, containers, volumes, networking |
| 20–21 | [Prefect 3](https://docs.prefect.io/v3/get-started), [serve API](https://reference.prefect.io/prefect/flows/#prefect.flows.Flow.serve) | Flows, tasks, server and local runner |
| 22 | [pytest how-to](https://docs.pytest.org/en/stable/how-to/index.html) | Fixtures, parameters, exceptions, monkeypatch |
| 23–24 | [EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html), [indexes](https://www.postgresql.org/docs/18/indexes.html) | Estimates versus actual work |
| 24 | [BigQuery sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox), [batch loading](https://docs.cloud.google.com/bigquery/docs/batch-loading-data) | Optional no-billing CSV upload and SELECT reports |
| 24 optional | [Spark SQL](https://spark.apache.org/docs/latest/sql-getting-started.html) | DataFrames and when distribution is useful; no install |
| 25 | [Matplotlib](https://matplotlib.org/stable/tutorials/pyplot.html) | Figures, labels, export |
| 26 | [GitHub Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) | Triggers, runners, dependencies, tests |

## Optional longer course afterward

[Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) offers a larger pipeline course with videos/exercises. Choose modules after you can explain this capstone; its broader stack is not an extra requirement this month.

[roadmap.sh](https://roadmap.sh/data-engineer) is a topic map, not a daily workload. Revisit it on Day 30 to mark what you have actually practised.

## Learning method

1. Name the gap precisely, such as LEFT JOIN with NULL.
2. Read one section and type a small example.
3. Close the reference and reproduce the syntax.
4. Apply it to today's exercise and test an edge case.
5. Explain the result in reflection.md.

When versions or UI labels differ, record the version and full error. Use current project documentation for facts and issue discussions for practical troubleshooting.
