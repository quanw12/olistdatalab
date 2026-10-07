# LAB06 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — reject duplicate keys while indexing

Before assigning lookup[key], test whether key already exists; even identical categories do not make a duplicate key acceptable in this contract.

### Hint 2 — preserve the input row

Copy each row, add the looked-up category, append the copy. Do not replace its stored sku with the trimmed key.

### Hint 3 — measure the boundary

Use the provided workload unchanged for baseline and candidate. Run the checker before profiling. Explain which loop disappeared, not just a percentage.

[Return to the assignment](exercise.md)

</details>
