# Learning roadmap: from zero to a data platform

The repo root is a finished **reference platform**. This folder is the road to building it yourself,
step by step: **basics → core data engineering → modern stack → scale → ML/AI → integration**.

> Rules
> 1. Never open the reference code (`src/`, `dbt/`, ...) for a task before you have a working
>    attempt of your own. Compare **after**, and write down what differs and why.
> 2. A technology goes on your CV only after its module's *Done when* checklist is ticked and
>    you can explain your code without notes.
> 3. Go in order. Each phase uses everything before it.

## How to study one module (the loop)

| Step | What | Time share |
|---|---|---|
| 1. Watch | The videos listed, at 1.25×, pausing to type every example yourself | 30% |
| 2. Read | The official docs pages linked; they are the truth when a video is outdated | 10% |
| 3. Syntax | The module's syntax sheet: retype each snippet, change it, break it | 10% |
| 4. Practice | Small drills, unrelated to the project, until the syntax is automatic | 15% |
| 5. Apply | Project tasks with hints, in `labs/` or a branch of this repo | 30% |
| 6. Check | Self-check questions out loud in English; tick *Done when* | 5% |

Stuck for more than 30 minutes? Read the hint again → official docs → search the exact error →
ask an AI to **explain** (not to write) → only then look at the reference code. Log what you
learned in [`docs/ai-log.md`](../docs/ai-log.md).

## The roadmap (≈32 weeks at 12–15 h/week next to school)

### Phase 1 · Foundations (Basic) — weeks 1–8
| # | Module | Weeks | Main video |
|---|---|---|---|
| 01 | [Python from zero](phase-1-foundations/01-python.md) | 1–3 | Data with Baraa — Python Full Course (13 h) |
| 02 | [Git, terminal and Linux](phase-1-foundations/02-git-linux.md) | 3 | freeCodeCamp Git crash course, Missing Semester |
| 03 | [SQL from zero](phase-1-foundations/03-sql.md) | 4–6 | Data with Baraa — SQL Full Course (30 h) |
| 04 | [pandas, NumPy, Polars](phase-1-foundations/04-dataframes.md) | 7–8 | Corey Schafer pandas, Bro Code NumPy, Baraa DataFrames |

**Gate 1:** write a Python script that reads a CSV, cleans it, writes Parquet, plus SQL with joins
and window functions on it — from a blank file, no AI.

### Phase 2 · Core data engineering (Intermediate) — weeks 9–14
| # | Module | Weeks | Main video |
|---|---|---|---|
| 05 | [Data modelling](phase-2-core/05-data-modeling.md) | 9 | Baraa — SQL Data Warehouse project |
| 06 | [Ingestion and data quality](phase-2-core/06-ingestion-quality.md) | 10–11 | Medallion, data contracts, idempotency |
| 07 | [APIs and reliability](phase-2-core/07-apis.md) | 12 | Corey Schafer requests, Caleb Curry REST |
| 08 | [Testing, logging and CI](phase-2-core/08-testing-ci.md) | 13–14 | freeCodeCamp pytest, GitHub Actions course |

**Gate 2:** your own `labs/` ingest + API extractor, tested, green in CI. Start applying for
internships with Phases 1–2 on your CV.

### Phase 3 · Modern data stack (Intermediate → Advanced) — weeks 15–20
| # | Module | Weeks | Main video |
|---|---|---|---|
| 09 | [dbt](phase-3-modern-stack/09-dbt.md) | 15–16 | Data Tech dbt crash course, Luke Barousse dbt course |
| 10 | [Docker, PostgreSQL and BI](phase-3-modern-stack/10-docker-postgres-bi.md) | 17–18 | TechWorld with Nana Docker, Luke Barousse Power BI |
| 11 | [Airflow](phase-3-modern-stack/11-airflow.md) | 19–20 | Data with Marc (Airflow 3), Ansh Lamba full course |

**Gate 3:** the batch pipeline runs on a schedule in Docker, dbt tests green, a dashboard on top.

### Phase 4 · Scale (Advanced) — weeks 21–26
| # | Module | Weeks | Main video |
|---|---|---|---|
| 12 | [Spark](phase-4-scale/12-spark.md) | 21–22 | Baraa "What is Spark?", Ansh Lamba PySpark |
| 13 | [Kafka streaming](phase-4-scale/13-kafka.md) | 23–24 | TechWorld with Nana Kafka |
| 14 | [Cloud and Terraform](phase-4-scale/14-cloud-terraform.md) | 25–26 | DevOps Directive Terraform, DE Zoomcamp |

### Phase 5 · ML and AI for data engineers (Advanced) — weeks 27–29
| # | Module | Weeks | Main video |
|---|---|---|---|
| 15 | [Machine learning](phase-5-ml-ai/15-ml.md) | 27 | StatQuest, freeCodeCamp scikit-learn, codebasics MLflow |
| 16 | [LLM engineering](phase-5-ml-ai/16-llm.md) | 28–29 | Karpathy intro to LLMs, Ollama, RAG from scratch |

### Phase 6 · Integration — weeks 30–32
| # | Module | Weeks |
|---|---|---|
| 17 | [Capstone: everything on real data](phase-6-integration/17-capstone.md) | 30–31 |
| 18 | [Portfolio and interviews](phase-6-integration/18-portfolio-interviews.md) | 32 |

Faster if you study more hours: the order matters, the weeks do not.

## Long courses to keep open in parallel

| Course | Use it for |
|---|---|
| [Data with Baraa — channel](https://www.youtube.com/@DataWithBaraa) | Python, SQL, data warehouse, Spark/Databricks explained visually |
| [Data with Baraa — "How I'd learn Data Engineering in 2026"](https://www.youtube.com/watch?v=1nVGaNbvuXg) | Watch once now, again at Phase 4 |
| [DataTalksClub Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | Free cohort course: Docker, Terraform, GCP, orchestration, dbt, Spark, Kafka. Use as a second explanation for Phases 3–4 |
| [Luke Barousse — Data Engineer Bootcamp (27 h)](https://www.youtube.com/watch?v=ol9_NnC9-cc) | Alternative path through SQL, Python, cloud, Bash |
| [Missing Semester (MIT)](https://missing.csail.mit.edu/) | Shell, Git, editor, debugging — the tools nobody teaches |

## Weekly rhythm

- 3 build sessions (2–3 h), 1 SQL practice session (1 h: [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) or [DataLemur](https://datalemur.com/questions)), 1 review session (re-explain last week without notes).
- Sunday: one entry in `docs/ai-log.md` or `docs/data-contract.md`.
- Map school courses to modules (databases → 03/05, OS/networks → 02/10/13, ML → 15).

## Your old course

The previous day-by-day course is archived in the local tag `archive/pre-refactor-2026-11-02`
and in `C:\Users\DELL\DE-Courses-history-2026-11-02.bundle`. Read an old file with
`git show archive/pre-refactor-2026-11-02:02-python/README.md`.
