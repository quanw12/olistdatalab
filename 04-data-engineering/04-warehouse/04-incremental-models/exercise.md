# DE15 assignment

Create project/dbt/models/current_incremental.sql using this adapter-supported strategy. Consume authoritative latest_changes including tombstones, initially scanning all latest rows. In a new lab copy/database, compare full and incremental state after b1, b2, replay and stale upsert. Explain why appended daily totals are wrong for corrections/deletes.

## Deliverables

Model and experiment.md with row-by-row equality and limits.

## Reflection

Why is an appended daily amount wrong after a correction?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

