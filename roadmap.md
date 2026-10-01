# 30-day Data Engineering roadmap

## How to use this workspace

Each day has its own folder named `day-NN`, such as `day-01`.

- Start with that day's `guide.md`; it gives the learning order.
- Write the code yourself instead of copying a complete answer.
- Keep notes, error screenshots, and results in the day's folder.
- Move on after completing the day's required output.

Each session is designed for 2.5–4 hours. Taking longer is fine; understanding the work and being able to run it again matter more.

## Goal after 30 days

Build a weather data pipeline: fetch API data, preserve raw data, clean it, load PostgreSQL, create analytics tables, check quality, and run it using Docker and basic orchestration. Include a README, tests, sample logs, and a short report for your portfolio.

## First-month stack

Python, SQL/PostgreSQL, Git/GitHub, terminal, CSV/JSON/Parquet, pytest, Docker Compose, Prefect, BigQuery Sandbox, and an LLM API for a small pipeline-support experiment.

Leave Kafka, Kubernetes, Terraform, multiple clouds, advanced Spark, vector databases, and RAG for later. Explore Spark concepts after the capstone.

## Daily schedule

| Day | Topic | Required output |
|---|---|---|
| 01 | Python, CSV files, basic Git | Weather CSV cleaning program |
| 02 | Python: functions, dict, list, set, exceptions | Small weather report and understanding/refactoring of Day 1 |
| 03 | Datetime, JSON, logging, configuration | JSON reading and structured logs |
| 04 | pandas: reading, filtering, types, missing values | Script that cleans whole columns |
| 05 | pandas: merge, groupby, result checks | City weather summary |
| 06 | CLI, environment variables, HTTP basics | CLI script that fetches current weather |
| 07 | Review and mini-project 1 | Organized repository, README, five quality checks |
| 08 | PostgreSQL through pgAdmin 4: tables, types, keys, constraints | Weather schema on local PostgreSQL |
| 09 | SQL: SELECT, WHERE, JOIN, GROUP BY | Ten queries with explanations |
| 10 | SQL: CTE, CASE, date/time, subqueries | Ten more advanced queries |
| 11 | SQL window functions | Rank, lag, and rolling-average analysis |
| 12 | Data modeling: grain, OLTP/OLAP, fact/dimension | ERD and star schema |
| 13 | PostgreSQL from Python: transactions, upsert | Safe staging-load script |
| 14 | Review and mini-project 2 | Weather analytics mart |
| 15 | REST APIs: timeout, status, JSON, retry | Open-Meteo extraction module |
| 16 | Raw/staging/mart, ETL and ELT | Three-layer data pipeline |
| 17 | Incremental loading, idempotency, backfill | Reruns without duplicate data |
| 18 | Docker: images, containers, volumes, networks | PostgreSQL container with persistent storage |
| 19 | Docker Compose for the application | Start the environment with one command |
| 20 | Prefect: flows, tasks, retry, logs | Orchestrated pipeline |
| 21 | Review and mini-project 3 | Locally scheduled pipeline |
| 22 | Testing: pytest, fixtures, mock API | Transformation and ingestion tests |
| 23 | Data quality: schema, null, uniqueness, range, freshness | Data quality checks |
| 24 | Data warehouses: columnar storage, partitioning, costs | BigQuery Sandbox lab |
| 25 | Analytics: KPIs, SQL mart, visualization | Three charts and observations supported by numbers |
| 26 | Basic CI with GitHub Actions | Tests run automatically on push |
| 27 | AI/LLM support for DE: docs, tests, verified summaries | Evaluated experiment |
| 28 | Capstone design and README | Architecture, data dictionary, runbook |
| 29 | Run capstone and handle failures | End-to-end pipeline demo |
| 30 | Finish the portfolio | README, demo video, retrospective |

For Days 08–17, use locally installed PostgreSQL, with pgAdmin 4 for SQL practice. Docker is not a prerequisite for these lessons. Start Day 8 with `day-08/guide.md`.

Day 18 introduces Docker step by step: why use it, image versus container, installing/starting Docker Desktop, understanding each command, host versus container ports, connecting pgAdmin, and using a volume to preserve data. Move to Docker Compose in Day 19. Consider the local server's existing port when choosing the container's host port.

## Completion criteria

A section is complete when you can:

1. Run it from the beginning without relying on hidden notebook state or a previous session.
2. Explain its inputs, outputs, possible errors, and how the program handles them.
3. Make a Git commit that accurately describes the change.

## Role of roadmap.sh

The [Data Engineer Roadmap](https://roadmap.sh/data-engineer) is a long-term reference covering Python, SQL, storage, pipelines, orchestration, warehouses, big data, and cloud. Use it to see what comes later, rather than as a checklist to finish in one month.
