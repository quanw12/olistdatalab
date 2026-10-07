# Help — Metric definitions and honest analytics

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Separate arithmetic evidence from causal explanations.

</details>

<details>
<summary>Detailed approach</summary>

Show the two changes: A +200, B -1500, C +800, net -500. Define whether c2 remains in a customer table with zero versus omitted from active-only mart. If computing a rate, write numerator and denominator first. Label cents/currency clearly; divide by 100 only for presentation. The tiny synthetic sample cannot establish seasonality or customer behavior.

</details>

<details>
<summary>Troubleshooting</summary>

A LEFT JOIN COUNT(*) can give one for a zero-order customer; count a non-null order key. Never silently fill an unknown monetary amount with zero.

</details>
