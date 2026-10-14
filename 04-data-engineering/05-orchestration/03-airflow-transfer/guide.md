# DE18 — Airflow concepts and orchestration transfer

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE17](../02-prefect-runs/guide.md)

## Prerequisites and pace

DE16–DE17; role-specific extension.

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
git add -- "04-data-engineering/05-orchestration/03-airflow-transfer"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de18 airflow-transfer"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE19](../../06-platforms/01-cloud-design/guide.md)


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
