# CL03 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

{"tasks":1,"max_retries":1,"timeout_seconds":120,"memory_mib":512} passes unchanged as a copy. tasks=2 and max_retries=True fail. Live evidence: one successful execution, one intentional failure, exit/log context and configured limits. No HTTP port/server is required.

## Reflection

1. When could a retry repeat a write?

2. Which job artifacts must live outside its filesystem?

<details>
<summary>After your reflection: compare the reasoning</summary>

Retry can repeat any external write completed before failure. Raw inputs, batch identity, request evidence and published outputs must outlive the container filesystem. A zero exit status belongs after required work is complete.

</details>

</details>
