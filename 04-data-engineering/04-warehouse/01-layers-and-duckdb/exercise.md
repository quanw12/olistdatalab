# DE12 assignment

Implement query.sql as one DuckDB SELECT returning id,customer_id,occurred_at,updated_at,version,amount_cents,op for latest per id from raw_changes. Use source version; keep tombstones. The typed fixture guarantees no equal-version conflicts. The checker uses a temporary warehouse and also introduces a newer changed record. Write layers.md with layer responsibilities and provenance.

## Deliverables

query.sql, layers.md and notes.md with an early-delete counterexample.

## Reflection

Why retain raw history after producing a mart?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

