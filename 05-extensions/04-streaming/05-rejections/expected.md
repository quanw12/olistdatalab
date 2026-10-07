# ST05 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

For one position and b"bad", the digest is stable and the returned record contains no payload bytes. Malformed position, string payload, oversized bytes or newline reason fails. Your policy distinguishes malformed data from a temporarily unavailable sink.

## Reflection

1. When may a source offset advance after invalid data?

2. Why can a DLQ publish be repeated?

<details>
<summary>After your reflection: compare the reasoning</summary>

Advance after invalid data only once its durable rejection/outbox is committed according to policy. DLQ publication can repeat after uncertain acknowledgement, so it needs an identity/deduplication policy. Environment outages should not be disguised as poison payloads.

</details>

</details>
