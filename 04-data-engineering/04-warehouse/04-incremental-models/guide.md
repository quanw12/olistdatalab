# DE15 — Incremental transformations and correctness before pruning

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE14](../03-dbt-tests/guide.md)

## Prerequisites and pace

DE13–DE14 and DE08–DE09.

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
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check_dbt.py" --incremental
~~~

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/04-warehouse/04-incremental-models" "04-data-engineering/project/dbt"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de15 incremental-models"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE16](../../05-orchestration/01-dependencies/guide.md)


## Independent variation

Create a scratch change for an older event day and a new tombstone. Compare incrementally materialized state with a full refresh, including key sets.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
