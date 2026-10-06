# Help — A complete retail pipeline portfolio

## First hint

Get one end-to-end fixture working, then add failure proof.

## Detailed approach

Follow the capstone acceptance contract in [project/capstone/contract.md](../../project/capstone/contract.md). Implement small stages using ideas learned earlier; reuse your own library code instead of pasting orchestration copies. Verify row counts at each boundary. Keep runtime output ignored. Another person should be able to start from the README without guessing secrets, paths or commands.

## Troubleshooting

Do not claim one atomic transaction across PostgreSQL, files and DuckDB. A mock database check does not replace live rollback proof. Avoid adding Kafka/Kubernetes for tiny fixtures.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

