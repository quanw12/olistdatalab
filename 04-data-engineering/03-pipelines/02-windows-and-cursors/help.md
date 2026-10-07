# Help — Event time, extraction cursors and backfills

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Parse times before sorting; textual offsets are not chronological order.

</details>

<details>
<summary>Detailed approach</summary>

Use datetime.fromisoformat and reject utcoffset None. A key function returns (parsed_updated_at, record['id']). Select before limiting. For page_after compare tuple keys > cursor_key. A date range uses >= start and < end. Persist the last committed pair only after the corresponding data transaction succeeds. A backfill should reconcile to full state, including correction and delete rules from DE08.

</details>

<details>
<summary>Troubleshooting</summary>

Using >= cursor can repeatedly return the last row; using only > timestamp can skip its ties. A max occurred_at cursor misses C's late arrival.

</details>
