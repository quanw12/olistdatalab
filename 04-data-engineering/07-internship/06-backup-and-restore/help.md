# Help — Verified restore

Attempt the verification queries before opening hints.

<details>
<summary>Hint 1 — what must agree?</summary>

Could two databases have four item rows but different stock or deletion state?
Write the minimum comparison that would distinguish those cases.

</details>

<details>
<summary>Hint 2 — command failures</summary>

A custom archive belongs to pg_restore, not psql -f. Confirm source/target, client
version and port. Authentication errors require configuration repair, not SQL edits.
Keep the complete sanitized error; do not continue after a nonzero exit code.

</details>

<details>
<summary>Hint 3 — verify recovery meaning</summary>

Compare sorted item/ledger values as well as active aggregates. Check referential
integrity and prove constraints with attempted invalid writes, rolling back each.
The target should match the dump point; it should not contain the later source mutation.
Time verification too, and distinguish data-loss observation from an RPO objective.

</details>
