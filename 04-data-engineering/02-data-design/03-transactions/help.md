# Help — Transactions, upserts and checkpoint atomicity

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Find the exact point at which your database commit becomes authoritative.

</details>

<details>
<summary>Detailed approach</summary>

Use your native PostgreSQL driver from the Python database lesson. Open a transaction context, validate a staged batch, compare equal versions, upsert valid records, then write ledger/progress. Raise the injected error inside that context. Query from a new connection after it exits, rather than mistaking uncommitted connection-local state for durability. Store batch identity plus a content hash; the same identity with different bytes must be rejected or versioned explicitly.

</details>

<details>
<summary>Troubleshooting</summary>

A file export cannot share the PostgreSQL transaction. If export fails after commit, record publication pending and regenerate from committed state; do not pretend rollback reverted committed rows.

</details>
