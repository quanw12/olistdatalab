# AI06 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

d-api v1 chunks [a,b] → v2 chunks [c] removes [a,b], adds [c], stores v2. v3 delete removes [c], adds [], stores a tombstone. A later v2 replay cannot resurrect it. Same-version changed digest fails. Input dictionaries/lists remain unchanged.

## Reflection

1. Why is a digest needed if chunk IDs already include version?

2. What recovery problem arises with a separate remote index?

<details>
<summary>After your reflection: compare the reasoning</summary>

Equal boundaries/IDs can hide changed text or metadata at the same revision; compare a canonical content digest too. If state and remote index commit separately, a failure can leave inconsistent search rows; use a durable outbox/reconciliation design or one local atomic boundary.

</details>

</details>
