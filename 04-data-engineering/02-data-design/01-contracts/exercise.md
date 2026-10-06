# DE04 assignment

Implement validate_change(raw) in exercise.py. Input is a dict requiring id, customer_id, occurred_at, updated_at, version, amount_cents, op. Ignore additional keys. IDs must be nonblank strings and are trimmed. Times must be ISO strings with an explicit offset; normalize to UTC ISO strings using +00:00. version is an exact int >=1; amount_cents is an exact int from 0 to 1000000; op is exactly upsert or delete. Return {'record': canonical seven-field dict or None, 'errors': list of invalid field names in the order above}. Collect all field errors; do not mutate input. No chronological relation between the two time fields is imposed. Write contract.md covering compatible additions, incompatible unit/key changes and quarantine versus batch failure.

## Deliverables

exercise.py, contract.md, notes.md and a boundary test.

## Reflection

Why can an unchanged SQL type still represent a breaking contract change?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

