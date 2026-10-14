# DE05 — Grain, dimensions and historical meaning

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE04](../01-contracts/guide.md)

## Prerequisites and pace

DE04 and foundation Day 12; practise SQL independently.

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
git add -- "04-data-engineering/02-data-design/02-grain-and-history"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de05 grain-and-history"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE06](../03-transactions/guide.md)


## Independent variation

Place an event exactly at a dimension boundary, then introduce overlapping intervals. Prove the first maps once and the second is rejected.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
