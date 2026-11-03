---
tags: [decourse, roadmap]
---

# Roadmap

A product-focused route to becoming a data engineer: about **32 weeks at 12–15 hours per week** (≈ 384–480 hours) for the core plus one elective branch. Adjust the pace to the exit gates, not to the number of videos you have watched.

Everything you need to study lives in this vault: **module guides** (`Module NN - …`) tell you what to watch, read, practise and hand in; **theory notes** teach the concepts with runnable examples, pitfalls, exercises and review questions. The code repo (`src/`, `dbt/`, `labs/`, …) is a separate thing: it holds the reference implementation and your lab code. Compare with the reference only after your own attempt — it is not evidence that you finished the course.

## How to study (and how to use AI)

1. **Diagnose first.** If you can already do and explain an exercise, skip the matching videos.
2. **Weekly mix:** ~20% reading/watching, 55% building/debugging, 15% verifying, 10% review and notes. Long videos are a reference library, not homework to finish in one week.
3. **Before asking AI:** write down expected vs. actual and a minimal reproducible example. Ask for explanations and counter-examples; check generated code with data or an independent test. See [[Learning with AI]].
4. **Rebuild from an empty file** once per module without AI. This is a memory check, not a ban on AI for product work.
5. **Review after 1, 7 and 30 days:** answer the questions, change the example data, log weak spots. See [[Review Schedule]].

Put a tool on your CV only when you have real runs and can explain the decisions, failures and recovery. The Basic/Advanced labels inside modules describe topics, not professional levels.

## Main route

| Weeks | Module guide | Theory notes | Output |
|---|---|---|---|
| 1–3 | [[Module 01 - Python]], [[Module 02 - Git and Linux]] | [[Python Basics and Collections]], [[Functions and Error Handling]], [[Files CSV JSON and Parquet]], [[Datetime Decimal and Timezones]], [[Python Environments and Packaging]], [[Git Branches PRs and Review]], [[Shell Linux and PowerShell]] | CLI that reads CSV, handles errors, a PR |
| 4–6 | [[Module 03 - SQL]] | [[SELECT NULL and CASE]], [[JOIN Grain and Fan-out]], [[Aggregation and Window Functions]], [[CTE Dedup and Incremental SQL]], [[Transactions Indexes and EXPLAIN]] | 8 queries, fan-out proof, window functions |
| 7–8 | [[Module 04 - DataFrames]] | [[DataFrames pandas and Polars]] | Profile + Parquet; pandas + SQL core, Polars optional — **G1** |
| 9 | [[Module 05 - Data Modeling]] | [[Data Modeling and SCD2]] | Grain, ERD, metric definitions, SCD2 |
| 10–11 | [[Module 06 - Ingestion and Quality]] | [[Ingestion Contracts and Idempotency]] | Contract, A→B→A snapshot, Parquet recovery |
| 12 | [[Module 07 - APIs]] | [[API Retry Pagination and Replay]] | Pagination, retry, raw replay, checkpoint |
| 13–14 | [[Module 08 - Testing and CI]] | [[Testing Logging and CI]] | Your labs in CI, bad-data tests — **G2** |
| 15–16 | [[Module 09 - dbt]] | [[dbt Models Tests and Incremental]] | **Real Olist**, marts, money reconciliation |
| 17–18 | [[Module 10 - Docker Postgres and BI]] | [[Docker PostgreSQL and Serving]], [[BI Metrics and Data Products]] | One dashboard, query plan, transaction, reader role |
| 19–20 | [[Module 11 - Airflow]] | [[Airflow Intervals and Backfill]] | Quality gate, correct-interval backfill — **G3** |
| 21 | [[Module 19 - Incremental and CDC]] | [[Incremental CDC and Backfill]] | 30-day late update, delete, SCD2, replay |
| 22 | [[Module 20 - Observability and Recovery]] | [[Observability and Recovery]], [[Failure Drills]] | Freshness alert, drills, measured recovery time |
| 23 | [[Module 21 - Security and Delivery]] | [[Security and Governance]], [[Delivery and Reproducibility]], [[Performance and Storage]] | Dev/prod, permissions, version manifest, rollback — **G4** |
| 24–25 | [[Module 14 - Cloud and Terraform]] | [[GCP BigQuery Terraform and Cost]] | One cloud, one BigQuery mart, permissions and cost |
| 26–28 | One branch below | See branch | An extension with quality/performance measurements |
| 29–31 | [[Module 22 - Independent Project]], [[Module 17 - Capstone]] | [[Second Project]], [[Olist Product Brief]] | Second project, review, demo, evidence — **G5** |
| 32 | [[Module 18 - Portfolio and Interviews]] | [[Interviews and Portfolio]] | Honest CV, mock interview, recovery demo |

