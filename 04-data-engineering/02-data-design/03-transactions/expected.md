# Expected — DE06

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Failed batch leaves rows, ledger and cursor unchanged. A retry changes state once. Replaying b1 after b2 does not restore deleted B or replace A version 2. Post-commit export failure can be repaired from committed state.

## Reflection answer

<details>
<summary>Open after answering</summary>

No. Database and filesystem publication are separate boundaries; use explicit publication state and recovery or a transactional outbox pattern.

</details>

Passing a supplied fixture is one piece of evidence. Explain the result and show one changed-input or failure example before marking the lesson complete.

</details>
