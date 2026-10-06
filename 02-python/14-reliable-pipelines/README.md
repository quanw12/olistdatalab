# Chapter 14 — Reliable pipelines and capstone

[Previous chapter](../13-apis-and-databases/README.md) · [Course index](../README.md)

These are original DE extensions. They do not claim to be additional chapters from the selected video. Finish the preceding chapter, or demonstrate its checkpoint independently.

Read [extension setup](../de-setup.md) once and use [the self-study guide](../../docs/study.md) throughout. Each lesson includes an automated offline checker; leave exercise.py for your own implementation.

## Lesson order

| Lesson | Focus |
|---|---|
| [C14-L01](01-incremental/guide.md) | Incremental state, replays, and corrections |
| [C14-L02](02-data-quality/guide.md) | Data-quality checks and fixed-clock freshness |
| [C14-L03](03-capstone/guide.md) | Capstone: reproducible retail ingestion |

## Chapter checkpoint

Handle corrections and stale versions, measure quality, and recover output publication after database commit.

Pass each local checker, explain its central rule in your own words, and repeat one task with changed input. A passing test is evidence for its cases, not proof of mastery. Mark [progress](../progress.md) only after completing your own work.

The capstone has a [detailed contract and rehearsal](03-capstone/contract.md). Reserve multiple sessions for implementation and the failure/recovery demonstration.
