# Incremental state, replays, and corrections

Original Python-for-DE extension. [Source reference](https://www.postgresql.org/docs/18/sql-insert.html).

## Concept and purpose

A batch can contain new records, repeats or corrections. A stable business key identifies the entity; a source version determines which snapshot is newer. Request time is not a substitute for source version.

Idempotency means repeating the same operation preserves the intended final state. It does not mean ignoring every duplicate key: that would also discard valid corrections. Compare versions and define equal-version behavior.

Our contract uses canonical UTC ISO text with identical microsecond precision, making string order match time order for these values. Without normalization, parse timestamps before comparing them. Equal versions with different contents indicate a source conflict; abort rather than choose an arbitrary winner.

A watermark records progress, but a strict timestamp > watermark filter can miss late arrivals and ties. Overlap windows plus deduplication, a compound cursor, or source-specific change tracking may be needed. A backfill processes earlier data deliberately and still follows the same winner rules.

This in-memory exercise models latest state. Persisting progress and state atomically is part of the capstone.

## Syntax example

~~~python
old={"order_id":"A","amount_cents":100,"updated_at":"2026-10-01T01:00:00.000000+00:00"}
new=dict(old,amount_cents=150,updated_at="2026-10-02T01:00:00.000000+00:00")
print(new["updated_at"]>old["updated_at"])
~~~

## Trace

The normalized newer version compares greater. An older replay must not reverse the correction.

## DE connection

Real pipelines are rerun and receive delayed data; correctness must survive both.

Use [exercise.py](exercise.py) for the exact input/output contract.
