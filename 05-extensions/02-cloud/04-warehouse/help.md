# CL04 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — rank inside a CTE

Add a row number to history in a CTE, then select rank 1 in the outer query. Explicitly list the six output columns so helper rank does not leak.

### Hint 2 — validate before MERGE

Group by event_id/version and check whether differing normalized payloads exist. Deduplicate identical repeats, then reduce to one source row per ID.

### Hint 3 — reason about crashes

If load succeeded but the client lost its response, retrieve the existing job by its durable ID. If report publication failed after MERGE, regenerate the report from checked current state; do not invent a successful publish marker.

[Return to the assignment](exercise.md)

</details>
