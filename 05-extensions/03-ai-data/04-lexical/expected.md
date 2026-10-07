# AI04 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

With the b1 corpus, cursor returns d-api; timezone returns d-time; an absent token returns no rows. query/limit remain bound parameters. Record the SQLite version and confirm FTS5 is available; the checker creates an isolated index.

## Reflection

1. Why does a lower SQLite BM25 score sort first?

2. Which input grammar is still present after SQL parameterization?

<details>
<summary>After your reflection: compare the reasoning</summary>

SQLite FTS5 transforms BM25 for ascending better-match order. SQL bound parameters avoid SQL interpolation, but MATCH still parses FTS query syntax. A CLI must define how it accepts or escapes search expressions.

</details>

</details>
