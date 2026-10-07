# ST07 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Snapshot active total 10. After source changes: M1=8,M3=5 active, M2 retained as deleted; active total 13. Restart after the injected crash preserves state and processes remaining input. Record actual positions, connector status and ledger evidence; message count can vary due to null tombstones/metadata, so do not hard-code a fixed total count.

## Reflection

1. What durable data makes consumer restart safe?

2. Which recovery does this lab not demonstrate?

<details>
<summary>After your reflection: compare the reasoning</summary>

The position ledger, current state and retained source epoch/configuration make a consumer restart safe. The lab does not establish recovery after destroyed source volumes, lost WAL or arbitrary topic recreation; that needs a new recovery policy.

</details>

</details>
