# ST04 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

b1+b2 yields M1 v2=8, M2 v2 delete=0, M3 v1=5: active total 13. Same position replay changes nothing. New position with identical business revision adds a ledger row without changing state. Stale revisions cannot resurrect M2. Injection leaves both tables as before the call.

## Reflection

1. Why persist stale accepted records in the transport ledger?

2. Which transaction boundary remains outside this function?

<details>
<summary>After your reflection: compare the reasoning</summary>

A stale accepted event still occupies a real transport position and can be safely acknowledged once ledgered. SQLite commit and Kafka offset commit remain separate; a crash between them is handled through replay. Tombstones protect highest business revisions.

</details>

</details>
