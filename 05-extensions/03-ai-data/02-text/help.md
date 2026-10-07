# AI02 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — work on lines

Normalize Unicode/newline forms, then strip each line individually. Track whether the preceding retained line was empty.

### Hint 2 — retain one paragraph separator

Skip an empty line only when a retained empty line already precedes it. Join the retained lines with LF and strip the final string.

### Hint 3 — verify idempotence

Assert normalize_text(normalize_text(x)) == normalize_text(x). Compare the internal spaces and paragraph boundary, not only total length.

[Return to the assignment](exercise.md)

</details>
