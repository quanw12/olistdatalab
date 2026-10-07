# ST06 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — handle null before dictionary access

Unwrap payload if present, then test whether the resulting value is None. A null tombstone does not contain an op.

### Hint 2 — split upsert/delete validation

Deletes require only event_id. Never insist on before.units or invent a temperature/version/source timestamp for missing data.

### Hint 3 — preserve source evidence honestly

Keep a nullable integer LSN for audit. Ordering in the live one-partition stream uses actual topic/partition/offset plus the source contract, not an LSN-based invented revision.

[Return to the assignment](exercise.md)

</details>
