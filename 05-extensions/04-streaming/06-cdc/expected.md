# ST06 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

data/cdc.json yields upsert M1/7, upsert M1/8, delete M2 with row=None, then a transport tombstone. A PK-only before delete passes. Unknown op or units=True fails. Input/wrapped payload remains unchanged.

## Reflection

1. Why may before contain only the key on delete?

2. Why is a transport tombstone not another business deletion?

3. Why cannot LSN be treated as a universal business version?

<details>
<summary>After your reflection: compare the reasoning</summary>

Default PostgreSQL replica identity may provide only primary-key information for delete. A null transport tombstone is separate from the preceding business delete envelope. LSN is source-position evidence, not a universal unique business version.

</details>

</details>
