# Fixed inputs

These are original small fixtures, with no live API or credentials.

## events.csv

A row is one source event assertion. event_id identifies an event; amount_cents contains 1–7 ASCII decimal digits representing a nonnegative integer up to 1000000. Leading zeros are allowed within that length. An identical repeated ID/amount is accepted but counted only once in the aggregate. Conflicting values for the same ID fail the complete run. Blank ID takes rejection priority over invalid amount.

Expected: input_rows 6, accepted_rows 4, rejected_rows 2, event_count 3, total_cents 3050. Rejected record numbers 6 (amount) and 7 (id), counting the header as record 1.

## runs.log

Six newline-terminated, simple space-delimited log records. INFO 3, WARN 1, ERROR 2. This is deliberately simple text, not a generic CSV/structured-log format.

Preserve these shared fixtures; create changed inputs in your native lab area. Full-input replay is deterministic. Accepted counts include duplicates; event_count and total count unique events.
