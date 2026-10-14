# DE14 — dbt data tests and transformation evidence

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE13](../02-dbt-models/guide.md)

## Prerequisites and pace

DE13 and DE10 quality checks.

**Core lesson.** Demonstrate the behavior before marking it complete. Use the difficulty and pace above.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Use [help.md](help.md) one hint at a time.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

Record the real commands, outputs and limits in notes.md. Expected observations are criteria, not a claim that an author ran your environment.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/04-warehouse/03-dbt-tests" "04-data-engineering/project/dbt"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de14 dbt-tests"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE15](../04-incremental-models/guide.md)
