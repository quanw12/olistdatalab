# DE05 — Grain, dimensions and historical meaning

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE04](../01-contracts/guide.md)

## Prerequisites and pace

DE04 and foundation Day 12; practise SQL independently.

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
git add -- "04-data-engineering/02-data-design/02-grain-and-history"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de05 grain-and-history"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE06](../03-transactions/guide.md)
