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
**My follow-up:** I must be able to explain every file before I list it on my CV. Each module in
`learning/` ends with a checklist; I tick it only after rebuilding the part myself.

---

<!-- Template
## YYYY-MM-DD · title
**Asked:**
**What went wrong / right:**
**How I checked:**
**Lesson:**
-->
