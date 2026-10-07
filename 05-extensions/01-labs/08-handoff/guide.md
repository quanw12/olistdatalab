# LAB08 — Complete an independent maintenance ticket

**Difficulty: Assess.** use the assignment's timebox; otherwise allow 2–4 hours. Syntax documentation is allowed; keep approach hints closed until the independent attempt ends.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the previous lesson in this track. Review the linked prerequisites when syntax is unfamiliar. Allow 4–8 focused hours; a lesson can take several sessions.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

This lesson uses a manual evidence checklist in expected.md. Passing a local check elsewhere does not complete this lesson. Record the commands, outputs and limitations of the work you actually performed.

## Commit completed work — Windows PowerShell

Use your existing feature/... branch, or create feature/extensions-lab08 from a clean starting point. Inspect your current work before changing branches. These commands stage only this lesson; include another file explicitly if your implementation also changed it.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/01-labs/08-handoff"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete lab08 handoff"
git push -u origin HEAD
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: LAB07](../07-logs/guide.md) · [Next: CL01](../../02-cloud/01-boundaries/guide.md)
