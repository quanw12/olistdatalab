# DE07 assignment

Use a disposable table in engineering_lab. Generate 50000 synthetic rows with generate_series, a deterministic timestamp distribution and a primary key. Compare a selective timestamp-range query before/after an index, using ANALYZE after loading. Record plans and three timed repetitions. Compare a broad range too. Keep correctness checks identical. Write why each index is or is not justified; do not promise a speedup.

## Deliverables

benchmark.sql, plans.md and notes.md with table/index sizes and measurement conditions.

## Reflection

Why is an index unused on a broad scan not necessarily a bug?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

