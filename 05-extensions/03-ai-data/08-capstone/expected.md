# AI08 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Checklist: b1 has four active docs; b2 has four active docs plus retained d-time tombstone; old cursor/timezone chunks absent; replay/stale inputs preserve current state; conflicting revision and injected failure leave state/index unchanged; lexical results attach provenance; metrics use versioned labels; unfamiliar document works; eight regressions pass; README reproduces the system. No generated answer is claimed correct from retrieval PASS alone.

## Reflection

1. Which write boundary prevents stale chunks?

2. What does your evaluation corpus fail to represent?

3. What evidence supports any real-model claim you make?

<details>
<summary>After your reflection: compare the reasoning</summary>

Atomic replacement of document state and derived chunks prevents obsolete text surviving an edit. A tiny synthetic corpus does not represent broad users/domains. Support real-model claims with actual model revision, corpus, preprocessing and measured query results.

</details>

</details>
