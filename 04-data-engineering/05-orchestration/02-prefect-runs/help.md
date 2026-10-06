# Help — Prefect runs, retry ownership and backfill rehearsal

## First hint

One controlled retry owner and one writer.

## Detailed approach

Import flow/task/get_run_logger; log during execution, not module import. Set cache_policy=None for side effects and retries=0 for the transactional loader/inner-retrying extractor. Keep fail-once state only in the toy demo. Permanent failures must raise. Inspect retry_condition_fn when classifying transient failures. A deployment still needs its chosen runner/server/worker arrangement; record what's actually running.

## Troubleshooting

Catching an error and returning None may look successful. Cached results can conceal a rerun you intended to execute.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

