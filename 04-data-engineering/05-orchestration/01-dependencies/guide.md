# DE16 — Dependency graphs, parameters and run boundaries

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE15](../../04-warehouse/04-incremental-models/guide.md)

## Prerequisites and pace

DE11–DE15; Python collections/functions.

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
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check.py" DE16
~~~
The provided checker verifies stated fixture contracts; add at least one meaningful changed-input test.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/05-orchestration/01-dependencies"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de16 dependencies"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE17](../02-prefect-runs/guide.md)


## Independent variation

Use an unknown dependency and a cycle. Fail explicitly rather than returning a partial valid-looking ordering.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
