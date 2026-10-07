# Help — Warehouse layers and a local analytical engine

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Window the complete history before filtering active rows.

</details>

<details>
<summary>Detailed approach</summary>

Use ROW_NUMBER() OVER (PARTITION BY id ORDER BY version DESC) in a CTE, then rn = 1. Return only seven specified columns and no hard-coded IDs. Preserve TIMESTAMPTZ values. A later mart filters op = 'upsert'. Detect equal-version conflict upstream rather than choosing arbitrary ties.

</details>

<details>
<summary>Troubleshooting</summary>

Filtering deletes early resurrects B. COUNT(*) over raw counts changes, not active orders.

</details>
