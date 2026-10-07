# 04 — Data Engineering

[Home](../README.md) · [Overall roadmap](../roadmap.md) · [Study guide](../docs/study.md)

**After Foundations, Python and Linux, read [setup.md](setup.md), then start [DE01](01-workflow/01-systems/guide.md).** This course has **29 lessons: 25 core and 4 optional**. It develops the reasoning, implementation and recovery skills needed for a scoped intern task.

## Modules

| Module | Lessons | Outcome |
|---|---|---|
| [Workflow](01-workflow/README.md) | DE01–DE03 | Trace a system, plan a ticket and debug unfamiliar code |
| [Data design](02-data-design/README.md) | DE04–DE07 | Contracts, grain/history, actual database rollback and measured query plans |
| [Pipelines](03-pipelines/README.md) | DE08–DE11 | Correct state, tied cursors, backfills, quality and recovery |
| [Warehouse](04-warehouse/README.md) | DE12–DE15 | Local analytical layers and tested dbt transformations |
| [Orchestration](05-orchestration/README.md) | DE16–DE18 | One Prefect workflow; DE18 Airflow transfer is optional |
| [Platforms](06-platforms/README.md) | DE19–DE22 | Cloud/IAM/cost concepts and verified AI; DE20 live cloud and DE21 Spark are optional |
| [Delivery and assessment](07-internship/README.md) | DE23–DE29 | Metrics, portfolio, unfamiliar task, source discovery, restore and interviews; DE24 ML data is optional |

Use Python, native PostgreSQL, a small local dbt/DuckDB warehouse, Prefect and the Docker/CI skills already practised. Complete the core before adding an optional platform. Lesson IDs are DE01–DE29; folder numbers define module order.

## Verify and deliver

Follow the lesson guide's concepts → task → help → verification → reflection/commit sequence. Ten small contracts have offline checks, including DE03 debugging. Other lessons require SQL, dbt, native-database, workflow or documented design evidence; their expected.md specifies it.

Build the [integrated retail capstone](project/capstone/contract.md), then complete DE26's unfamiliar assignment independently. DE27 profiles a new source; DE28 proves a native database restore before DE29 applications. Use [assessment](../docs/assessment.md) to find gaps and [interviews](../docs/interviews.md) to practise explanations. Track core/optional work in [progress](progress.md).

Read [resources](../docs/resources.md) for focused references and [sources](sources.md) for provenance and actual author validation. Local reference passes do not mark your work complete. A small project cannot establish mastery of every production platform.

Every guide includes manual commit commands using the current paths. Keep your feature/... branch convention and review the staged diff. Shared folder/Git rules are in [workspace](../docs/workspace.md).
