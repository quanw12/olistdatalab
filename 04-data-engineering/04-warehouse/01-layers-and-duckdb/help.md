# Help — Warehouse layers and a local analytical engine

## First hint

Window the complete history before filtering active rows.

## Detailed approach

Use ROW_NUMBER() OVER (PARTITION BY id ORDER BY version DESC) in a CTE, then rn = 1. Return only seven specified columns and no hard-coded IDs. Preserve TIMESTAMPTZ values. A later mart filters op = 'upsert'. Detect equal-version conflict upstream rather than choosing arbitrary ties.

## Troubleshooting

Filtering deletes early resurrects B. COUNT(*) over raw counts changes, not active orders.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

