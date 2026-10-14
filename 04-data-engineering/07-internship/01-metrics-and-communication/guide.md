# DE23 — Metric definitions and honest analytics

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE22](../../06-platforms/04-security-and-ai/guide.md)

## Prerequisites and pace

DE13–DE14; core SQL; foundation Day 25 optional chart refresh.

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
git add -- "04-data-engineering/07-internship/01-metrics-and-communication"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de23 metrics-and-communication"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE24](../02-ml-feature-data/guide.md)


## Independent variation

Give the consumer a data dictionary and source-to-report column mapping; ask them to identify the grain and one unsafe interpretation.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
