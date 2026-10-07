# Expected results — Native PostgreSQL with Psycopg

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Offline: values are bound separately in one transaction/cursor. Live: initial A=100, newer correction A=150, older replay A=100 leaves 150. A failing two-row batch inserts neither row.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why distinguish a fake connection check from an integration check?

<details>
<summary>Reveal reasoning after answering</summary>

A fake can confirm calls and parameter separation while accepting syntactically invalid SQL. Only the real server tests SQL semantics, constraints and transactional behavior.

</details>

</details>
