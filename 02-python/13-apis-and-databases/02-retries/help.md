# Help — Retry only transient failures

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Count total attempts, including the first call.

</details>

<details>
<summary>Detailed approach</summary>

Use for attempt in range(max_attempts). On TimeoutError, if attempt == max_attempts-1 use bare raise; otherwise sleep(2**attempt). Return immediately from the successful call. Do not catch Exception or swallow failures into None.

</details>

<details>
<summary>Troubleshooting</summary>

Four calls with max_attempts=3 is an off-by-one error. A final sleep wastes time because no call follows. Retrying ValueError violates the contract.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>
