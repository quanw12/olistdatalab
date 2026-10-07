# Help — Data contracts, types and evolution

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Validate every field before deciding whether to return a record.

</details>

<details>
<summary>Detailed approach</summary>

Create errors = [] and a separate canonical dict. For each ID, use isinstance(value, str) before strip. Parse each timestamp in a narrow try block; reject when parsed.utcoffset() is None. Use astimezone(timezone.utc).isoformat(). For integers, use type(value) is int. Append the field name once. If errors is nonempty return record None; otherwise return only the seven canonical fields. A missing key is the same field error as an invalid value.

</details>

<details>
<summary>Troubleshooting</summary>

A broad except around the whole function can hide a programming bug. Reject True as an integer. Normalize offsets before comparing timestamp strings.

</details>
