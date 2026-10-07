# Learning roadmap

[Home](README.md) · [Study method](docs/study.md) · [Readiness checks](docs/assessment.md)

**Next: [Foundation Day 12](01-foundation/day-12/guide.md).** Days 1–11 remain completed.
Continue your current Day 12 implementation.

## Core order

Use one main course at a time; SQL continues alongside it through your own resources.
A lesson number is a unit of work, not a promise to finish in one day.

| Order | Course | Demonstrated outcome |
|---|---|---|
| 1 | [Foundation: 30 days](01-foundation/README.md) | Weather pipeline, database model, tests and failure/recovery. Your first broad review. |
| 2 | [Python: 56 units](02-python/README.md) | Programs from blank files, then reliable file/API/database work; independent checkpoints and Gate A. |
| 3 | [Linux: 22 units](03-linux/README.md) | Run/debug/deliver the supplied app; Bash statuses, Git collaboration, Docker persistence and CI behavior. |
| 4 | [Data Engineering: 25 core + 4 optional](04-data-engineering/README.md) | Clarify tasks, own contracts/state, test/recover, hand off data and handle an unfamiliar assignment. |

Course indexes give lesson order. This file gives overall order.

## Difficulty and repeated topics

Every guide states **Learn, Apply, Integrate or Assess**; see the
[definitions](docs/study.md#difficulty-and-hints). Group familiar syntax drills in
one session after a changed-case check. Read required syntax, attempt, then reveal
one hint if needed. Record hints used; a copied algorithm is guided practice.

Foundation introduces the weather workflow. Python isolates language boundaries.
Linux teaches execution around a supplied app. DE makes you own requirements,
state and delivery. A repeated topic must show a new input/failure/responsibility.
If a refresher is demonstrable, complete its variation and move on.

## Core coverage

| Skill | Practice |
|---|---|
| Python syntax, functions, collections, errors, objects | Python Chapters 1–9 |
| Files, exact money, time zones, CLI, packaging, tests | Python Chapters 10–12 |
| SQL, keys, analytical queries, fact/dimension grain | Foundation Days 8–12; your SQL study; Gate B; DE04–DE07 |
| Linux, HTTP diagnosis, Git/reviews, containers and CI | Linux LE01–LE22 |
| APIs, pagination, retries, ETL/ELT, parameterized loads | Foundation Days 13–17; Python Chapter 13 |
| Corrections/deletes, cursors, backfills, replay | Python Chapter 14; DE08–DE11 |
| Warehouse layers, dbt models/tests/incremental behavior | DE12–DE15 |
| Orchestration, logs, quality, reconciliation and recovery | DE09–DE17; Foundation Days 20–23 |
| Storage/IAM/cost concepts, secrets/privacy, verified AI | DE19, DE22 |
| Consumer metrics, dictionary and lineage | DE23, DE27 |
| Source profiling, owner questions and catalog | DE02 brief discovery; DE27 full exercise |
| Native database backup and verified restore | DE28 |
| Portfolio, unfamiliar task and English handoff | DE25–DE26, DE29; Gates A–G |

Optional in course 4: DE18 Airflow, DE20 BigQuery, DE21 Spark, DE24 ML feature data.
Add for a demonstrated need. One working orchestrator and one cloud direction are
enough for this learning path.

## Calendar estimate

Example: **16 weeks at roughly 18–24 focused hours/week**, including SQL and repair
time. This is an estimate, not a completion or hiring guarantee.

| Weeks | Main work |
|---|---|
| 1–3 | Foundation Days 12–30; integrations can span sessions. |
| 4–7 | Python; group familiar drills, reserve time for functions/tests/capstone/checkpoints. |
| 8–9 | Linux execution, collaboration and delivery. |
| 10–14 | Core DE and the integrated retail project. |
| 15–16 | Unfamiliar assignment, source/restore drills, failed-gate repair and handoff. |

At 10–15 hours/week, extend the calendar. An eight-week target requires demonstrated
prior competence and targeted refreshes; do not compress every unit into it.
Practise SQL in several short sessions each week and assess it with Gate B.

## Readiness and extensions

Use [Gates A–G](docs/assessment.md): independent results, meaningful failures and
clear limits. Check current student-year/location/work-schedule eligibility
separately. Apply to suitable roles when you can demonstrate relevant skills;
prepared materials alone do not establish readiness.

Then open [Part 5](05-extensions/README.md). All requested tracks remain available:

| Order | Track | New responsibility |
|---|---|---|
| 1 | [Engineering Labs](05-extensions/01-labs/README.md), 8 | Diagnose and repair maintenance tickets. |
| 2 | [Cloud](05-extensions/02-cloud/README.md), 8 | GCP storage/IAM, jobs, warehouse loads, scheduling and cost limits. |
| 3 | [AI Data](05-extensions/03-ai-data/README.md), 8 | Documents, retrieval, edits/deletes and evaluation. No paid LLM is needed. |
| 4 | [Streaming](05-extensions/04-streaming/README.md), 8 | Kafka, transactional sinks, CDC and restart evidence. |

Keep this teaching order, with extensions as later practice/specialization. Allow
additional months for all 32; finishing them is not required before applications.
Live services have separate setup/evidence requirements; offline checks do not prove deployment.

[Course review](docs/course-review.md) records difficulty decisions, duplication fixes,
added coverage and validation limits.
