# Help — Cloud storage, IAM and cost-aware design

## First hint

Start from required actions rather than assigning a broad admin role.

## Detailed approach

For each component list read/write/list/create needs and resource scope. Use synthetic data only. Estimate rows/bytes, query scans, run frequency and storage duration; do not invent a current price. Link the chosen platform's live pricing page and record date if you calculate real cost. Propose a maximum-bytes limit for paid on-demand queries and quotas where available, alongside alerts. Explain region/location compatibility.

## Troubleshooting

A bucket path is not a database table. A local filesystem rename does not establish multi-object atomicity in a cloud store. Never claim a budget guarantees no charges.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

