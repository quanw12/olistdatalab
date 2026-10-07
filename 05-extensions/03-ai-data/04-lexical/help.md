# AI04 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — use the table name in FTS expressions

FTS5 MATCH/bm25 expect the virtual table, not an arbitrary text column alias. Read the syntax example.

### Hint 2 — deterministic results

ORDER BY score ASC, chunk_id ASC prevents equal-score results from varying. Bind a limit through the database API.

### Hint 3 — interpret the result

Search cursor, timezone and an absent word. A zero-hit result is valid evidence of a retrieval miss, not permission to invent an answer.

[Return to the assignment](exercise.md)

</details>
