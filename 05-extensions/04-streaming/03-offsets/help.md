# ST03 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate duplicate evidence

Use a position key (topic,partition,offset). Detect conflicting statuses before reducing a partition.

### Hint 2 — stop at the first failure

For each sorted partition group, update last_safe for processed statuses and break on failed. If its first delivered record failed, produce no commit for that partition.

### Hint 3 — remember next-offset semantics

Return last_safe + 1. A replay after a crash between sink commit and this Kafka commit is expected and handled in ST04.

[Return to the assignment](exercise.md)

</details>
