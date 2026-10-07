# DE21 — Spark schemas, plans and distributed-processing decisions

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE20](../02-bigquery-sandbox/guide.md)

## Prerequisites and pace

DE12 SQL/dataframes; optional PySpark role extension.

**Optional specialization.** Skip this runtime until a target role needs it. Read the concepts and record your choice. Use the difficulty and pace above.

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
git add -- "04-data-engineering/06-platforms/03-spark-introduction"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de21 spark-introduction"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE22](../04-security-and-ai/guide.md)
