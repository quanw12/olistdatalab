# Help — dbt models, refs and dependency structure

## First hint

Models return their grain, not manual CREATE TABLE statements.

## Detailed approach

In Windows PowerShell:
~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\project\dbt"
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" debug --profiles-dir .
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" seed --profiles-dir .
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" build --profiles-dir . --select stg_changes latest_changes mart_customer
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" docs generate --profiles-dir .
~~~
Use ref('changes') for the seed and CAST(occurred_at AS TIMESTAMPTZ). Reuse DE12's selection idea. target/compiled has rendered SQL; target/manifest.json records dependencies. Close other connections to warehouse.duckdb before building.

Give casts explicit aliases, for example `CAST(version AS INTEGER) AS version`. Omitting AS before a keyword-like column name can produce a parser error. Check rendered SQL rather than changing the seed's contract to work around it.

After the completed models build, verify the actual fixture warehouse:
~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check_dbt.py"
~~~

## Troubleshooting

Comment-only models are unfinished. File-lock errors may mean your own reader remains open; stop it before retrying.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

