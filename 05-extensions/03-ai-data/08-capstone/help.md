# AI08 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — deliver lexical search first

Use one SQLite file with metadata/state and FTS tables. Validate documents before beginning writes, then replace derived rows atomically.

### Hint 2 — turn edits into regressions

Search cursor/timezone before b2, then after b2. Inspect the index directly to ensure old text is removed; a top-k change alone is not proof of deletion.

### Hint 3 — add model work only after reliability

Reuse verified chunk IDs/provenance with real embeddings. Evaluate the same labeled corpus and report which queries improved or regressed. Keep optional answer generation separate from required pipeline checks.

[Return to the assignment](exercise.md)

</details>
