# DE26 — An independent take-home and debugging rehearsal

**Difficulty: Assess.** 4 hours for implementation plus the separate SQL diagnostic. Syntax documentation is allowed; keep approach hints closed until the independent attempt ends.

[Course](../../README.md) · [Setup](../../setup.md) · [Previous: DE25](../03-integrated-capstone/guide.md)

## Prerequisites and pace

DE25 core acceptance and independent SQL gate.

**Core lesson.** Demonstrate the behavior before marking it complete. Use the difficulty and pace above.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Keep [help.md](help.md) closed until the independent attempt ends; then use it to diagnose gaps.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

Record the real commands, outputs and limits in notes.md. Expected observations are criteria, not a claim that an author ran your environment.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/07-internship/04-unseen-assignment"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de26 unseen-assignment"
git push origin main
~~~

Work on `main`. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Next: DE27](../05-source-discovery/guide.md)
