# CL04 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

b1: 2 current rows, active units 10. b1+b2: 3 current rows; M1 v2=8, M2 v2 delete=0, M3 v1=5; 2 active rows and total 13. Replay preserves this result. The GoogleSQL implementation needs live load/MERGE evidence separately.

## Reflection

1. Why retain a tombstone in current?

2. Which uncertain failure can a deterministic load job ID resolve?

<details>
<summary>After your reflection: compare the reasoning</summary>

A retained highest-version tombstone prevents an older upsert from reappearing. A deterministic load job ID lets you inspect an already-submitted request after losing its response; it does not merge storage/load/report publication into one transaction.

</details>

</details>
