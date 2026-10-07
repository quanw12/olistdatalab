# LAB07 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate every event, including old attempts

Keep a (stage, attempt) → status map to detect conflicts. A newer success does not excuse contradictory old evidence.

### Hint 2 — reduce to final attempts

Maintain a separate stage → latest event map. Update only when the attempt number increases.

### Hint 3 — classify after reduction

Compute failed/missing lists, then apply the documented precedence. Do not return early just because an older failure appears.

[Return to the assignment](exercise.md)

</details>
