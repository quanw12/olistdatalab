# Help — Source discovery

Attempt first and record the highest hint used.

<details>
<summary>Hint 1 — measurement versus decision</summary>

Can you count repeated rows without deciding which to publish? Trace one proposed
key on a two-row example and state exactly what duplicate excess means.

</details>

<details>
<summary>Hint 2 — syntax pointers</summary>

DictReader exposes its header and can use None for extra/missing cells. A tuple
of stripped fields is hashable. fromisoformat alone does not require an offset.
The lesson lists the APIs; use its references for a specific syntax question.

</details>

<details>
<summary>Hint 3 — isolate a failing measurement</summary>

Check one column/key on three manually counted rows. Inspect stripped values and
the definition of duplicate excess. Counters are independent; do not stop measuring
a row after its first defect or select a latest row while profiling.

</details>
