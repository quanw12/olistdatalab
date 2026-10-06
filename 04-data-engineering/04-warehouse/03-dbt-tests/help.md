# Help — dbt data tests and transformation evidence

## First hint

Return evidence of violations rather than a row saying pass.

## Detailed approach

Compute expected and actual totals in CTEs; return rows WHERE totals or counts differ. COALESCE empty sums. accepted_values uses arguments: then values: ['upsert','delete']. Put singular SELECT tests under project/dbt/tests. Run dbt test --profiles-dir . --select latest_changes mart_customer, or dbt build for dependency-aware execution. Keep tests out of the source-input acquisition.

## Troubleshooting

A SELECT returning one zero-valued row still fails a data test. A SQL syntax failure does not demonstrate the intended semantic assertion.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

