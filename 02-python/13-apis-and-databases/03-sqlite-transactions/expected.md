# Expected results — Parameterized SQL and transaction rollback

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Two new rows insert 2. Replaying them inserts 0. A batch with one new valid row followed by a negative amount raises IntegrityError and inserts neither.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Does the connection's with block close it?

<details>
<summary>Reveal reasoning after answering</summary>

No. It controls commit/rollback for the transaction. The connection owner must separately close the resource.

</details>

</details>