32 weeks is the budget for **core + one branch**. If a gate is not passed, extend that part and cut electives; do not force every technology into the same budget.

## Elective branches

- **Scale/Streaming:** [[Module 12 - Spark]] ([[Spark Partitions Shuffle and Skew]]) and [[Module 13 - Kafka]] ([[Kafka Offsets Replay and Ordering]]). Pick one main extension: Spark needs a shuffle/skew experiment, Kafka needs a crash/replay test with a real broker.
- **Data for AI:** [[Module 15 - ML]] ([[ML Features and Point-in-Time]]) for point-in-time/leakage, and [[Module 16 - LLM]] ([[LLM Caching Evaluation and Guardrails]], [[RAG Retrieval and Evaluation]]). Pick scoring or labelling as the main extension; RAG/text-to-SQL come after the core.

One BI tool and one cloud are enough for the first round. Add tools to match the roles you are targeting.

**Mandatory core:** Python, SQL, Git/shell, modelling, ingestion/API, tests, dbt, Docker/Postgres, one BI tool, Airflow, incremental loads, observability/recovery, security, one cloud, two projects. **Optional:** deep Polars, several BI tools/clouds, deep Spark and Kafka, ML model tuning, RAG/text-to-SQL. Learning many tools does not by itself make anyone senior.

## Mandatory gates

| Gate | Condition | Evidence |
|---|---|---|
| G1 | CSV→Parquet, joins/windows from an empty file; NULLs and grain | Script, SQL, results, your own explanation |
| G2 | Your own ingestion/API code; duplicates/drift/retry | CI runs **your** labs, not just reference code |
| G3 | Real Olist batch, reconciliation, dashboard, backfill | Counts, proof SQL, run log, screenshot |
| G4 | Late updates/deletes, green-but-stale job, recovery, permissions | Incident report, recovery time, permission tests |
| G5 | Independent project, changed requirement, someone else reproduces it | Brief, ADR, review, demo, README |

After G2 you can start applying for internships to get feedback. Gates do not guarantee a job.

## Diagnostic test (60–90 minutes, no AI)

Read a CSV, detect duplicate keys, pre-aggregate before a JOIN, write a running total and one test for bad data. If this goes well, watch videos only where you are weak instead of the full playlists. Still take each gate independently after every phase.

## Threads that run through the course

- Module 04: you can already profile real Olist data; fake data is for fast tests.
- Module 09: run the real batch and fill in `docs/data-contract.md` — do not wait until week 30.
- Module 11: accept the local batch and a correct-interval backfill.
- Module 20: drills on a copy and recovery from raw.
- Module 17: collect evidence for **core + the branch you chose**; you do not need every branch.

Never run `olist sample` into the real Olist folder: the command overwrites it with sample data. Use separate `OLIST_DATA_DIR` and `DUCKDB_PATH` values for sample, real and drill runs.

## From lessons to product

[[Olist Product Brief]] defines users and metrics. [[Failure Drills]] tests the system when it breaks. [[Second Project]] tests whether you can do it again with different requirements. Use [[Progress and Evidence]] to separate *read*, *ran* and *did independently*.

## Sources and references

- [Python tutorial](https://docs.python.org/3/tutorial/), [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html): foundations.
- [DE Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp): a second explanation, homework and peer review; tools change between cohorts.
- [Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html): reproducible tasks, explicit partitions.
- [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models): watermarks and adapter strategies.
- [BigQuery cost best practices](https://docs.cloud.google.com/bigquery/docs/best-practices-costs): dry runs and bytes billed; a budget alert is not a hard cap.

Videos in the modules are optional. Record the versions of Python, dbt/adapter and services when you use a snippet.

## Weekly rhythm

Three build/debug sessions, one SQL session, one review-and-explain session. Save one understood bug or one justified decision every week. Every two weeks, ask a friend to review a PR, or self-review it after 48 hours.
