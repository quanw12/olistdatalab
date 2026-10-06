# Help — An optional BigQuery sandbox lab

## First hint

Read the sandbox notice and capabilities before selecting a lab operation.

## Detailed approach

Create a dedicated learning project/dataset rather than using an existing work project. Load a tiny local CSV through the UI, inspect types, then run SELECT with project.dataset.table fully qualified. Confirm integer cents and row count; do not treat cents as currency units. Save local evidence because the sandbox table expires. Cleanup only resources you created; do not delete a shared project.

## Troubleshooting

If the page asks you to upgrade/enable billing, pause the lab and use the local alternative. Storage quota behavior and expiry can differ from assumptions in older tutorials.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

