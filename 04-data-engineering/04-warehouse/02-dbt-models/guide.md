# DE13 — dbt models, refs and dependency structure

**Difficulty: Integrate.** 2–6 hours across several sessions. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE12](../01-layers-and-duckdb/guide.md)

## Prerequisites and pace

DE12 and the warehouse environment.

**Core lesson.** Demonstrate the behavior before marking it complete. Use the difficulty and pace above.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Use [help.md](help.md) one hint at a time.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

Record the real commands, outputs and limits in notes.md. Expected observations are criteria, not a claim that an author ran your environment.


## Command reference

Use these after implementing the relevant task. Environment setup is linked above;
commands do not supply model/flow logic. Inspect each exit code before continuing.

~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\project\dbt"
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" debug --profiles-dir .
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" seed --profiles-dir .
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" build --profiles-dir . --select stg_changes latest_changes mart_customer
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" docs generate --profiles-dir .
~~~

~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check_dbt.py"
~~~

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/04-warehouse/02-dbt-models" "04-data-engineering/project/dbt"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de13 dbt-models"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE14](../03-dbt-tests/guide.md)
