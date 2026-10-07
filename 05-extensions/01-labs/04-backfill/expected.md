# LAB04 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

For 2024-02-28T00:00:00+00:00 → 2024-03-03T00:00:00+00:00, chunk_days=3:

1. [Feb 28, Mar 2)
2. [Mar 2, Mar 3)

No final day is lost. A +07:00 timestamp at local 07:00 normalizes to UTC midnight and is allowed; local 00:00+07:00 does not meet this lab boundary. chunk_days=True fails.

## Reflection

1. Why is an exclusive end useful when concatenating windows?

2. What extra policy is needed for local calendar-day backfills?

<details>
<summary>After your reflection: compare the reasoning</summary>

Exclusive ends make adjacent windows share a boundary without double-counting it. Local calendar-day backfills additionally need an explicit timezone/DST policy; a UTC-day planner does not establish that policy.

</details>

</details>
