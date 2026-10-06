# DE19 — Cloud storage, IAM and cost-aware design

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE18](../../05-orchestration/03-airflow-transfer/guide.md)

## Prerequisites and pace

DE12 and Linux container/storage lessons.

**Core lesson.** Demonstrate the behavior before marking it complete. Budget 2–4 hours; integrations may need more than one session.

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
git add -- "04-data-engineering/06-platforms/01-cloud-design"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de19 cloud-design"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE20](../02-bigquery-sandbox/guide.md)
