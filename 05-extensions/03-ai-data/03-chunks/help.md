# AI03 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate progress

size-overlap must be positive, otherwise the loop cannot advance. Reject bool for integer arguments.

### Hint 2 — build the final chunk once

After appending a chunk, test whether it already reaches len(text) before moving the cursor.

### Hint 3 — reconstruct boundaries

For each result assert text[start:end] equals the stored chunk text. Check that the final end equals the full text length and adjacent starts follow the documented overlap.

[Return to the assignment](exercise.md)

</details>
