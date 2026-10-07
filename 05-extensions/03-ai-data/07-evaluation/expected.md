# AI07 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

got=[a,a,b,c], relevant=[b], k=2 → precision 0.5, recall 1.0, MRR 0.5. No hits → all 0.0. Duplicate relevant IDs do not inflate the denominator. Evaluation evidence clearly separates retrieval metrics from any answer-generation judgment.

## Reflection

1. Why deduplicate documents rather than chunks here?

2. What must change in evaluation when the corpus is edited?

<details>
<summary>After your reflection: compare the reasoning</summary>

This metric assesses unique relevant documents, so multiple chunks of one document count once. After edits/deletes, version the corpus and labels together. Retrieval metrics are separate from correctness of an answer generated from the evidence.

</details>

</details>
