# LAB03 — Assignment

Write migration.sql with a single ALTER TABLE statement against items(item_id TEXT PRIMARY KEY, units INTEGER NOT NULL CHECK(units >= 0)). Add zone TEXT NOT NULL DEFAULT 'unknown'. Preserve all rows, keys and units. A CHECK rejecting blank zones is a useful optional extension, not required by the checker.

Write a deployment note covering old-writer compatibility, validation before/after and recovery before/after commit. Demonstrate an insert omitting zone and one explicitly passing NULL. Never run this against a previous course database.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.


## Required deployment evidence

The ALTER statement is a short syntax exercise. The applied task is the migration
decision: run it in a disposable lab database with existing rows, show their values
before/after, and prove old-writer omission versus explicit NULL behavior.
Rehearse a failure before commit and explain why rollback cannot undo a committed
migration. A checker pass without this evidence is only the syntax portion.
