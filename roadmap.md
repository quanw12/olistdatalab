# Learning roadmap

[Home](README.md) · [Study method](docs/study.md) · [Readiness checks](docs/assessment.md)

**Study in this order: 30-day DE foundations → Python → Linux → Data Engineering.** SQL practice continues alongside the current course, using your own SQL learning resources. There is no separate `intern-prep` course.

Your current position is **Foundation Day 12**. Days 1–11 remain completed. Finish Days 12–30 before starting the next course; use the earlier lessons as references when a gap appears.

## 1. Foundations: complete the 30-day course

Open [01-foundation](01-foundation/README.md). Its [lesson index](01-foundation/lessons.md) contains all 30 days, in order. This is the full review and practice course, with one lesson per day number. A difficult lesson can take more than one session.

| Days | Focus | What you build |
|---|---|---|
| 01–07, completed | Python, CSV/JSON, pandas, CLI and APIs | A reproducible weather snapshot |
| 08–14 | PostgreSQL, analytical SQL, grain, facts/dimensions, loading | A database loader and weather mart |
| 15–21 | HTTP reliability, ETL, incremental work, Docker, orchestration | A repeatable batch pipeline |
| 22–27 | Tests, data quality, warehouse concepts, reports, CI, verified AI | Evidence that the pipeline is correct and recoverable |
| 28–30 | Documentation, recovery rehearsal, demo | A complete weather portfolio project |

**Exit check:** run the weather project from its README, explain one record from source to report, rerun it without duplicating observations, and demonstrate one failure and recovery. Identify guided work honestly. You do not need to master every introduced tool here.

## 2. Python: write a program independently

Open [02-python](02-python/README.md). Chapters 1–8 follow your selected video's order; Chapters 9–14 are original DE practice. There are 56 small lesson units. Read the [source notes](02-python/sources.md) for the limits of video alignment.

| Chapters | Focus | Required outcome |
|---|---|---|
| 01–08 | Types, strings, numbers, logic, conditions, loops, collections, functions | Write and explain a small validator and grouped report |
| 09–11 | Errors, logging, types, files, time/money, imports, environments, CLI, tests | Make a runnable program with explicit boundaries and useful tests |
| 12–13 | Generators/batches, pandas, Parquet, APIs, database access | Handle files and external systems without hiding failures |
| 14 | Corrections, quality and persistent state | Build the Python retail ingestion capstone |

Begin at Chapter 1 because syntax and independent coding are your stated gaps. An easy lesson can be a short refresh: solve it before looking at help and explain a changed input. Do not skip functions, mutation, exceptions or tests merely because you have seen their syntax.

