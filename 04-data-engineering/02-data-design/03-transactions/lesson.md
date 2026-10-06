# Transactions, upserts and checkpoint atomicity

## Understand it

A transaction groups database changes into one commit or rollback. Upsert handles key conflicts under a specified policy; it does not automatically choose the right source version. Store source progress with state changes in the same transaction so a failed batch cannot skip data on retry. This lab assumes one writer. Concurrency and isolation anomalies need additional design.

## Syntax and trace

~~~sql
BEGIN;
INSERT INTO demo_state (id, version, amount_cents)
VALUES ('sample', 2, 1200)
ON CONFLICT (id) DO UPDATE
SET version = EXCLUDED.version,
    amount_cents = EXCLUDED.amount_cents
WHERE EXCLUDED.version > demo_state.version;
-- Update the batch ledger/checkpoint here, then COMMIT.
ROLLBACK;
~~~

EXCLUDED names the attempted row. The WHERE predicate prevents an older version overwriting a newer row. Equal-version conflicting content must be checked separately. This snippet rolls back intentionally.

## Engineering connection

An apparently successful checkpoint can permanently lose records if data changes were not committed.

[Reference](https://www.postgresql.org/docs/18/sql-insert.html). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

