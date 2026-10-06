# Day 17 — Incremental loads, corrections, and backfills


## Idempotency includes values

Repeating an idempotent operation preserves the intended final state. A unique key prevents duplicate identities but does not stop an old record from undoing a new correction.

For this lab, requested_at acts as an ingestion-version timestamp. Update only if the incoming request is newer. Equal version and equal values is a no-op; equal version with conflicting values is a visible conflict. Real providers may have a more authoritative revision field: request time is our teaching simplification.

Conditional UPSERT on an unrelated table:

~~~sql
INSERT INTO example_prices AS target (sku, price, received_at)
VALUES (%s, %s, %s)
ON CONFLICT (sku) DO UPDATE
SET price = EXCLUDED.price, received_at = EXCLUDED.received_at
WHERE EXCLUDED.received_at > target.received_at;
~~~

## Watermarks and late arrivals

A watermark records progress. Strictly reading timestamps greater than it can miss late input. Re-read an overlap and let key/version rules handle repeats. An overlap assumes bounded lateness; it cannot guarantee capture of arbitrarily late records.

Use one state row for the single fixture stream. Select records with requested_at >= watermark minus one day. No existing watermark means read all. Advance to max(old watermark, accepted candidate request times). Commit staging, mart and checkpoint in the same transaction. Never advance before the load succeeds.

timedelta(days=1) is a duration. Compare aware datetimes, not timestamp strings containing different offsets. A full refresh of this tiny mart remains acceptable.

## Backfill is explicit replay

A backfill processes a chosen historical interval. The current-weather API cannot retrieve arbitrary history by inventing start/end parameters. This lab replays saved raw files by local observation date, with start inclusive and end exclusive.

Backfill bypasses incremental candidate filtering, uses the same validation/upsert policy, and does not advance the normal ingestion checkpoint. It repairs records beyond the overlap without changing what a current API endpoint means.

Read: [ON CONFLICT](https://www.postgresql.org/docs/18/sql-insert.html), [datetime](https://docs.python.org/3.13/library/datetime.html), [isolation](https://www.postgresql.org/docs/18/transaction-iso.html). Concurrency beyond one runner is outside today's scope.
