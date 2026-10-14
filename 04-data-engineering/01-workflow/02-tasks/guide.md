# DE02 — From an assigned task to a checked delivery

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Overall roadmap](../../../roadmap.md)

## Before starting

Complete the Foundations, Python and Linux courses, or demonstrate their exit checks. This is a core lesson. Allow 2–4 hours and split debugging work into sessions when needed.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Use [help.md](help.md) progressively. Compare with [expected.md](expected.md) after your attempt, answer the reflection in notes.md and update [progress](../../progress.md). The [shared study guide](../../../docs/study.md) explains the routine.

## Verify

Review task.md, plan.md, test-cases.md and handoff.md against expected.md. This lesson assesses requirement reasoning, not a finished pipeline. Use actual fixture values for small acceptance examples.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/01-workflow/02-tasks"
git diff --cached --stat
git diff --cached
git commit -m "feat(de): complete de02 tasks"
git push origin main
~~~

Work on `main` and inspect all staged files. Generated profiles/output stay ignored. See [workspace conventions](../../../docs/workspace.md).

## Continue

[Previous: DE01](../01-systems/guide.md) · [Next: DE03](../03-debugging/guide.md)


## Independent variation

List observed source facts before writing your plan. Separate source guarantees requiring confirmation from assumptions you can test.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
