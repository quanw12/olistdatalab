# Hints for DE01

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Write a sentence beginning “The consumer needs one row per …”. Follow one ID through both batches instead of counting every incoming version as a sale.

</details>

<details>
<summary>Build the explanation</summary>

Use a table with Stage / Input grain / Output grain / Key / Failure / Evidence. Raw input contains changes. Latest state represents one highest-version row per ID, including tombstones. A serving total uses the relevant active state, grouped at the agreed consumer grain.

Sort each ID's versions on paper. A later update can change an earlier business day's result. A deleted ID still needs a version marker so an older upsert cannot resurrect it. Ask whether the source retains changes long enough for your recovery window.

Do not invent a latency target. Put your lab assumption in the document, then say who would confirm it for a real project. Use volume, delay, source guarantees and operational constraints to justify a tool choice.

If the amounts do not reconcile, list active IDs and their individual amounts before aggregating. If time fields look interchangeable, write the event and extraction timeline separately.

</details>
