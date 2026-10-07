# Expected results — Capstone: reproducible retail ingestion

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Base fixture: input_rows=8, accepted_rows=4, rejected_rows=4, stored_rows=3, total_cents=3050. Next fixture: input_rows=3, accepted_rows=3, rejected_rows=0, stored_rows=4, total_cents=3850. Replaying either file preserves the latest stored state. See contract.md for files and failure cases.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why rebuild output after recognizing a previously successful batch?

<details>
<summary>Reveal reasoning after answering</summary>

The database may have committed before filesystem publication failed. Skipping ingestion prevents duplicate changes, but skipping artifact generation would leave the run unrecoverable.

</details>

</details>
