# ST05 — Assignment

Implement build_rejection(position,raw_bytes,reason). Validate ST04 position. raw_bytes must be bytes (not str/bytearray), size <=1048576; empty bytes are allowed. reason must be a stripped nonempty string <=120 characters with no newline/CR. Reject invalid input with ValueError. Return exactly topic, partition, offset, payload_sha, reason. No raw payload field. Do not mutate position.

Design a transactional quarantine/outbox table keyed by source position. Write a consumer policy: invalid JSON/contract → durable rejection then safe acknowledgement; transient database/broker/auth failures → stop/retry without advancing. Explain replay of the outbox publish separately.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
