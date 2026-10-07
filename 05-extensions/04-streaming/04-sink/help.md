# ST04 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — check transport replay first

Inside a transaction, read the position ledger and compare digest. Do not confuse an existing business ID with an existing Kafka position.

### Hint 2 — compare the complete business state

At equal version, sku/time/units/op differences are a conflict. A higher delete becomes the stored state; an older upsert cannot revive it.

### Hint 3 — inject after both writes

Raise just before commit to verify both state and ledger roll back. After a successful return the caller may commit the Kafka offset; a crash before that will replay harmlessly.

[Return to the assignment](exercise.md)

</details>
