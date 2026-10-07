# ST04 — Assignment

Implement apply_event(conn,event,position,fail_before_commit=False). Event contract is ST02. position is exactly {topic:nonempty str,partition:exact nonnegative int,offset:exact nonnegative int}. fail_before_commit must be bool. Schema is in schema.sql; conn has no active transaction and remains open.

Use canonical event SHA256 from ST02 bytes. Existing identical position → {"status":"replay"}; changed bytes at that position → ValueError. For a new position, compare entity_state by event_id: no state/higher version → apply full six-field state including tombstone, status applied; older → stale; equal identical → replay; equal differing → ValueError. Record every new accepted position even if stale or a logical replay. Data/state/ledger writes share a transaction. Inject RuntimeError immediately before commit when requested; roll everything back. Malformed data/active connection/contract conflict → ValueError.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
