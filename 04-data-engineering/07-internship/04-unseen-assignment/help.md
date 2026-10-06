# Help — An independent take-home and debugging rehearsal

## First hint

Do a three-record example manually before building the CLI.

## Detailed approach

If the independent attempt stalls, stop the timed diagnostic and label it guided practice. Solve one stage at a time: parse/validate, version fold, aggregate, publish. Build a tiny expected map by hand. Show that shuffling valid consistent changes preserves final state. The expected.md result is for post-attempt reconciliation; keep it closed until the attempt ends.

## Troubleshooting

A delivered event later cancelled is not final delivered weight. Printing a correct supplied total without processing a changed input is not evidence.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

