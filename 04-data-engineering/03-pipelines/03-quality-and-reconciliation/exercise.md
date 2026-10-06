# DE10 assignment

Implement quality_report(records, now, max_age_hours). Input records are canonical active current records; now is aware ISO string, threshold a nonnegative finite number excluding bool. Return exactly {'duplicate_ids': extra occurrences beyond one per id, 'negative_amounts': number of rows amount_cents<0, 'stale_rows': rows with now-updated_at strictly greater than threshold, 'future_rows': rows updated_at>now}. Raise ValueError for naive clocks/timestamps or invalid threshold. Count each check independently. Then write SQL tests for orphan customer IDs and source-active versus mart totals; freshness of an empty dataset must be handled separately as missing-data policy.

## Deliverables

exercise.py, quality.sql, notes.md with a fixed-clock failing example.

## Reflection

Can valid values plus zero duplicate IDs prove revenue is correct?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

