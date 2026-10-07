# CL02 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

object_key("b-001", "changes.jsonl") → "raw/b-001/changes.jsonl". "../x", "folder/x.json", "x.txt" and True fail. Live completion additionally records one generation and an existing-key collision; offline PASS alone is not an upload.

## Reflection

1. Why is a new timestamp a bad replay identity?

2. What must be compared when the object already exists?

<details>
<summary>After your reflection: compare the reasoning</summary>

A new clock-based ID on retry loses the relationship to the original batch. An existing object needs content/manifest verification, including its digest/generation; a failed create-only request by itself does not prove identical content.

</details>

</details>
