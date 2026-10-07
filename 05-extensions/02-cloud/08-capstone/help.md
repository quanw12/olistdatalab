# CL08 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — build in slices

First local batch/quality checks, then storage, then one manual job, then warehouse, then publication. Diagnose a single boundary at a time.

### Hint 2 — represent uncertain requests

Persist a load request identity and retrieve an existing job on recovery. Check manifest bytes before treating input as a replay. A successfully merged state with no report is pending publication, not completed delivery.

### Hint 3 — keep claims honest

Record execution IDs, counts, active units, replay and failure recovery. Explain single-writer assumptions and cross-service transaction limits in the handoff.

[Return to the assignment](exercise.md)

</details>
