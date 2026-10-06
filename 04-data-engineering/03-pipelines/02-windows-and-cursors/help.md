# Help — Event time, extraction cursors and backfills

## First hint

Parse times before sorting; textual offsets are not chronological order.

## Detailed approach

Use datetime.fromisoformat and reject utcoffset None. A key function returns (parsed_updated_at, record['id']). Select before limiting. For page_after compare tuple keys > cursor_key. A date range uses >= start and < end. Persist the last committed pair only after the corresponding data transaction succeeds. A backfill should reconcile to full state, including correction and delete rules from DE08.

## Troubleshooting

Using >= cursor can repeatedly return the last row; using only > timestamp can skip its ties. A max occurred_at cursor misses C's late arrival.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

