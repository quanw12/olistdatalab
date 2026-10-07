# Help — Data-quality checks and fixed-clock freshness

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Use a fixed passed-in clock and independent counters.

</details>

<details>
<summary>Detailed approach</summary>

Parse updated_at, use timedelta(hours=max_age_hours), and compare aware datetimes. Future rows do not have positive stale ages, but explicitly count them. For amount validity use type(value) is int and value >= 0. Compute duplicate occurrences with total minus distinct IDs.

</details>

<details>
<summary>Troubleshooting</summary>

Failures that depend on today's date indicate an internal clock call. A boundary record marked stale means you used >= instead of >.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>
