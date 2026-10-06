# Python — fundamentals and practical Data Engineering

**Start with [C01-L01: run a script and print](01-fundamentals/01-run-print/guide.md).**

This English course contains **56 lessons across 14 chapters**: 35 fundamentals lessons following the eight-chapter order in [your selected video](https://www.youtube.com/watch?v=Rq5gJVxz55Q), followed by 21 original Python-for-DE extensions. Each lesson includes explanations, syntax examples, a prompt-only exercise, detailed hints, expected results and commit commands.

**Studying without Codex:** follow [self-study.md](self-study.md). The new extensions have local checkers, fixed fixtures and reflection answer keys. They require no LLM access.

The first eight chapters are aligned with your screenshots and the public course syllabus. Chapters 9–14 are original DE extensions. It is not a transcript or a copy of the instructor's handbook. A complete video transcript was not retrieved; [source notes](sources.md) identify shared video windows and supplementary practice.

## Follow this order

1. Read [setup.md](setup.md) once and use your existing interpreter.
2. Open the next lesson's guide.
3. Watch its linked video window; pause at each new concept.
4. Read lesson.md; predict and run the small example.
5. Write your own implementation in exercise.py.
6. Use help.md progressively, then compare with expected.md.
7. Explain the result, review your own work using the checks or request feedback when available, and commit with the guide's commands.

The files in a lesson belong together; they are not separate courses. Guides are the entry points. Exercise files initially contain only comments and intentionally print nothing.

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

All 21 extensions have check.py. The first 35 lessons retain their manual expected-output checks. The PostgreSQL lesson additionally has a separate optional live-server checker.

A lesson is a learning unit, not a fixed calendar day. Start with 60–120 minutes including video and practice; setup and the final project may take longer. Combine two easy lessons only if you can explain both; split a difficult lesson across sessions.

Long sections are deliberately split: loops into five lessons, data structures into ten, and functions into six. Shared video windows are labeled; you do not need to rewatch an entire window for each associated exercise.

## Folder pattern

~~~text
Python/
  README.md           # entry and chapter index
  setup.md            # shared Windows/Python instructions
  de-setup.md         # extension environment and troubleshooting
  self-study.md       # independent learning workflow
  requirements-de.txt # tested extension package versions
  check_support.py    # shared checking infrastructure
  data/               # fixed retail fixtures
  sources.md          # video map and source limitations
  progress.md         # completion checklist
  01-fundamentals/
    README.md         # chapter order and completion checkpoint
    01-run-print/
      guide.md
      lesson.md
      exercise.py
      help.md
      expected.md
  ...
  08-functions/
    ...
    06-clean-functions/
  09-errors-and-types/
    01-exceptions/
      ...
      check.py        # provided checker; implement exercise.py yourself
  ...
  14-reliable-pipelines/
    03-capstone/
~~~

Use scratch.py within a lesson when experimenting. Keep the final implementation in exercise.py. Any notes.md you create belongs in that lesson folder.

## Final project and boundaries

Part A ends with an in-memory weather validator and city report. Part B ends with a [retail ingestion capstone](14-reliable-pipelines/03-capstone/guide.md): CSV validation, quarantine, exact money, UTC timestamps, latest-version SQLite state, a batch ledger and reports. Its tests exercise reruns, corrections, stale records, rollback, empty input and publication recovery.

This provides practical core Python-for-DE coverage, not mastery of every Python topic or every DE tool. Advanced concurrency, distributed processing, production cloud operation and deeper SQL/modeling remain separate tracks in [the internship roadmap](../intern-prep/roadmap.md).

Chapters 1–8 need no third-party packages. Part B adds a small tested package set; most checks use only the standard library. No paid API or Docker is needed. The PostgreSQL live lab uses your native installation. Preparing the lessons does not mark learning complete.

## What to send for review

Provide the lesson ID, terminal result, and what confused you. Your implementation is in the shared workspace, so you can ask me to read the file directly. Explain one key decision in your own words. [Progress](progress.md) starts unchecked; creating materials does not mark your learning complete.

## Commit the prepared course

For the initial course-material commit, review the Python course and navigation updates. The earlier intern-prep roadmap is also still uncommitted; the command includes it.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- Python README.md intern-prep .gitignore
git diff --cached --stat
git diff --cached
git commit -m "docs(python): prepare fundamentals and DE self-study course"
git push -u origin HEAD
~~~

Use your current feature/... branch. These commands do not switch branches or apply the Day 12 stash. Later lesson guides stage only that lesson's folder. Previously staged files remain staged; inspect the full diff before committing.
