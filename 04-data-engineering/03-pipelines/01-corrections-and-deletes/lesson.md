# Corrections, tombstones and deterministic replay

## Understand it

Source changes describe versions of an entity, not always new entities. Choose the authoritative version, keep deletions as tombstones, and derive active rows after version selection. Removing tombstones too early allows stale data to resurrect an entity. Event time groups business activity; source version orders revisions. A version number is useful only under an explicit producer guarantee.

## Syntax and trace

~~~python
current = {"id": "sample", "version": 2, "op": "delete"}
incoming = {"id": "sample", "version": 1, "op": "upsert"}
print(incoming["version"] > current["version"])
~~~

False means the stale upsert must not override the tombstone. Filtering delete before comparing revisions would lose this protection.

## Engineering connection

Replay safety comes from stable keys and update rules, not from a scheduler's retry setting.

Original practice contract; review [sources.md](../../sources.md) for context.

