# CL05 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

read_raw+write_output returns 3 bindings; adding load_warehouse returns 5. Duplicating read_raw adds no binding. Unknown action raises ValueError. Live notes contain a sanitized allow/deny demonstration and each grant's scope.

## Reflection

1. Why is storage.objectCreator alone insufficient for replay verification?

2. Which account did your successful permission test actually use?

<details>
<summary>After your reflection: compare the reasoning</summary>

objectCreator creates output but does not read it to verify replay, so the course grants output viewer too. A permission check as the deployer is not evidence of runtime permissions. Always identify the account, action and resource scope.

</details>

</details>
