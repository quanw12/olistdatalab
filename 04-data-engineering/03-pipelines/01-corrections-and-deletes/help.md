# Help — Corrections, tombstones and deterministic replay

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Compare version before considering active/delete status.

</details>

<details>
<summary>Detailed approach</summary>

Handle None first. Assert matching id, then compare integer version values. On an equality branch compare canonical dicts, not only amount. Return dict(winner) so downstream code cannot accidentally mutate the caller's dict. When aggregating, filter op == upsert only after all source versions have been resolved.

</details>

<details>
<summary>Troubleshooting</summary>

updated_at can tie. Do not choose the last list element as truth without an explicit tie rule. A tombstone must survive even when its amount is zero.

</details>
