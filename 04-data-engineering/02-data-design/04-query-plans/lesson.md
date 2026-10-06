# Query plans, indexes and measured optimization

## Understand it

A plan describes how the database intends to execute a query. Estimated rows, actual rows, filtering and join choices help diagnose cardinality errors and bottlenecks. An index has write/storage cost and helps particular access patterns; a tiny table may sensibly use a sequential scan. EXPLAIN ANALYZE executes the statement, so use SELECT in this lesson.

## Syntax and trace

~~~sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT id, updated_at
FROM current_changes
WHERE updated_at >= TIMESTAMPTZ '2026-09-01T00:00:00+00'
  AND updated_at < TIMESTAMPTZ '2026-09-02T00:00:00+00';
~~~

The half-open filter avoids double-counting midnight. Record actual row count and buffers alongside duration; a single elapsed-time sample is noisy.

## Engineering connection

Learn to justify an optimization rather than adding every possible index.

[Reference](https://www.postgresql.org/docs/18/using-explain.html). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

