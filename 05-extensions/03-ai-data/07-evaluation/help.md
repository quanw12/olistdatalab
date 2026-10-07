# AI07 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — deduplicate before slicing

If [a,a,b] and k=2, the document ranking is [a,b], not [a]. Do not count two chunks of a as two relevant documents.

### Hint 2 — compute ranks from one

Use enumerate(top_k, start=1) for the first hit. Handle zero relevant documents before dividing.

### Hint 3 — freeze the evaluation inputs

Save corpus version, index configuration, queries and labels with the metrics. A better score on one tiny corpus is not a universal semantic-quality claim.

[Return to the assignment](exercise.md)

</details>
