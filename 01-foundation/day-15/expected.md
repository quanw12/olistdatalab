# Day 15 — Reliable HTTP extraction and bounded retries

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

| Scenario | Attempts | Pauses | Outcome |
|---|---:|---|---|
| valid200 | 1 | none | envelope |
| 503 then200 | 2 | 1s | envelope |
| 503 three times | 3 | 1s,2s | failure |
| 400 | 1 | none | failure |
| invalid JSON200 | 1 | none | failure |

429/Retry-After5 waits at least5 seconds. Retry-After120 stops under the30-second lab policy. Complete offline evidence is sufficient; live network success is optional.

</details>
