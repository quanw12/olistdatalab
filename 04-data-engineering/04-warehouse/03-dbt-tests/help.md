# Help — dbt data tests and transformation evidence

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Return evidence of violations rather than a row saying pass.

</details>

<details>
<summary>Detailed approach</summary>

Compute expected and actual totals in CTEs; return rows WHERE totals or counts differ. COALESCE empty sums. accepted_values uses arguments: then values: ['upsert','delete']. Put singular SELECT tests under project/dbt/tests. Run dbt test --profiles-dir . --select latest_changes mart_customer, or dbt build for dependency-aware execution. Keep tests out of the source-input acquisition.

</details>

<details>
<summary>Troubleshooting</summary>

A SELECT returning one zero-valued row still fails a data test. A SQL syntax failure does not demonstrate the intended semantic assertion.

</details>
