# Expected results — Aware time, UTC, and deterministic clocks

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

08:00+07:00 becomes 01:00.000000+00:00; 01:00Z maps to the same string. Fraction .123456 is retained. A naive datetime, a date-only string and impossible date fail.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why use a passed-in now for freshness tests?

<details>
<summary>Reveal the reasoning after answering</summary>

It makes the boundary repeatable. The same fixture and clock yield the same age; tests do not unexpectedly fail tomorrow.

</details>

</details>
