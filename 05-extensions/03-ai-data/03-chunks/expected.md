# AI03 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

"abcdefghij", size=4, overlap=1 → [0,4) "abcd", [3,7) "defg", [6,10) "ghij". IDs contain the document/revision/bounds. A text of length 4 produces one chunk, not two. size=overlap fails.

## Reflection

1. Why must a document revision be part of chunk identity?

2. What differs between characters, UTF-8 bytes and model tokens?

<details>
<summary>After your reflection: compare the reasoning</summary>

Revision in chunk identity supports replacement/audit; it does not detect a conflicting payload reused at the same revision without content checks. Unicode code points, encoded bytes and tokenizer tokens have different lengths/boundaries.

</details>

</details>
