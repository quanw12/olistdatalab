# Help — Incremental transformations and correctness before pruning

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Keep tombstones in entity state; recompute small aggregates from current truth.

</details>

<details>
<summary>Detailed approach</summary>

Run upstream models before current_incremental. Run dbt run --profiles-dir . --select current_incremental twice. Compare --full-refresh in a separate database/copy. Begin a copied seed with b1, append b2, reseed/build upstream then incremental. Use a single writer; source fixture version consistency is an assumption. Equal-version conflicts need upstream validation.

For the full supplied five-row fixture in the main lesson warehouse:
Run commands are in the guide's Command reference.
Keep b1-only/mutated experiments in separate copies; this fixture checker intentionally expects the final full source state.

</details>

<details>
<summary>Troubleshooting</summary>

Filtering deletes before latest selection resurrects B. Entirely removing an ID from source history differs from receiving a tombstone.

</details>
