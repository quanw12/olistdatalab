# LAB01 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — inspect row multiplication

Temporarily select m.event_id, m.units and a.audit_id before aggregation. M1 appears twice.

### Hint 2 — choose the correct source

The requested report needs products and movements. Audit rows are not facts in this metric; remove their influence or aggregate them before a later join.

### Hint 3 — preserve empty products

Start from products, LEFT JOIN the movement facts, group by product_id, count the non-null movement key and handle a NULL sum. ORDER BY makes the comparison deterministic.

[Return to the assignment](exercise.md)

</details>
