---
tags: [decourse, labs]
---

# Labs Guide

Labs are the code you write yourself. The **code lives in the separate code repo** under `labs/`; the **instructions live here** and in each module guide. Each lab folder in the repo contains a file with function signatures, docstrings and hints (no solutions) and a test file that describes the expected behaviour.

```powershell
# run from the root of the code repo
pytest labs/01-python -v      # red at first; make it green
```

| Lab folder (code repo) | Module guide | What you build | Done |
|---|---|---|---|
| `labs/01-python` | [[Module 01 - Python]] | Parse Olist timestamps, normalise statuses, find duplicates | [ ] |
| `labs/06-ingest` | [[Module 06 - Ingestion and Quality]] | Contract check, idempotent snapshot load, A→B→A | [ ] |
| `labs/07-api` | [[Module 07 - APIs]] | FX client with retry, pagination and raw replay | [ ] |
| `labs/19-incremental` | [[Module 19 - Incremental and CDC]] | Replay, version conflicts, deletes, moving partitions | [ ] |

Other modules ask you to create your own folder in `labs/` (`09-dbt/`, `11-airflow/`, `12-spark/`, `13-kafka/`, `15-ml/`, `16-llm/`) and write the code from scratch, using the tasks and hints in the module guide.

Modules 20–21 describe operational and permission drills; create your own `labs/20-operations/` and `labs/21-delivery/` with evidence after you run them. Module 22 is an independent project in a new domain, not another copy of the Olist reference.

## Rules

- Labs are **not** part of the default `pytest` run — they start red on purpose. Add each one to CI once it passes ([[Module 08 - Testing and CI]]).
- Make one honest attempt before opening the reference code in `src/`.
- Write expected values by hand before running anything; a green test you did not predict teaches little.
- Record every finished lab in [[Progress and Evidence]].

## How to work through a lab

1. Read the module guide section and the relevant theory notes.
2. Read the test file first: each test is a specification. Write down in one sentence what each test demands.
3. Implement one function at a time; run only its tests (`pytest labs/06-ingest -k validate -v`).
4. When everything is green, add one test of your own for a case the tests missed.
5. Rebuild the hardest function from an empty file a week later.
