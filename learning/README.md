# Learning path: build this platform one technology at a time

The repo root is the portfolio. This folder is how you earn it. Every module teaches one part of a
modern data stack by **reading, rebuilding and extending** the matching part of the platform.

> Rule: you list a technology on your CV only after you ticked that module's *Done when*
> checklist and can explain its code without notes. Code you cannot explain is a liability in an
> interview, not an asset.

## How to study a module

1. **Learn** — read the concepts and the official docs linked (1–3 h).
2. **Read in this repo** — trace the code that uses the concept; run it; add `print`/breakpoints.
3. **Build** — do the exercises in a branch. Each has an acceptance check (test, query, number).
4. **Break it** — run the failure drills and write what happened in `docs/ai-log.md` or your notes.
5. **Explain** — answer the interview questions out loud in English, 2 minutes each.
6. Commit with a clear message, open a PR to yourself, let CI pass, merge.

## Plan (about 16 weeks at 15–20 h/week next to school)

| Weeks | Module | Stack you add | Builds / extends |
|---|---|---|---|
| 1 | [01 Setup, Git, CI](01-setup-git-ci.md) | Git, GitHub Actions, pytest, ruff, venv | CI pipeline, branch + PR workflow |
| 2–3 | [02 SQL and data modelling](02-sql-modeling.md) | SQL, DuckDB, star schema, window functions | Analytical queries on the marts |
| 3–4 | [03 Ingestion and data quality](03-ingestion-quality.md) | pandas, NumPy, Polars, Parquet, data contracts | `ingest.py`, `quality.py` |
| 5 | [04 APIs and reliability](04-apis-reliability.md) | requests, retries, idempotency | `fx.py`, a second API source |
| 6–7 | [05 dbt](05-dbt.md) | dbt, incremental models, tests, docs | `dbt/` models and tests |
| 8 | [06 Orchestration](06-orchestration-airflow.md) | Apache Airflow 3 | `olist_daily` DAG, backfills |
| 9 | [07 Docker, Postgres, BI](07-docker-postgres-bi.md) | Docker Compose, PostgreSQL, Metabase/Superset, Power BI | Serving layer + dashboard |
| 10–11 | [08 Spark and big data](08-spark.md) | PySpark, partitions, Hadoop/Hive concepts, Delta Lake | `spark/customer_rfm.py` |
| 11–12 | [09 Streaming with Kafka](09-kafka-streaming.md) | Kafka, consumer groups, offsets | `streaming.py` live feed |
| 13 | [10 Cloud and IaC](10-cloud-terraform.md) | GCP (GCS, BigQuery), Terraform; Snowflake/Databricks mapping | `infra/terraform/gcp` + load to BigQuery |
| 14 | [11 ML for data engineers](11-ml-for-de.md) | scikit-learn, MLflow, feature pipelines | `ml.py` |
| 15 | [12 LLM and AI engineering](12-llm-ai-engineering.md) | Ollama, Claude API, structured output, RAG, LangChain | `ai_enrich.py`, text-to-SQL |
| 16 | [13 Portfolio and interviews](13-portfolio-interviews.md) | — | Real-data numbers, demo, CV bullets |

Apply for internships from **week 8** (after module 06): ingestion, SQL, dbt and Airflow on real
data already match most intern postings. Modules 07–12 continue while you apply.

## Coverage map: where each skill appears

| Category | Technologies | Module |
|---|---|---|
| Languages | Python, SQL, Bash (CI, Docker), HCL (Terraform) | 01–10 |
| Databases | DuckDB, PostgreSQL, Redis (cache idea in 12), Oracle → compare in 02 | 02, 07 |
| Processing | pandas, NumPy, Polars, Spark; Hadoop/Hive concepts | 03, 08 |
| Streaming | Kafka | 09 |
| Orchestration / transformation | Airflow, dbt | 05, 06 |
| Warehouse / lakehouse | DuckDB, BigQuery, Snowflake, Databricks, Delta Lake | 02, 08, 10 |
| AI / ML | scikit-learn, MLflow, Ollama, Claude/OpenAI/Gemini APIs, Hugging Face, LangChain, FastAPI | 11, 12 |
| BI | Metabase, Superset, Power BI, Streamlit, Jupyter | 07 |
| Cloud / DevOps | GCP, Docker, Terraform, GitHub Actions, Linux, Git | 01, 07, 10 |

## Weekly rhythm

- 3 sessions of build (2–3 h), 1 session of SQL practice (1 h, any site with real interview
  questions), 1 session of review: re-explain last week's module without notes.
- Every Sunday: update `docs/data-contract.md` or `docs/ai-log.md` with one thing you learned.
- At school, map each course to a module (databases → 02, networks → 07/09, ML → 11).

## Your old course

The previous day-by-day course (weather pipeline, Python/Linux/DE lessons) is archived in git
history under the tag `archive/pre-refactor-2026-11-02` (local) and in the bundle file
`C:\Users\DELL\DE-Courses-history-2026-11-02.bundle`. To read an old lesson:
`git show archive/pre-refactor-2026-11-02:02-python/README.md`.
