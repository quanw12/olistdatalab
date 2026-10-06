# DE08 — Corrections, tombstones and deterministic replay

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE07](../../02-data-design/04-query-plans/guide.md)

## Prerequisites and pace

DE04–DE06; Python dictionaries and tests.

**Core lesson.** Demonstrate the behavior before marking it complete. Budget 2–4 hours; integrations may need more than one session.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Use [help.md](help.md) one hint at a time.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

In Windows PowerShell with the Engineering environment prepared:
~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check.py" DE08
~~~
The provided checker verifies stated fixture contracts; add at least one meaningful changed-input test.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/03-pipelines/01-corrections-and-deletes"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de08 corrections-and-deletes"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE09](../02-windows-and-cursors/guide.md)
