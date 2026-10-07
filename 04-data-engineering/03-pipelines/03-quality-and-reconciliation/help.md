# Help — Quality checks, reconciliation and fixed-clock freshness

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

A result of zero stale rows does not prove an empty feed is healthy.

</details>

<details>
<summary>Detailed approach</summary>

Keep a seen set and count repeated IDs after the first. Parse aware updated timestamps. Use total_seconds for age and strict > for staleness. A future row can be an error even though it is not stale. SQL anti-joins must show orphan rows rather than hiding them in an INNER JOIN. Reconcile unique active source rows to fact rows and exact integer total.

</details>

<details>
<summary>Troubleshooting</summary>

A GROUP BY can accidentally conceal duplicates. Be clear whether your count describes affected keys or extra rows; this contract counts extras.

</details>
