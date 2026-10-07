# LAB03 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

The checker starts with 3 rows and 15 units. Those rows/units survive and each zone is unknown. An old-style insert receives unknown; an explicit NULL zone raises an integrity error; an explicit non-null zone works. Your notes distinguish rollback of an open transaction from recovery after commit.

## Reflection

1. Does a DEFAULT override an explicitly supplied NULL?

2. How would you evaluate this migration on native PostgreSQL?

<details>
<summary>After your reflection: compare the reasoning</summary>

A default applies when an insert omits the column; explicit NULL still violates NOT NULL. On PostgreSQL test the actual DDL/locks, old/new writers, constraints and recovery on an owned copy before deployment. A committed change is not undone by issuing ROLLBACK later.

</details>

</details>
