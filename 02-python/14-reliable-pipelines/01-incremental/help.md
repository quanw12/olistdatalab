# Help — Incremental state, replays, and corrections

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Map order_id to a copied record, then compare one incoming row with the current winner.

</details>

<details>
<summary>Detailed approach</summary>

Use a state dictionary, copy accepted records with dict(row), and return sorted keys. On an equal timestamp compare the entire clean record. Reject a conflict before committing any persistent state in the later capstone. Canonical time is a prerequisite, not something to guess inside this function.

</details>

<details>
<summary>Troubleshooting</summary>

Using >= overwrites equal-version conflicts. Unconditionally assigning by key lets older data win. Modifying a dictionary from existing leaks changes back to the caller.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>
