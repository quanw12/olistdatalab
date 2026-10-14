# CL01 — Plan one cloud pipeline and its ownership

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete LAB01–LAB08. Review DE19 and optional DE20; Linux Docker lessons are required before live image work. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

This lesson uses a manual evidence checklist in expected.md. Passing a local check elsewhere does not complete this lesson. Record the commands, outputs and limitations of the work you actually performed.

## Commit completed work — Windows PowerShell

Work on `main`.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/02-cloud/01-boundaries"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete cl01 boundaries"
git push origin main
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: LAB08](../../01-labs/08-handoff/guide.md) · [Next: CL02](../02-storage/guide.md)


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
