# LAB05 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate without changing data

Use type(delta) is int, not isinstance. Check connection.in_transaction before BEGIN. The checker creates a clean connection and initialized tables.

### Hint 2 — check identity inside the transaction

Read ledger with a bound batch_id. Compare hashes before updating any item. If no ledger exists, fetch each current stock and apply its delta; inspect missing rows explicitly.

### Hint 3 — place the crash correctly

Inject after execute() has changed the Nth item but before commit(). A rollback should restore the first update as well. Test from a fresh SELECT, then retry without injection.

[Return to the assignment](exercise.md)

</details>
