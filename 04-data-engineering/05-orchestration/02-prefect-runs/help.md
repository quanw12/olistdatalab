# Help — Prefect runs, retry ownership and backfill rehearsal

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

One controlled retry owner and one writer.

</details>

<details>
<summary>Detailed approach</summary>

Import flow/task/get_run_logger; log during execution, not module import. Set cache_policy=None for side effects and retries=0 for the transactional loader/inner-retrying extractor. Keep fail-once state only in the toy demo. Permanent failures must raise. Inspect retry_condition_fn when classifying transient failures. A deployment still needs its chosen runner/server/worker arrangement; record what's actually running.

</details>

<details>
<summary>Troubleshooting</summary>

Catching an error and returning None may look successful. Cached results can conceal a rerun you intended to execute.

</details>
