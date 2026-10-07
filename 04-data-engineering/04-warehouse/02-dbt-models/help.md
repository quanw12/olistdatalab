# Help — dbt models, refs and dependency structure

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Models return their grain, not manual CREATE TABLE statements.

</details>

<details>
<summary>Detailed approach</summary>

In Windows PowerShell:
Run commands are in the guide's Command reference.
Use ref('changes') for the seed and CAST(occurred_at AS TIMESTAMPTZ). Reuse DE12's selection idea. target/compiled has rendered SQL; target/manifest.json records dependencies. Close other connections to warehouse.duckdb before building.

Give casts explicit aliases, for example `CAST(version AS INTEGER) AS version`. Omitting AS before a keyword-like column name can produce a parser error. Check rendered SQL rather than changing the seed's contract to work around it.

After the completed models build, verify the actual fixture warehouse:
Run commands are in the guide's Command reference.

</details>

<details>
<summary>Troubleshooting</summary>

Comment-only models are unfinished. File-lock errors may mean your own reader remains open; stop it before retrying.

</details>
