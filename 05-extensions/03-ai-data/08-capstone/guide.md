# AI08 — Deliver a reproducible document search pipeline

**Difficulty: Integrate.** 2–6 hours across several sessions. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the previous lesson in this track. Review the linked prerequisites when syntax is unfamiliar. Allow 6–10 focused hours; a lesson can take several sessions.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

This lesson uses a manual evidence checklist in expected.md. Passing a local check elsewhere does not complete this lesson. Record the commands, outputs and limitations of the work you actually performed.

## Commit completed work — Windows PowerShell

Work on `main`.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/03-ai-data/08-capstone"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete ai08 capstone"
git push origin main
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: AI07](../07-evaluation/guide.md) · [Next: ST01](../../04-streaming/01-broker/guide.md)
