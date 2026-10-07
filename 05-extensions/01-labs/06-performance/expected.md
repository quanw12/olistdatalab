# LAB06 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

A row {"sku":" p01 ","units":7} becomes {"sku":" p01 ","units":7,"category":"hardware"}. Unknown SKU yields None. Output order/input fields survive. Duplicate dimension SKUs after trimming raise ValueError. Submit measured times and correctness evidence; the checker has no timing assertion.

## Reflection

1. What tradeoff does the lookup make in memory?

2. Why can two identical dimension rows still be a contract violation?

<details>
<summary>After your reflection: compare the reasoning</summary>

A lookup adds O(D) memory to avoid repeatedly scanning the dimension. Duplicate keys violate the unique dimension contract even when the current values match; silently choosing one hides upstream ambiguity.

</details>

</details>
