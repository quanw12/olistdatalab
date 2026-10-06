# The 30-day Data Engineering foundation

## How to use this plan

Each row is one lesson. Budget 2.5–4 hours, with extra setup time for a new tool. Read concepts and syntax, solve the exercise, use help selectively, verify and commit. Finish a core task before starting its dependent lesson; the day number is a sequence, not a deadline.

For your current position, continue at [Day 12](day-12/guide.md). Earlier attempts are preserved under each day's previous-work/. Unfinished Day 12 remains in the stash documented in the repository README.

| Day | Lesson | Concrete deliverable |
|---|---|---|
| [01](day-01/guide.md) | Python and CSV cleaning | Clean a CSV with rejection counts |
| [02](day-02/guide.md) | Functions, lists, dictionaries, and sets | Return and print a structured summary |
| [03](day-03/guide.md) | JSON, configuration, and datetime | Extract a configured JSON snapshot |
| [04](day-04/guide.md) | Clean tabular data with pandas | Filter invalid rows with pandas |
| [05](day-05/guide.md) | Join and aggregate with pandas | Build a joined city summary |
| [06](day-06/guide.md) | CLI, environment variables, and HTTP APIs | Fetch weather with a CLI |
| [07](day-07/guide.md) | Mini-project 1: a reproducible weather snapshot | Finish the first offline pipeline |
| [08](day-08/guide.md) | PostgreSQL tables, keys, and constraints | Create constrained tables in pgAdmin |
| [09](day-09/guide.md) | SQL joins, grouping, and NULL | Write ten join/aggregate queries |
| [10](day-10/guide.md) | CTEs, CASE, dates, and subqueries | Write ten CTE/date/subquery reports |
| [11](day-11/guide.md) | Window functions and time comparisons | Write eight window-function queries |
| [12](day-12/guide.md) | Data modeling: grain, dimensions, and facts | Build a dimensional model |
| [13](day-13/guide.md) | Load PostgreSQL from Python | Load normalized JSON in one transaction |
| [14](day-14/guide.md) | Mini-project 2: a reusable loader and SQL mart | Package a loader and dimensional mart |
| [15](day-15/guide.md) | Reliable HTTP extraction and bounded retries | Prove bounded HTTP retries |
| [16](day-16/guide.md) | ETL, file layers, and a complete batch pipeline | Create raw/clean/rejected layers and manifests |
| [17](day-17/guide.md) | Incremental loads, corrections, and backfills | Handle corrections, progress and backfill |
| [18](day-18/guide.md) | Docker and Linux CLI from the beginning | Run persistent PostgreSQL; learn Linux commands |
| [19](day-19/guide.md) | Package the pipeline with Docker Compose | Run the application with Compose |
| [20](day-20/guide.md) | Orchestration with Prefect flows and tasks | Observe Prefect flow/task states |
| [21](day-21/guide.md) | Mini-project 3: schedule and observe repeated runs | Schedule the third mini-project |
| [22](day-22/guide.md) | Meaningful automated tests with pytest | Test contracts and transactions |
| [23](day-23/guide.md) | Data quality and deterministic freshness checks | Report quality with a fixed clock |
| [24](day-24/guide.md) | Warehouses, query plans, and a small cloud lab | Read query plans; optional cloud warehouse |
| [25](day-25/guide.md) | Analytics: turn clean data into an honest report | Create three charts and a supported report |
| [26](day-26/guide.md) | Continuous integration with GitHub Actions | Run offline tests in GitHub Actions |
| [27](day-27/guide.md) | Use AI assistance with deterministic verification | Validate AI proposals against computed facts |
| [28](day-28/guide.md) | Capstone architecture, contracts, and runbook | Document architecture and recovery |
| [29](day-29/guide.md) | Rehearse end to end and recover from failures | Rehearse fresh setup and failures |
| [30](day-30/guide.md) | Package the portfolio and explain your decisions | Finish a portfolio demo and skills assessment |

## Deliberate scope

One language (Python), one relational database (PostgreSQL), one orchestrator (Prefect), one container workflow (Docker/Compose), and one optional warehouse (BigQuery). Git and testing recur throughout. CLI practice starts in PowerShell; Day 18 introduces a Linux shell explicitly.

The [roadmap.sh DE map](https://roadmap.sh/data-engineer) is a long-term checklist. This month selects a connected path. Spark is a conceptual introduction on Day 24; these small fixtures do not need distributed processing. Kafka, Kubernetes, Terraform, Airflow, dbt, multiple clouds and production Spark are deferred until a later goal justifies them.

## Milestones

- Day 07: reproducible weather snapshot with validation.
- Day 14: packaged loader and dimensional PostgreSQL mart.
- Day 21: repeatable pipeline with containers and orchestration.
- Day 30: portfolio with reproducible setup, failure evidence, analytics and a short demo.

## Outcome and next stage

You practise reading files/APIs, defining contracts, validating data, loading safely, writing analytical SQL, handling reruns/failures and explaining your decisions. This supports later DA reports and ML feature pipelines.

One month does not establish mastery of all DE tools or guarantee internship readiness. Use your capstone's weak points to build deeper Python, SQL and engineering tracks in separate folders afterward.
