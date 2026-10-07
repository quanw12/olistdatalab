# ST07 — Learn

## Test the real boundary

A decoder test proves envelope handling. A live CDC demonstration additionally proves database capture, broker delivery, sink persistence and restart progress. Use the isolated PostgreSQL source/connector from live-lab.md, not your native course databases.

The source table has no business revision. In this one-partition lab, preserve source order through Kafka and apply accepted changes using position-ledger deduplication. Retain business delete state. Never compare numeric offsets across different partitions/topics or a recreated source stream.

## Syntax — SQL source changes

~~~sql
UPDATE stock SET units = 8 WHERE event_id = 'M1';
DELETE FROM stock WHERE event_id = 'M2';
INSERT INTO stock(event_id, sku, units) VALUES ('M3', 'p02', 5);
~~~
A crash after SQLite commit and before Kafka acknowledgement must replay safely. Record a stream epoch/configuration: deleting the topic/connector/source volume can invalidate its prior position history. This lab demonstrates consumer restart, not arbitrary lost-WAL/source disaster recovery.

[Assignment](exercise.md) · [Hints](help.md)
