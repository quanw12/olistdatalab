# Help — Incremental transformations and correctness before pruning

## First hint

Keep tombstones in entity state; recompute small aggregates from current truth.

## Detailed approach

Run upstream models before current_incremental. Run dbt run --profiles-dir . --select current_incremental twice. Compare --full-refresh in a separate database/copy. Begin a copied seed with b1, append b2, reseed/build upstream then incremental. Use a single writer; source fixture version consistency is an assumption. Equal-version conflicts need upstream validation.

For the full supplied five-row fixture in the main lesson warehouse:
~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check_dbt.py" --incremental
~~~
Keep b1-only/mutated experiments in separate copies; this fixture checker intentionally expects the final full source state.

## Troubleshooting

Filtering deletes before latest selection resurrects B. Entirely removing an ID from source history differs from receiving a tombstone.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

