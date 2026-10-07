# Help — A complete retail pipeline portfolio

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Get one end-to-end fixture working, then add failure proof.

</details>

<details>
<summary>Detailed approach</summary>

Follow the capstone acceptance contract in [project/capstone/contract.md](../../project/capstone/contract.md). Implement small stages using ideas learned earlier; reuse your own library code instead of pasting orchestration copies. Verify row counts at each boundary. Keep runtime output ignored. Another person should be able to start from the README without guessing secrets, paths or commands.

</details>

<details>
<summary>Troubleshooting</summary>

Do not claim one atomic transaction across PostgreSQL, files and DuckDB. A mock database check does not replace live rollback proof. Avoid adding Kafka/Kubernetes for tiny fixtures.

</details>
