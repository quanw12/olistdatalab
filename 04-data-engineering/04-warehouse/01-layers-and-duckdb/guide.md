# DE12 — Warehouse layers and a local analytical engine

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE11](../../03-pipelines/04-observability-and-recovery/guide.md)

## Prerequisites and pace

DE08–DE10 and SQL windows; install the warehouse environment here.

**Core lesson.** Demonstrate the behavior before marking it complete. Use the difficulty and pace above.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Use [help.md](help.md) one hint at a time.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

In Windows PowerShell with the Engineering environment prepared:
~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check.py" DE12
~~~
The provided checker verifies stated fixture contracts; add at least one meaningful changed-input test.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/04-warehouse/01-layers-and-duckdb"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de12 layers-and-duckdb"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE13](../02-dbt-models/guide.md)
