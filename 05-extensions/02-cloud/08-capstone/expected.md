# CL08 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Live checklist: b1 active total 10; b2 current rows 3, active rows 2, total 13; identical replay changes no final result; conflicting replay fails; injected publication failure can recover; job exit/log evidence is truthful; actual runtime allows required actions and denies raw overwrite; query bound demonstrated; schedule paused; cleanup plan owned. Local-only work is a valid learning artifact but not a deployed cloud capstone.

## Reflection

1. Which durable identifier resolved a lost response?

2. What happens if MERGE commits but publication fails?

3. Which behavior would change with multiple concurrent writers?

<details>
<summary>After your reflection: compare the reasoning</summary>

Load request IDs and immutable manifest/content identities support recovery. After a successful MERGE but failed publication, preserve checked state and resume publication; report delivery is still incomplete. Concurrent writers require a durable concurrency design beyond this sequential lab.

</details>

</details>
