# LAB07 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

extract failed/1, extract succeeded/2, and load/quality/publish succeeded/1 → status succeeded, retry_count 1, no failed/missing stages. Removing publish → incomplete with missing_stages ["publish"]. A failed latest load → failed, even when publish is absent. Shuffling logs changes no result.

## Reflection

1. Why is ERROR-line counting misleading?

2. What changes if attempts can skip numbers?

<details>
<summary>After your reflection: compare the reasoning</summary>

A failed earlier attempt can be superseded by a successful retry. Determine the latest terminal attempt per stage. max_attempt-1 represents retry count only under the stated sequential-attempt assumption; skipped numbers need explicit attempt evidence.

</details>

</details>
