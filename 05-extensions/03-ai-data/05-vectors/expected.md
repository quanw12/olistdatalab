# AI05 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Query [1,0,0] against n1=[1,0,0], n2=[0.8,0.6,0], n3=[-1,0,0] yields scores 1,0.8,-1. Zero vectors, unequal dimensions, NaN, bool and duplicate IDs fail. Changed candidate order preserves ranking. Large finite [1e300,1e300] compares without NaN/infinity.

## Reflection

1. What does the fixture ranking prove?

2. Why can a relevant document have several returned chunks?

<details>
<summary>After your reflection: compare the reasoning</summary>

Fixture scores prove numeric validation, cosine/ranking behavior and deterministic ties. They do not prove a model understands meaning. Several chunks can refer to one document, so document-level evaluation must deduplicate appropriately.

</details>

</details>
