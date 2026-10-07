# ST03 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

p0: offsets 3 processed,4 failed,5 processed → commit 4. p1: 0 processed,1 processed → commit 2. Delivered processed offsets 3 and 7 with no failed record → commit 8. Shuffling input does not alter output. A first failed record yields no commit.

## Reflection

1. Why is replay safer than silently skipping a failed sink write?

2. Why must offsets never be compared across partitions?

<details>
<summary>After your reflection: compare the reasoning</summary>

Replay after an uncertain acknowledgement can be safely deduplicated; skipped uncommitted sink work is lost data. Offsets identify positions within their own topic/partition, so cross-partition numerical comparison has no ordering meaning.

</details>

</details>
