# Help — Cloud storage, IAM and cost-aware design

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Start from required actions rather than assigning a broad admin role.

</details>

<details>
<summary>Detailed approach</summary>

For each component list read/write/list/create needs and resource scope. Use synthetic data only. Estimate rows/bytes, query scans, run frequency and storage duration; do not invent a current price. Link the chosen platform's live pricing page and record date if you calculate real cost. Propose a maximum-bytes limit for paid on-demand queries and quotas where available, alongside alerts. Explain region/location compatibility.

</details>

<details>
<summary>Troubleshooting</summary>

A bucket path is not a database table. A local filesystem rename does not establish multi-object atomicity in a cloud store. Never claim a budget guarantees no charges.

</details>
