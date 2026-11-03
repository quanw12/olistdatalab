# Design decisions

Short records of choices that an interviewer may ask about. Add one whenever you choose between
two reasonable options.

## 1. DuckDB locally, BigQuery in the cloud
DuckDB runs the full dataset on a laptop in seconds, needs no server and speaks the same SQL
dialect family as cloud warehouses. dbt models stay portable: switching adapter (`dbt-bigquery`)
is a profile change plus a few function names. Cost of the choice: one writer at a time, so the
DAG runs with `max_active_runs=1` and the stream consumer writes to its own file.

## 2. Bronze stores text, staging types it
Loading with type inference silently turns a bad value into NULL or fails the whole file.
Keeping text in bronze makes every value visible and every cast a testable step in dbt.

## 3. Contract checks before publishing, not after
A candidate table is checked and swapped in only if it passes. Downstream never reads a
half-good table, and yesterday's data stays available when today's file is broken.

## 4. Idempotency by file hash
Re-running the same current snapshot skips the DB load; bronze Parquet is re-exported so retry
repairs missing/stale outputs after a DB commit. Compare the input hash with the currently
published table, not any historical manifest row: A→B→A must publish A again.
A changed file is reloaded in full
(Olist is a snapshot, not a change feed). For a change feed you would switch to merge on key +
updated_at; see learning module 09 (dbt incremental).

## 5. Pre-aggregate before joining
Items and payments are summed per order before joining to orders, because joining two
one-to-many tables to the same parent multiplies rows. Verified by a reconciliation test.

## 6. At-least-once + idempotent sink for streaming
Exactly-once across Kafka and an external database is expensive. Committing offsets after the
write and deduplicating on a deterministic `event_id` gives the same result with simpler parts.

## 7. Time-based split for the ML model
A random split leaks the future into training. The model trains on older orders and is tested
on the newest 20%, the way it would be used.

## 8. LLM labels are cached and versioned
Labels are keyed by review/order, input SHA-256, prompt version, provider and model. Re-runs
reuse only the same configuration and content; changed text/model gets a new historical entry.
Legacy rows are migrated transactionally with an unknown-input marker and are not reused.
Evaluation excludes labels for old input and groups by model. Generation parameters/preprocessing
must be versioned too when changed; a model alias alone does not pin a hosted model revision.

## 9. Learning core before breadth

The course now integrates real data at module 09 and tests production failure modes before one
chosen specialization. `DEcourse/` is a standalone English Obsidian vault that holds every lesson; the repo holds only code. Modules 19–22 add
incremental/CDC, observability/recovery, security/delivery and an independent second project.
The reference snapshot DAG and bounded-lookback mart remain intentionally limited; course
instructions identify the missing interval/update/delete handling instead of claiming it exists.

## 10. Track dbt source models, ignore only root ML artifacts

The ignore rule `/models/` is anchored at the repository root. The old unanchored `models/`
also hid `dbt/models/`, so a clean clone missed the transformation source even though local
tests passed. dbt SQL/YAML source belongs in Git; generated ML binaries in root models do not.

## 11. Seller quality rates use seller/order grain

Item revenue is summed from item lines, but late-delivery and review averages give each
seller/order one vote. Aggregate item lines to seller/order before joining order-level
measures; otherwise multi-item orders overweight the rates. A singular dbt reconciliation
test checks these rates against distinct seller/order keys.
