# Day 23 — Data quality and deterministic freshness checks

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

With base 8, as-of2026-09-19T03:00:00+00:00 and threshold 2h: Hanoi fresh age 1h; HCMC fresh age 1h; Da Nang stale age 22h; Hue missing. Structural/duplicate/orphan checks pass, but completeness/freshness fails and CLI exits2. After next, with the SAME 03:00 UTC clock: Da Nang is fresh age 1h; Hanoi is future-dated because its newest observation is05:00 UTC; HCMC remains fresh age 1h; Hue remains missing. This verifies future-time detection. Other timestamps must be evaluated from actual data, not hardcoded expectations.

</details>
