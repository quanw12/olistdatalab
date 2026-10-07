# Day 28 — Capstone architecture, contracts, and runbook

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Start by executing --help and listing actual module names; document those, not planned names. Copy only commands you have tested. The fixture CLI uses raw_batch.json for run and normalized weather_batch.json for load.

Draw the transaction boundary around staging/mart/checkpoint. Keep raw-file save and manifest publication outside it. Explain replay when the DB committed but the success manifest failed.

For native setup include Python version, environment, dependency installation, PG variables, database creation and SQL bootstrap. For Docker include external volume creation, db start, schema bootstrap and app command. A fresh machine needs both files and schema.

List evidence with labels such as 'unit tests, commit X' or 'local Docker fixture run'. Avoid a green CI badge until the workflow really ran. Write limitations from observed boundaries: no distributed locking, limited provider handling, fixed single-zone fixtures and no useful ML forecast yet.

</details>
