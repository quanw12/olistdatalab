# Expected results — Data-quality checks and fixed-clock freshness

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

With now=2026-10-02T00:00Z: a record exactly 24 hours old is fresh; 25 hours old is stale; one hour ahead is future. Empty input yields zero for every metric.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why distinguish duplicate occurrences from duplicate key groups?

<details>
<summary>Reveal reasoning after answering</summary>

Three rows with the same ID have two duplicate occurrences but one duplicated key group. Different definitions produce different counts and decisions.

</details>

</details>
