# AI02 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

"  Alpha  \r\n\r\n\r\n Beta  " → "Alpha\n\nBeta". "a  b" remains "a  b". A decomposed e + combining acute accent becomes NFC é. An all-blank string becomes empty.

## Reflection

1. Which representation do chunk offsets address?

2. Why is split() inappropriate for this contract?

<details>
<summary>After your reflection: compare the reasoning</summary>

Offsets address normalized Unicode text, not original UTF-8 bytes. split() discards all whitespace boundaries; splitting explicit LF and tracking empty lines retains paragraph structure. Deterministic normalization is idempotent.

</details>

</details>
