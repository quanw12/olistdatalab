# Help — Point-in-time feature data and leakage

## First hint

Reconstruct state available then, not current truth now.

## Detailed approach

Parse timestamps with explicit awareness checks. Filter updated_at first, fold by id/version, then filter deletes and occurred_at. Aggregate integer cents by customer. At a cutoff before b2 arrived, use b1 values; final latest state alone cannot reconstruct it. Use chronological splits and fit learned transformations only on training data when modeling later.

## Troubleshooting

Filtering a current table by occurred_at keeps future-corrected amounts. Random train/test splits can mix future records into training on temporal tasks.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

