# Help — Data contracts, types and evolution

## First hint

Validate every field before deciding whether to return a record.

## Detailed approach

Create errors = [] and a separate canonical dict. For each ID, use isinstance(value, str) before strip. Parse each timestamp in a narrow try block; reject when parsed.utcoffset() is None. Use astimezone(timezone.utc).isoformat(). For integers, use type(value) is int. Append the field name once. If errors is nonempty return record None; otherwise return only the seven canonical fields. A missing key is the same field error as an invalid value.

## Troubleshooting

A broad except around the whole function can hide a programming bug. Reject True as an integer. Normalize offsets before comparing timestamp strings.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

