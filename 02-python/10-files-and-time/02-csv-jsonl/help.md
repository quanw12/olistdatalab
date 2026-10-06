# Help — CSV, JSON, JSON Lines, and schema boundaries

## First hint

Inspect DictReader.fieldnames before iterating. Extra values appear under a None key; missing cells get None values.

## Detailed approach

Compare both len(fieldnames) and set(fieldnames) to detect duplicated names. For each row reject None in row keys or values. Do not strip values yet. For JSONL, open once with 'w' and write json.dumps(row, ensure_ascii=False, allow_nan=False) followed by '\n'.

## Troubleshooting

A city containing a comma breaks manual splitting. Single quotes in output indicate you used str(row). Reusing append mode duplicates output on rerun.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.
