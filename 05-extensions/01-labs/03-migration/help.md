# LAB03 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — inspect before changing

PRAGMA table_info(items) reveals the original columns. Count rows and sum units before applying your migration to a temporary copy.

### Hint 2 — choose an additive operation

Adapt the syntax example to items/zone/unknown. Leave item_id and units untouched.

### Hint 3 — verify compatibility

Query existing rows with zone; insert another row using only the old columns. Then try NULL inside a separate transaction and roll it back after the expected constraint error.

[Return to the assignment](exercise.md)

</details>
