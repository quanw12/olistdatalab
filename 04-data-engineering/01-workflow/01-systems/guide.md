# DE01 — Data systems and the lifecycle

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Overall roadmap](../../../roadmap.md)

## Before starting

Complete the Foundations, Python and Linux courses, or demonstrate their exit checks. This is a core lesson. Allow 2–4 hours and split debugging work into sessions when needed.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Use [help.md](help.md) progressively. Compare with [expected.md](expected.md) after your attempt, answer the reflection in notes.md and update [progress](../../progress.md). The [shared study guide](../../../docs/study.md) explains the routine.

## Verify

Use the design checklist in expected.md. Trace the supplied retail changes by hand; there is no executable checker for a design explanation. Separate fixture observations from assumptions about a real source.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/01-workflow/01-systems"
git diff --cached --stat
git diff --cached
git commit -m "feat(de): complete de01 systems"
git push origin main
~~~

Work on `main` and inspect all staged files. Generated profiles/output stay ignored. See [workspace conventions](../../../docs/workspace.md).

## Continue

[Course index](../../README.md) · [Next: DE02](../02-tasks/guide.md)


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