**Exit check:** pass [Gate A](docs/assessment.md#gate-a--python-independence-90120-minutes) using a new input and a blank implementation. Repair specific weaknesses before moving on.

## 3. Linux: run, inspect and deliver your program

Open [03-linux](03-linux/README.md). Complete LE01–LE22 in order. This stage uses a supplied application so you can concentrate on the environment around a program.

| Lessons | Focus | Required outcome |
|---|---|---|
| LE01–LE09 | Shells, paths, streams, permissions, Bash, arguments, exit codes | Write a quoted wrapper that runs the right interpreter and reports failure |
| LE10–LE12 | Processes, ports, HTTP and diagnosis | Distinguish an environment failure from an application/data failure |
| LE13–LE15 | Git, staging, conflicts, collaboration | Review and repair a change without losing someone else's work |
| LE16–LE22 | Docker, Compose, CI and delivery | Deliver the supplied batch app, retain its outputs and demonstrate recovery |

**Exit check:** use a fresh terminal, follow your runbook, run a successful and failed batch, explain its logs/status, resolve a practice Git conflict, and demonstrate the container/CI behavior you claim. Docker is taught explicitly; it is not a prerequisite for the earlier Bash lessons.

## 4. Data Engineering: turn a task into a reliable result

Open [04-data-engineering](04-data-engineering/README.md). Complete **23 core lessons**; four optional lessons are marked separately. This stage builds on the earlier courses rather than introducing another Python or Linux course.

| Module | Lessons | What becomes your responsibility |
|---|---|---|
| [Workflow](04-data-engineering/01-workflow/README.md) | DE01–DE03 | Trace the data system, clarify a ticket, read/debug unfamiliar code |
| [Data design](04-data-engineering/02-data-design/README.md) | DE04–DE07 | Contracts, grain/history, native transactions, indexes and query plans |
| [Pipelines](04-data-engineering/03-pipelines/README.md) | DE08–DE11 | Corrections/deletes, cursors/backfills, quality, reconciliation and recovery |
| [Warehouse](04-data-engineering/04-warehouse/README.md) | DE12–DE15 | Raw/staging/mart layers, local DuckDB, dbt models/tests and incremental state |
| [Orchestration](04-data-engineering/05-orchestration/README.md) | DE16–DE17 | Dependencies, parameters, retries and real Prefect run evidence |
| [Platforms](04-data-engineering/06-platforms/README.md) | DE19, DE22 | Storage/IAM/cost reasoning, credentials, privacy and verified LLM assistance |
| [Delivery and assessment](04-data-engineering/07-internship/README.md) | DE23, DE25–DE27 | Metrics, integrated retail portfolio, an unfamiliar task and interview explanations |

Optional: **DE18 Airflow transfer, DE20 BigQuery sandbox, DE21 Spark introduction, DE24 ML feature data**. Attempt one when a project or role needs it, after the core works. Conceptual cloud design is core; a paid cloud deployment is not required. No mandatory Kafka, Kubernetes, Terraform or second cloud is added.

**Exit check:** pass [Gates A–F](docs/assessment.md), deliver the [retail capstone](04-data-engineering/project/capstone/contract.md), and complete DE26 without a generated implementation. The goal is to handle a small, scoped intern assignment: identify unknowns, implement a slice, check results, debug a failure and communicate a clear handoff. Asking a focused question is part of independent work.

## Why some topics appear twice

The foundation introduces tools in one connected weather project. Later courses practise ownership of their behavior. Use earlier syntax notes as references; do the later exercise because its acceptance criteria are different.

| Introduction | Later depth | New evidence |
|---|---|---|
| Foundation Python examples | Python functions, errors, files and tests | A new program written without a template solution |
| Foundation SQL/model | DE04–DE07 | Contract evolution, event-time history, actual rollback and a measured query plan |
| Foundation incremental load | Python capstone and DE08–DE11 | Persistent state, deletes, equal-version conflicts, tied cursors and publication recovery |
| Foundation Docker/Prefect | Linux delivery and DE16–DE17 | Shell/status ownership, service addressing, reproducible runs and retry boundaries |
| Foundation warehouse/AI | DE12–DE15 and DE22 | Tested transformation dependencies and deterministic checks of untrusted proposals |

The Python project assesses programming, the Linux project assesses delivery, and the final retail project integrates both with modeling and reliability. They are not three unrelated technology stacks. The final project should reuse verified components with documented interfaces.

## What the core covers

| Skill | Where to practise |
|---|---|
| DE lifecycle, OLTP/OLAP, batch/stream, requirements and acceptance criteria | DE01–DE02 |
| Python syntax, functions, collections, errors, modules, CLI/configuration | Python Chapters 01–11 |
| CSV/JSONL/Parquet, generators/batches, UTC/event time, exact money | Python Chapters 10–13; DE04, DE09 |
| HTTP, pagination, timeouts, bounded retries and source limitations | Foundation 06/15; Python Chapter 13 |
| SQL joins/cardinality, NULL, dates, CTEs, windows and query reasoning | Foundation 08–11; independent SQL; Gate B; DE07 |
| Relational and dimensional design, keys, constraints, history, transactions | Foundation 12–14; Python PostgreSQL; DE04–DE07 |
| ETL/ELT, state, corrections, tombstones, checkpoints, backfills and reruns | Foundation 16–17; Python Chapter 14; DE08–DE11 |
| Testing, quality, reconciliation, freshness, observability and recovery | Python Chapter 11; Foundation 22–23; DE03, DE10–DE11 |
| Linux/CLI, processes/networking, Git, Docker/Compose and CI | Linux LE01–LE22 |
| Warehouse layers, dbt models/tests and incremental correctness | DE12–DE15 |
| Dependencies, scheduling intervals, retries and orchestration evidence | Foundation 20–21; DE16–DE17 |
| Cloud storage/IAM/cost, credentials, privacy, checked AI/LLM use | DE19, DE22 |
| Read unfamiliar code, debugger, profiling, task plan and handoff | DE02–DE03, DE07, DE26 |
| Metrics, portfolio README/runbook, English explanation and independent task | DE23, DE25–DE27 |

Advanced distributed operation, production incident ownership and advanced model training remain beyond this preparation. Do not claim those from a small local lab.

## A realistic calendar from your current position

This is a planning estimate for **about 18–24 focused hours per week**, not a promise. Keep the order and extend a phase when its exit check fails.

| Weeks | Main course |
|---|---|
| 1–4 | Foundation Days 12–30; complete the weather project |
| 5–8 | Python Chapters 1–14; short refreshes for skills demonstrated independently |
| 9–10 | Linux LE01–LE22; allow extra setup time |
| 11–12 | DE01–DE11: workflow, design, reliable state and recovery |
| 13 | DE12–DE15: warehouse/dbt |
| 14 | DE16–DE17, DE19, DE22, DE23: orchestration, platforms and metrics |
| 15 | DE25: integrate and rehearse the retail capstone |
| 16 | DE26–DE27: unfamiliar task, targeted repairs, explanations and applications |

Keep two or three short SQL practice sessions each week and explain one result in English. An eight-week route is reasonable only if assessments already demonstrate substantial Python/SQL/Linux skill; it is not the default beginner schedule. Internship eligibility, hiring and the actual team's stack still vary.

## Start now

Open [Foundation Day 12](01-foundation/day-12/guide.md), complete its modeling task, verify the result and use its commit commands. Record progress in the course checklist. For study habits use [study.md](docs/study.md); for folder/Git conventions use [workspace.md](docs/workspace.md). These shared documents support the four courses; they are not additional courses.
