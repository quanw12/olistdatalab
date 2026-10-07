# Help — Logging and observable failures

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Build the sanitized dictionary before invoking the logger.

</details>

<details>
<summary>Detailed approach</summary>

Start with {'event': event}. Loop through the three allowed field names and copy those present in details. Use details[key], not pop, to avoid mutation. Call logger.info(record). Your application can later choose a JSON formatter; this function's contract is about safe fields and a single emitted event.

</details>

<details>
<summary>Troubleshooting</summary>

Two logger calls indicate duplicated work. A token in the return value means your sanitizer copied the whole input. Returning the original details also violates the separate-object requirement.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.

</details>
