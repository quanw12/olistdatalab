# AI05 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — normalize stably

Validate each vector before arithmetic. Scale components by the largest absolute component before computing a norm; this also handles a finite vector whose unscaled norm would overflow. math.hypot computes the norm of the scaled vector. Normalize before dot products. Clamp only a tiny numerical overshoot, not negative similarity.

### Hint 2 — rank explicit records

Collect each validated cosine score, then sort by (-score, chunk_id). Check duplicates before ranking.

### Hint 3 — separate the evidence

One report covers algorithm contracts. A second optional report covers real downloaded model revision, resource use, corpus labels and retrieval results.

[Return to the assignment](exercise.md)

</details>
