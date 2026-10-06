# Help — Corrections, tombstones and deterministic replay

## First hint

Compare version before considering active/delete status.

## Detailed approach

Handle None first. Assert matching id, then compare integer version values. On an equality branch compare canonical dicts, not only amount. Return dict(winner) so downstream code cannot accidentally mutate the caller's dict. When aggregating, filter op == upsert only after all source versions have been resolved.

## Troubleshooting

updated_at can tie. Do not choose the last list element as truth without an explicit tie rule. A tombstone must survive even when its amount is zero.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

