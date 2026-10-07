# ST02 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate once at a shared boundary

Use one helper for the six-field contract; both public functions must reject invalid input. Do not normalize away a content conflict silently.

### Hint 2 — canonical bytes

Dictionary insertion order should not alter the serialized bytes. Exact sorted keys/compact separators let later ledgers compare stable content.

### Hint 3 — check completion

Poll while producing, flush with a timeout, then fail if delivery errors exist or messages remain. Save sanitized acknowledgement positions; do not call a consumer's sink complete here.

[Return to the assignment](exercise.md)

</details>
