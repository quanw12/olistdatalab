# AI log

How I use AI assistants on this project. Each entry: what I asked → what was right or wrong →
how I verified it (a test that failed before the fix, a count on the real data, a doc page).
Interviewers ask about this; a log of caught mistakes is stronger evidence than "I use AI".

---

## 2026-11-02 · Repository restructured with an AI assistant

**Asked:** turn my scattered lesson folders into one portfolio project and a study path.
**Got:** the platform skeleton in this repo, tested end to end on a synthetic sample.
**Bugs caught while verifying (by running the code):**
- `ingest_table` crashed when called on its own because the audit tables were only created by
  `ingest_all` → moved table creation into `ingest_table`; covered by `test_ingest.py`.
- A DuckDB file named `stream.duckdb` made the schema name `stream` ambiguous → schema renamed
  to `live`; covered by `test_streaming.py`.
- MLflow 3 refuses the old `./mlruns` file store → switched to its SQLite backend.
**My follow-up:** I must be able to explain every file before I list it on my CV. Each module guide in
the DEcourse vault ends with a checklist; I tick it only after rebuilding the part myself.

---

<!-- Template
## YYYY-MM-DD · title
**Asked:**
**What went wrong / right:**
**How I checked:**
**Lesson:**
-->

## 2026-11-03 · Course revision and DEcourse vault

**Asked:** improve the course for product work, create a separate Obsidian reference called
DEcourse with syntax/applications/examples/review, then commit and push.

**Changed:** core + one elective route, real-data integration from dbt, modules 19–22 for
incremental/CDC, observability/recovery, security/delivery and independent transfer project.
Vault notes contain worked examples, pitfalls and recall exercises; learner
progress/evidence starts unchecked. Lab 19 intentionally starts red and is excluded from
the reference test suite until the learner solves it.

**Reference issues reproduced and fixed:**
- Historical hash membership skipped snapshot A after A→B→A; now compare current lineage.
- DB commit could leave missing/stale bronze Parquet; skipped DB loads now re-export local output.
- Labels ignored review content/model changes; cache identity includes input hash and model,
  with transactional legacy migration and evaluation of current content only.
- Unanchored `models/` ignored dbt source; root ML artifacts stay ignored via `/models/`,
  while dbt SQL/YAML source is now included for clean checkouts.
- Seller quality rates were item-weighted; pre-aggregate seller/order before averaging and
  verify with a deterministic multi-item fixture plus a dbt singular test.

**Verification approach:** reference pytest/ruff, vault links and explicitly runnable Python/SQL
examples, isolated sample batch + keyword labelling/evaluation, and a source-only checkout
without ignored local data. These checks do not claim broker/cloud/hosted-LLM execution or
learner completion; real-data findings remain for the learner to measure.

## 2026-11-03 · Vault becomes the single home for lessons, in English

**Asked:** separate lessons from the code repo, expand the thin theory, translate everything to English.

**Changed:** `learning/` and the lab instructions moved into `DEcourse/` as module guides and a
Labs Guide; folders and notes renamed to English; every theory note rewritten as a full lesson
(goals, concepts, runnable examples, Olist application, pitfalls, exercises, folded answers).
`scripts/check_course.py` now also rejects Vietnamese text and links from the vault into the repo.

**How I checked:** `python scripts/check_course.py` executes every runnable Python/SQL example.
