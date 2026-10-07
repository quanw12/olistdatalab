# 02 — Python

[Home](../README.md) · [Overall roadmap](../roadmap.md) · [Study guide](../docs/study.md)

**After the foundation course, start at [C01-L01: run and print](01-fundamentals/01-run-print/guide.md).** This course has 56 lesson units across 14 chapters. It develops independent programming before deeper data-system work.

Chapters 1–8 follow the eight-chapter order in [your selected video](https://www.youtube.com/watch?v=Rq5gJVxz55Q). The outline was aligned using your screenshots and public syllabus; a complete transcript was not retrieved. Chapters 9–14 and supplementary exercises are original. See [source notes](sources.md).

Read [setup.md](setup.md) before Chapter 1 and [de-setup.md](de-setup.md) before Chapter 9. Each lesson starts with guide.md and includes concepts/syntax, a prompt-only exercise.py, help and expected results. Early lessons use manual result checks; all 21 extensions include a local check.py. The native PostgreSQL lab additionally has a live-server checker.

## Part A — video-aligned fundamentals

| Chapter | Folder | Lessons | Why it is divided this way |
|---|---|---|---|
| 1 | [Python Fundamentals](01-fundamentals/README.md) | 3 | Three lessons combine setup/output and variables/input, then give types their own practice. |
| 2 | [Python Strings](02-strings/README.md) | 3 | Three lessons separate normalization, slicing, and searching/validation. |
| 3 | [Python Numbers](03-numbers/README.md) | 2 | Two lessons cover arithmetic, then rounding and controlled randomness. |
| 4 | [Python Logic & Operators](04-logic/README.md) | 3 | Three lessons separate truth values, combined rules, and identity/membership. |
| 5 | [Python Conditional Statements](05-conditions/README.md) | 3 | Three lessons progress from branches to nested rules and compact syntax. |
| 6 | [Python Loops](06-loops/README.md) | 5 | Five lessons split loop control, loop-else, and nested iteration. |
| 7 | [Python Data Structures](07-data-structures/README.md) | 10 | Ten lessons give mutation, copying, sorting, sets, and dictionaries focused practice. |
| 8 | [Python Functions](08-functions/README.md) | 6 | Six lessons separate function design, argument binding, returns/scope, flexible arguments, callable forms, and integration. |

## Part B — original Python-for-DE extensions

Before Chapter 9, complete [extension setup](de-setup.md). These are supplied lessons, not only a future syllabus.

| Chapter | Folder | Lessons | Practice |
|---|---|---|---|
| 9 | [Errors and typed records](09-errors-and-types/README.md) | 3 | Exceptions, logging, type hints and dataclasses |
| 10 | [Files and time](10-files-and-time/README.md) | 4 | Paths/context managers, safe writes, CSV/JSONL, datetime and Decimal |
| 11 | [Projects and tests](11-projects-and-tests/README.md) | 4 | Imports, environments, CLI/configuration, unittest/pytest and mocks |
| 12 | [Data processing](12-data-processing/README.md) | 3 | Generators/batches, pandas joins and Parquet |
| 13 | [APIs and databases](13-apis-and-databases/README.md) | 4 | Pagination, retries, SQL parameters, SQLite and native PostgreSQL |
| 14 | [Reliable pipelines](14-reliable-pipelines/README.md) | 3 | Corrections, data quality and a persistent retail capstone |

## Completion

Use each chapter's checkpoint and [progress](progress.md). After Chapters 3, 6, 8 and 14, complete the [independent checkpoints](checkpoints.md). Easy lessons may be short refreshes if you solve and explain a changed input independently. Difficult topics can take several sessions; do not replace coding practice with video time.

Part A ends with a [weather validator/report](08-functions/06-clean-functions/guide.md). Part B ends with a [retail ingestion capstone](14-reliable-pipelines/03-capstone/guide.md): validation, quarantine, exact money, UTC time, persistent latest-version state, replay, rollback and recovery.

Pass [Python Gate A](../docs/assessment.md#gate-a--python-independence-90120-minutes) before continuing to [Linux](../03-linux/README.md). Keep SQL practice alongside the current course. Setup, chapter checkpoints and checks define this course; use the root roadmap for the overall calendar.

Save experiments in scratch.py and your reasoning in notes.md inside the lesson. Its guide contains scoped commit commands. [Workspace conventions](../docs/workspace.md) explain the feature/... branch naming and the course-folder migration.
