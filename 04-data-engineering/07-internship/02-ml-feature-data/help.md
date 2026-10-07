# Help — Point-in-time feature data and leakage

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Reconstruct state available then, not current truth now.

</details>

<details>
<summary>Detailed approach</summary>

Parse timestamps with explicit awareness checks. Filter updated_at first, fold by id/version, then filter deletes and occurred_at. Aggregate integer cents by customer. At a cutoff before b2 arrived, use b1 values; final latest state alone cannot reconstruct it. Use chronological splits and fit learned transformations only on training data when modeling later.

</details>

<details>
<summary>Troubleshooting</summary>

Filtering a current table by occurred_at keeps future-corrected amounts. Random train/test splits can mix future records into training on temporal tasks.

</details>
