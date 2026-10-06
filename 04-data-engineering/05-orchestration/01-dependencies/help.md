# Help — Dependency graphs, parameters and run boundaries

## First hint

Ready means prerequisites satisfied, not just a smaller name.

## Detailed approach

Copy prerequisite sets; validate names exist. Repeatedly sort currently ready tasks and choose the first, then mark completed. If tasks remain but none are ready, raise a cycle error. In the real pipeline, quality failure blocks publish. Keep cursor commit in the loader's transaction.

## Troubleshooting

Insertion order is not execution order. A cycle must raise rather than hang.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

