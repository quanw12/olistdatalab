# CL03 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate the key set

Compare set(config) to the four required names before reading values; return dict(config), not the original mapping.

### Hint 2 — preserve errors at the process boundary

Catch an exception only to add useful context, then return a failing exit status or re-raise. Do not print success in finally.

### Hint 3 — compare local/cloud configuration

Use the same batch ID and input contract. Confirm task count, retries and timeout explicitly; do not assume defaults. Save the actual execution result.

[Return to the assignment](exercise.md)

</details>
