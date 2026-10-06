# Chapter 13 — APIs and database integration

[Previous chapter](../12-data-processing/README.md) · [Course index](../README.md) · [Next chapter](../14-reliable-pipelines/README.md)

These are original DE extensions. They do not claim to be additional chapters from the selected video. Finish the preceding chapter, or demonstrate its checkpoint independently.

Read [extension setup](../de-setup.md) once and use [the self-study guide](../../docs/study.md) throughout. Each lesson includes an automated offline checker; leave exercise.py for your own implementation.

## Lesson order

| Lesson | Focus |
|---|---|
| [C13-L01](01-pagination/guide.md) | HTTP responses, pagination, and bounded extraction |
| [C13-L02](02-retries/guide.md) | Retry only transient failures |
| [C13-L03](03-sqlite-transactions/guide.md) | Parameterized SQL and transaction rollback |
| [C13-L04](04-postgresql/guide.md) | Native PostgreSQL with Psycopg |

## Chapter checkpoint

Bound pagination/retries, bind SQL values, and prove batch rollback and replay behavior.

Pass each local checker, explain its central rule in your own words, and repeat one task with changed input. A passing test is evidence for its cases, not proof of mastery. Mark [progress](../progress.md) only after completing your own work.

Complete the PostgreSQL [native-server lab](04-postgresql/live-lab.md) separately from its offline fake-connection check. No Docker is used.
