# AI08 — Assignment

Implement app.py commands ingest, search and evaluate, with an output/ database path. Use b1/b2 from documents.json and lessons AI01–AI07. Ingest b1 → four active docs; ingest b2 updates d-api, deletes d-time and adds d-types → four active docs. Old cursor/timezone text must disappear. Retain tombstones, source metadata and content digests.

Implement identical replay, stale revisions, conflicting same revisions and crash-before-commit cases. Search returns cited chunk/provenance records; evaluation saves corpus/index configuration and labels. Write at least eight regressions. Add one unfamiliar document and query without changing code. Optional real embeddings must follow embedding-lab.md; fixture vectors alone cannot support semantic-quality claims.

Deliver README, contract, runbook, evaluation report and a short English demonstration. A paid LLM, vector server or framework is not required.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
