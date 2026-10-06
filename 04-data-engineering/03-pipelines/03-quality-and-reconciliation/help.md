# Help — Quality checks, reconciliation and fixed-clock freshness

## First hint

A result of zero stale rows does not prove an empty feed is healthy.

## Detailed approach

Keep a seen set and count repeated IDs after the first. Parse aware updated timestamps. Use total_seconds for age and strict > for staleness. A future row can be an error even though it is not stale. SQL anti-joins must show orphan rows rather than hiding them in an INNER JOIN. Reconcile unique active source rows to fact rows and exact integer total.

## Troubleshooting

A GROUP BY can accidentally conceal duplicates. Be clear whether your count describes affected keys or extra rows; this contract counts extras.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

