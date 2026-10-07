# AI Data

[Part 5](../README.md) · [Setup](../setup.md) · [Progress](../progress.md)

Build reliable data for retrieval. Python/SQLite provide the core runtime. [Real embedding lab](embedding-lab.md) is optional after AI05. There is no mandatory paid model or vector server.

Follow these eight lessons in order. Read each guide, then concepts/syntax, assignment, progressive help and acceptance criteria. A lesson is a unit of work, not necessarily a calendar day. Commit commands are included in every guide.

| Lesson | Focus | Verification |
|---|---|---|
| [AI01](01-documents/guide.md) | Define document identity and provenance | Offline contract + evidence |
| [AI02](02-text/guide.md) | Normalize text without losing paragraph structure | Offline contract + evidence |
| [AI03](03-chunks/guide.md) | Create deterministic overlapping chunks | Offline contract + evidence |
| [AI04](04-lexical/guide.md) | Build a local lexical retrieval baseline | Offline contract + evidence |
| [AI05](05-vectors/guide.md) | Rank vectors and distinguish fixtures from embeddings | Offline contract + evidence |
| [AI06](06-index-state/guide.md) | Propagate document edits and deletes | Offline contract + evidence |
| [AI07](07-evaluation/guide.md) | Evaluate retrieval before trusting generated answers | Offline contract + evidence |
| [AI08](08-capstone/guide.md) | Deliver a reproducible document search pipeline | Manual evidence |

## Exit check

A local document search pipeline with provenance, edit/delete handling and versioned retrieval evaluation. Demonstrate one successful run, one failure and recovery, one unfamiliar input and a clear English explanation. Record guided versus independent work honestly. Update only progress you have actually demonstrated.
