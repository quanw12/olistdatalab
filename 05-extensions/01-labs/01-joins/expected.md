# LAB01 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

| product_id | total_units | event_count |
|---|---:|---:|
| p01 | 10 | 2 |
| p02 | 5 | 1 |
| p03 | 0 | 0 |

Total units across products: 15. Adding another audit changes none of these values. Adding a p03 movement of 7 units makes p03 7/1. Record both a reproduction and the corrected changed-input result.

## Reflection

1. Why does SUM(DISTINCT units) lose valid movements?

2. Which key defines the report grain?

<details>
<summary>After your reflection: compare the reasoning</summary>

SUM(DISTINCT units) merges two different movements that happen to have the same numeric value. The movement event_id defines a fact; product_id defines the report group. Audit rows have a different grain and cannot multiply movement facts.

</details>

</details>
