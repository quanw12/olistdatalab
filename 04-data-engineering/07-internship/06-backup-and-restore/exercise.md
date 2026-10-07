# DE28 assignment

Demonstrate a verified logical restore using only two new disposable lab databases.
Do not use any previous course/project database.

1. Run bootstrap.sql on the source. Write checks.sql to capture complete item
   key/value/version/deletion state, ledger state, active stock units, orphan count
   and relevant constraints. Keep a sanitized baseline in notes.md.
2. Dump the source and inspect the custom archive's table/data/constraint entries.
3. Run after-backup.sql on the source **after** the dump. Record which committed
   changes this dump cannot recover.
4. Restore to the empty target. Require a successful exit code, then use your checks
   to compare the target with the baseline, not the changed current source.
5. In separate disposable transactions, prove duplicate-key, negative-unit and
   orphan-batch writes fail. Roll back each attempt. Repeat the successful report check.
6. Write recovery.md: tools/versions, exact owned source/target, dump point, measured
   restore-plus-verification duration, observed data loss, access-policy limits,
   and what a real RPO/RTO objective would require. Do not claim PITR.

## Deliver

checks.sql, recovery.md and sanitized notes.md. Keep dumps/logs in output/ outside
commits. A setup script is supplied infrastructure, not your completed verification.

## Independent variation

In a separate new lab pair, add one valid baseline item with different units before
the dump. Predict and verify the restored key set and stock total. Your queries
must discover it without hard-coded fixture totals.
