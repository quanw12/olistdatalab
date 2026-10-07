# Expected results — Parquet and explicit storage schemas

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

A 105-cent record round-trips unchanged with an int64 amount column. Empty rows return [] and retain all four stored columns.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why preserve the schema when there are no rows?

<details>
<summary>Reveal reasoning after answering</summary>

Readers still need field names/types, and later nonempty batches must use a compatible structure.

</details>

</details>
