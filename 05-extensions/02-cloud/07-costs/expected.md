# CL07 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

allow_query(100,100)=True; allow_query(101,100)=False; (-1,100), (True,100) fail. Live notes include estimated and actual bytes, an intentionally refused query and a cleanup inventory. No claim of a complete spending hard cap.

## Reflection

1. Which costs are outside maximum_bytes_billed?

2. Why can SELECT ... LIMIT 10 still scan substantial data?

<details>
<summary>After your reflection: compare the reasoning</summary>

The query byte limit does not cap storage, container jobs, builds or total billing. LIMIT bounds returned rows, not necessarily scanned input. Record estimated and actual bytes plus the relevant billing mode.

</details>

</details>
