# DE06 assignment

In engineering_lab, implement a parameterized loader for supplied batches using your DE05 schema. Detect same-id/same-version conflicts before the upsert. Apply a batch and its ledger/progress in one transaction. Add an injectable exception after the first row and before commit. Show unchanged state and progress on failure, successful retry, replay, and stale-version protection. Do not interpolate source values into SQL. Keep database credentials in environment variables.

## Deliverables

loader.py, test_loader.py and notes.md with actual before/after queries and a single-writer assumption.

## Reflection

Can a database rollback undo a JSON file already written outside the transaction?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

