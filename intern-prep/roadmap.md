# Detailed DE internship roadmap

## Goal and evidence

Goal: independently complete a modest data engineering assignment, check its correctness, and explain your decisions. This plan develops Python, SQL, databases, pipelines, and the ability to deliver working code. It does not require senior-level mastery of every DE technology before you apply.

The starting recommendation is **Python first with SQL alongside**, based on your reported difficulty writing a complete program independently. Your earlier SQL exercises show exposure to joins, CTEs, and windows; they do not establish mastery of unseen problems.

Published Vietnam role examples support prioritizing the fundamentals:
- [Pizza Hut Vietnam's DE intern description](https://pizzahut.talent.vn/job/hcm-data-engineer-intern-53453) asks for SQL, a programming language with Python preferred, and basic pipeline/modeling/cloud knowledge. It accepts familiarity with at least one of several platform tools. Its June 30, 2026 deadline has passed.
- [Kyanon Digital's trainee description](https://kyanon.digital/wp-content/uploads/2025/10/202509_Kyanon-Digital-_-Data-Engineer-Trainee-1.pdf) names SQL, Python or another language, ETL, pipelines, and APIs; cloud/Spark/Kafka/Airflow exposure is listed as a bonus. Current vacancy availability is unconfirmed.

These are examples of requirements, not a survey of the whole market or a list of active vacancies. Our learning order is an inference from your gaps and those examples. Check actual target internships again before choosing specialized tools.

## Priority and progression

**Core** means a practical capability to demonstrate. **Conditional** means learn it when a target role or project requires it. **Later** means useful depth after the core gates.

The tables define topic-sized lessons, not a promise to finish the whole track in that many calendar days. Each future lesson has one main topic, concepts and syntax before exercises, and detailed help separately.

| Track | Prerequisite | Practical scope | Completion gate |
|---|---|---|---|
| Python | Basic coding logic | Independent programs and debugging | Unseen CSV task with tests |
| SQL | Tables and SELECT; practise during Python | Correct analytical queries | Unfamiliar schema and edge cases |
| Database/modeling | Core SQL and Python functions/files | PostgreSQL schemas, transactions, models | Safe loader and reconciled mart |
| Reliable pipelines | Database gate and API basics | Batch pipelines and recovery | Replay/correction/failure proof |
| Delivery/platforms | Working local pipeline | CLI, containers, CI, orchestration, one cloud | Fresh setup and observable run |
| Internship rehearsal | Core gates; tool-specific additions as needed | Coding/SQL assignments and project explanation | Independent assignment and demo |

### Baseline diagnostic

Before assigning all Python lessons, attempt a small orders CSV task with documentation allowed:
- Validate order ID, timestamp, quantity, and decimal price.
- Reject bad records with reasons; handle missing values and duplicates under a stated rule.
- Return total accepted records and revenue by customer.
- Split logic into functions, separate printing from return values, and test an empty file.

If you cannot start or explain your own code, follow PY01 onward. If you can complete it independently, use errors to select a shorter refresh. AI-generated completion is not evidence of independence; explain and reproduce a key part yourself.

Do a separate SQL diagnostic: joins with a customer who has no orders, latest order per customer with ties, and revenue by month. Compare results against hand-computed rows.

## Track 1 — Python

Learn plain Python first. Add pandas once you can explain the equivalent row/collection logic. Use the [Python tutorial](https://docs.python.org/3.13/tutorial/) as a reference alongside instruction; it assumes some programming knowledge.

| ID | Main topic | What the teacher must explain | Practice target |
|---|---|---|---|
| PY01 | Values, variables, types | Assignment, conversion, comparisons, truthiness, None, mutable versus immutable values | Trace values and identify conversion errors |
| PY02 | Control flow | if/elif/else, for/while, indentation, break/continue, Boolean expressions | Validate rows and trace branches |
| PY03 | Collections | list/dict/set/tuple, indexing, iteration, get, membership, append/add, copying and shared references | Deduplicate IDs and group amounts by customer |
| PY04 | Functions | def, parameters/arguments, return versus print, scope, defaults, keyword arguments; avoid mutable defaults | Design small functions with clear input/output |
| PY05 | Transforming collections | Comprehensions after loops, sorting with key, enumerate/zip, grouping; when hashing avoids repeated searches | Build a reusable aggregation without pandas |
| PY06 | Errors and debugging | Read tracebacks, distinguish exception types, narrow try/except, raise, debugger/breakpoints | Repair deliberate logic and input failures |
| PY07 | Files and paths | pathlib, with, text encoding, csv/JSON, relative paths, structured output | Read fixtures reliably from different working directories |
| PY08 | Dates and numeric correctness | datetime parsing, aware versus naive time, timezone conversion, Decimal for money, validation boundaries | Normalize timestamps and preserve decimal totals |
| PY09 | Program structure | Modules/imports, main entry point, virtual environments, dependencies, argparse, configuration/environment variables | Turn functions into a reusable CLI with an importable module |
| PY10 | Objects and contracts | A small class/dataclass, methods, composition, type hints; hints do not validate runtime data | Represent a record clearly without unnecessary inheritance |
| PY11 | Tests | pytest assertions, parametrization, fixtures, testing errors, mocking external boundaries | Test empty, malformed, duplicate, and boundary inputs |
| PY12 | Independent mini-project | Decompose a specification; connect parsing, validation, transformation, output and tests | Build an orders cleaner/report from a blank implementation |

**Gate:** given a new fixture, produce accepted/rejected files and a customer report; show exact expected counts and totals, explain every function, and fix a deliberately introduced bug. Include CLI instructions, tests, and a short README. Do not mark a project complete solely because it runs on the happy path.

**Later Python depth:** iterators/generators and chunked processing; context managers; practical typing and packaging; profiling memory/time; decorators when encountered; bounded concurrency after a serial version is correct. Advanced metaclasses and descriptor implementation are not a prerequisite for this internship plan.

## Track 2 — SQL

Use PostgreSQL and pgAdmin, matching your existing setup. SQL is a continuing practice track while Python receives the initial emphasis. Prefer a course with datasets and questions over one that only demonstrates syntax. The [PostgreSQL tutorial](https://www.postgresql.org/docs/18/tutorial.html) provides a reference for queries, joins and aggregates.

| ID | Main topic | What to understand | Practice target |
|---|---|---|---|
| SQ01 | Query logic and NULL | Logical evaluation, WHERE, ORDER BY, NULL comparisons and three-valued logic | Explain why filters exclude missing values |
| SQ02 | Aggregation | GROUP BY, HAVING, COUNT(*) versus COUNT(column), conditional aggregation | Reconcile row counts and business totals |
| SQ03 | Joins and cardinality | Inner/left joins, keys, one-to-many/many-to-many, filter placement, unmatched rows | Diagnose duplicated revenue after a join |
| SQ04 | Subqueries and existence | Scalar/table subqueries, correlated subqueries, EXISTS/NOT EXISTS; NULL traps in NOT IN | Find entities with and without matching activity |
| SQ05 | CTEs and set operations | Readable stages, UNION ALL versus UNION, INTERSECT/EXCEPT, CASE | Combine sources under a stated duplicate rule |
| SQ06 | Window functions | Partition/order, ROW_NUMBER/RANK/DENSE_RANK, LAG/LEAD, frames, tie handling | Compute latest records, changes and running totals |
| SQ07 | Time-based queries | DATE/TIMESTAMPTZ, timezone-aware grouping, intervals, half-open date ranges | Report local-day totals at midnight boundaries |
| SQ08 | Analytical questions | Grain, numerator/denominator, latest-per-key, missing periods, basic retention/cohorts | Translate a business request into a documented query |
| SQ09 | Quality and reconciliation | Uniqueness, completeness, orphan detection, join coverage, source-to-mart totals | Write checks that catch a faulty transformation |
| SQ10 | Plans and efficiency | Read EXPLAIN, estimates versus actuals, scan/join/sort costs; avoid unsupported performance claims | Compare queries with representative data and a plan |

**Gate:** solve an unfamiliar customer/order/order-item schema with at least 12 questions, including no-order customers, join multiplication, ties, NULLs and time boundaries. Predict a small fixture's results before execution; explain why every join is safe at the chosen grain.

The [PostgreSQL EXPLAIN guide](https://www.postgresql.org/docs/18/using-explain.html) is a reference. EXPLAIN ANALYZE executes the statement; use controlled lab data for experiments, especially writes.

**Later SQL depth:** recursive CTEs, complex sessionization, gaps/islands, more demanding cohort questions and performance tuning. Practise these after ordinary joins/windows are dependable.

## Track 3 — PostgreSQL and data modeling

| ID | Main topic | Depth and practice |
|---|---|---|
| DB01 | Grain and keys | Define one row in words; distinguish natural/surrogate/composite keys; resolve duplicate business IDs |
| DB02 | Relational design | Normalize customers/orders/items; define PK/FK/UNIQUE/NOT NULL/CHECK; test invalid inserts |
| DB03 | Types and temporal meaning | Choose numeric precision, timestamps and timezone metadata; preserve meaning across Python and PostgreSQL |
| DB04 | Transactions | Commit/rollback, atomic loading, basic isolation/locking; demonstrate a failed load leaves no partial batch |
| DB05 | Index design | Composite key order, selectivity, read/write trade-offs; justify an index using a measured query plan |
| DB06 | Dimensional modeling | OLTP versus OLAP, facts/dimensions, star schema, measures, daily aggregates and grain changes |
| DB07 | Corrections and history | UPSERT, deterministic winner rules, SCD Type 1; introduce Type 2 when historical attributes are required |
| DB08 | Evolving a schema | Reproducible migrations, staging-to-mart flow, backfill/reconciliation and documenting compatibility |

**Mini-project:** model retail orders and line items, load them from Python using parameterized SQL, and build a daily sales mart. Explicitly define revenue, cancelled orders, and line-item grain. Keep native PostgreSQL/pgAdmin until the Docker lesson has been taught.

**Gate:** explain the model, enforce invalid-row rejection, prove rollback, handle a corrected record and replay, and reconcile the mart with the accepted source. Deep database administration and distributed transaction theory can follow later.

## Track 4 — Reliable pipelines

This revisits foundation concepts using a new domain and less scaffolding.

| ID | Main topic | Depth and practice |
|---|---|---|
| DE01 | Data contracts | Required fields, types, units, keys, timestamps, freshness, schema changes; distinguish quarantine from a failed run |
| DE02 | APIs | HTTP/JSON, pagination, auth, timeouts, status codes, bounded retries/backoff, rate limits; test with offline responses |
| DE03 | ETL/ELT and layers | Raw/staging/clean/mart responsibilities, CSV/JSON/Parquet trade-offs, provenance and reproducible transformation |
| DE04 | Incremental processing | Watermarks and event time, late data, corrections, overlap windows, backfills; introduce CDC conceptually |
| DE05 | Idempotency and state | Stable keys, source versions, transaction boundaries, checkpoint timing and file writes; replay must not double-count |
| DE06 | Quality and testing | Unit/integration/contract tests, uniqueness, null/range rules, reconciliation and deterministic freshness |
| DE07 | Observability and failure | Structured logs, batch IDs, counts/duration, failure categories, actionable alerts, recovery runbook |
| DE08 | Independent pipeline | Connect extract/validate/load/report; demonstrate replay, correction and failure recovery |

**Mini-project:** a retail orders pipeline using fixed CSV/API fixtures, PostgreSQL and a daily mart. Live API access is a separate optional mode. Fixture tests must work without network access.

**Gate:** a rerun preserves the intended state; a newer correction wins; a failed transaction does not advance progress; a backfill reconciles with a full rebuild. Explain what the pipeline guarantees and what it does not.

## Track 5 — Delivery and platforms

| ID | Main topic | Core practical scope |
|---|---|---|
| OP01 | Linux/CLI | Paths, pipes, redirection, permissions, processes, environment variables, exit codes and basic network diagnosis; distinguish PowerShell from Bash syntax |
| OP02 | Git and CI | Branches, meaningful commits, diff/review, conflicts, PRs, secrets hygiene and an automated offline test job |
| OP03 | Docker/Compose | Images versus containers, Dockerfile, ports, networks, mounts/volumes, logs and persistence; explain before using commands |
| OP04 | Orchestration | Dependencies, schedules, run/task states, retries, backfills and preventing conflicting runs; deepen existing Prefect practice |
| OP05 | One cloud | Storage, warehouse, IAM basics, credentials, usage/cost controls, load/query workflow and cleanup; pick the target employer's cloud |
| OP06 | Warehouse delivery | Partitioning/clustering concepts, models, incremental transformations, quality checks and reproducible SQL changes |

**Gate:** another person can run the fixture pipeline using the README; CI catches a real regression; failures are visible; data persists as intended; you can explain the boundaries between scheduler, code, database, and storage.

Git and tests already recur in earlier tracks. This stage deepens delivery; it does not postpone engineering habits.

Choose one cloud only. BigQuery/GCP continues the foundation course if no target role determines the choice; switch to Azure/AWS when selected internship requirements justify it. A cloud design exercise can precede an account-based lab.

### Conditional tool depth

| Tool/topic | When to add it | What the first deeper module covers |
|---|---|---|
| Airflow | Target roles require it, or you need to transfer orchestration knowledge | DAG/task dependencies, schedules/data intervals, retries, backfill and local reproducibility |
| dbt | Target roles focus on warehouse SQL transformations | Models, sources, refs, tests, documentation, incremental model correctness |
| Spark | Target roles require PySpark or a workload justifies distributed processing | DataFrame schemas, NULLs, transformations/actions, joins, partitions, shuffles, plans and skew basics |
| CDC/streaming | A role/project needs continuously changing events | Change events, ordering, duplicates, checkpoints and delivery semantics before adding Kafka tooling |

Small fixture files do not need Spark. Explain its purpose before installing it. A Spark lesson should compare the same transformation with Python/SQL, then identify which workload properties make distributed processing relevant. Kubernetes and multiple orchestrators/clouds are later specializations.

## Track 6 — Internship rehearsal

| ID | Main topic | Evidence |
|---|---|---|
| IN01 | Practical coding | Solve parsing, grouping, sorting and deduplication; explain basic time/memory complexity; handle edge cases |
| IN02 | SQL interview practice | Solve unseen timed questions, then review correctness, readability and cardinality |
| IN03 | Assignment and review | Read an unfamiliar repo/specification, fix a defect, add a useful test and explain a review diff |
| IN04 | Project and applications | Fresh setup/demo, architecture trade-offs, failure recovery, concise English answers, CV/GitHub evidence and target-role matching |

Use 3–5 actual internship descriptions to build a requirement matrix: required, preferred, demonstrated, missing. A requirement appearing in one role does not automatically become a prerequisite for every application.

**Readiness checkpoint:** you can build and debug a small task independently, write correct SQL, explain grain and safe loading, demonstrate a reproducible project, and identify your own limits. Start applying when you can show relevant evidence; continue learning during applications. There is no guaranteed hiring outcome from completing a checklist.

## Optional DA and AI/ML branches

| Branch | Prerequisites | Initial scope | Deliverable |
|---|---|---|---|
| DA | SQL gate and a trustworthy mart | Metric definitions, descriptive statistics, chart choice, missing data, one BI tool such as Power BI | Dashboard plus a written explanation of assumptions |
| ML data preparation | Python/SQL and pipeline gates | Feature definitions, time-aware splits, leakage, training/validation/test, reproducibility and basic model evaluation | Repeatable feature dataset with leakage checks |
| LLM-assisted engineering | Practise from the first track with verification | Explain unfamiliar code, request hints, suggest edge cases, review SQL; validate outputs and protect credentials/private data | An assistance log showing proposals, checks and corrections |
| LLM pipeline integration | Reliable pipeline gate and a real use case | Structured outputs, schema validation, bounded calls, retries, evaluation cases and deterministic fallback | A narrow enrichment component with measured failure cases |

Use AI to ask for explanations or graded hints before requesting a complete solution. Run checks, inspect every change and independently reproduce core logic. LLM outputs do not replace validation, SQL constraints, or source evidence. Model training and agent frameworks are not required to learn basic DE.

## Portfolio strategy

Keep the weather foundation project. Build the deeper retail project to demonstrate transfer:
- Python cleaner and tests become the file-processing component.
- SQL reports and the data model become the PostgreSQL mart.
- Incremental pipeline work adds reliable loading and recovery.
- Delivery work adds CI, containers, orchestration and one optional cloud lab.
- A final README explains the question, grain, architecture, setup, checks, limitations and a short demo.

Each track must have a small standalone deliverable before integration. Add a third short unseen assignment for independence if needed, rather than expanding one project with every tool.

## Choosing the next lesson

Current status: **[56 Python lessons](../Python/README.md) prepared: 35 video-aligned lessons plus 21 original DE extensions**. The first eight chapters' map is grounded in the supplied screenshots and public syllabus; full-transcript coverage was unavailable. Individual learning gates are not marked passed.

Follow [Python C01-L01](../Python/01-fundamentals/01-run-print/guide.md) onward in the video's order: fundamentals, strings, numbers, logic, conditions, loops, collections, then functions. This develops PY01–PY05 and part of independent program construction. Chapters 9–11 now provide practice for PY06–PY11, including extra pytest syntax practice. Chapters 12–14 add data libraries, integration and a file-based capstone supporting PY12. The lessons provide material for these gates; you must still demonstrate the capability independently. Keep one SQL exercise session after every two Python study sessions initially.

Before each new track, review your submitted code and choose the next unresolved capability. After each track, repeat the gate with a new fixture or question. Repeat focused practice when necessary; do not repeat the whole course automatically.
