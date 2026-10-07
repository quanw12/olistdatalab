# ST07 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — create the source before the connector

The init SQL creates a publication and snapshot rows. Register the connector only after source/broker readiness. Inspect task status, not just the registration response.

### Hint 2 — distinguish business state from position

Deduplicate (topic,partition,offset) in a ledger. Same entity has several positions; apply them in the single partition's delivered order. A previously processed position must not reapply after restart.

### Hint 3 — place the crash between commits

Commit SQLite, terminate before calling consumer.commit(), then restart. Inspect final state from a fresh connection and compare the ledger before/after. Preserve volumes for this restart test.

[Return to the assignment](exercise.md)

</details>
