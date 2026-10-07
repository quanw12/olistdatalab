# Expected results — pandas joins, types, and trustworthy totals

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Hanoi=1000, Hue=2050, Da Nang=0 map to central=2050 and north=1000. Missing/duplicate dimension keys fail.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why validate cardinality before aggregation?

<details>
<summary>Reveal reasoning after answering</summary>

A many-to-many accident duplicates fact values; grouping afterward can hide the duplication behind plausible totals.

</details>

</details>
