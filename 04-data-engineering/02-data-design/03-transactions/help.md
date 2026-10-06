# Help — Transactions, upserts and checkpoint atomicity

## First hint

Find the exact point at which your database commit becomes authoritative.

## Detailed approach

Use your native PostgreSQL driver from the Python database lesson. Open a transaction context, validate a staged batch, compare equal versions, upsert valid records, then write ledger/progress. Raise the injected error inside that context. Query from a new connection after it exits, rather than mistaking uncommitted connection-local state for durability. Store batch identity plus a content hash; the same identity with different bytes must be rejected or versioned explicitly.

## Troubleshooting

A file export cannot share the PostgreSQL transaction. If export fails after commit, record publication pending and regenerate from committed state; do not pretend rollback reverted committed rows.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

