# ST04 — Learn

## Two identities serve different purposes

Kafka position identifies a delivered record. event_id/version identifies a business revision. A transport replay should not apply twice; a later transport position may carry the same business revision or an older revision. Persist transport ledger and business state in the same database transaction.

## Syntax — SQLite

~~~sql
CREATE TABLE message_ledger (
  topic TEXT NOT NULL, partition_id INTEGER NOT NULL, offset_id INTEGER NOT NULL,
  payload_sha TEXT NOT NULL, PRIMARY KEY(topic, partition_id, offset_id)
);
~~~
The primary key prevents two ledger rows for one position. It does not make the Kafka commit and SQLite commit a single transaction. This lab uses at-least-once delivery plus an idempotent sink. Do not claim distributed exactly-once semantics.

Business deletes retain highest-version tombstones. Review LAB05 transaction ownership and DE08 correction/conflict rules.

[Assignment](exercise.md) · [Hints](help.md)
