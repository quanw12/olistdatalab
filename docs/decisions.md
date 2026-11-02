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
Re-running the pipeline with the same files does nothing. A changed file is reloaded in full
(Olist is a snapshot, not a change feed). For a change feed you would switch to merge on key +
updated_at; see learning module 05.

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
Labels are keyed by review, prompt version and provider. Re-runs cost nothing, and a new prompt
is a new version that can be compared with the old one on the same reviews.
