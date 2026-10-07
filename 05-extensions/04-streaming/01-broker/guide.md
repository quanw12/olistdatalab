# ST01 — Understand topics, partitions and a local broker

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete AI Data, Linux Docker/Compose and DE08–DE11. This is the first lesson requiring a running Kafka stack. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

This lesson uses a manual evidence checklist in expected.md. Passing a local check elsewhere does not complete this lesson. Record the commands, outputs and limitations of the work you actually performed.

## Commit completed work — Windows PowerShell

Use your existing feature/... branch, or create feature/extensions-st01 from a clean starting point. Inspect your current work before changing branches. These commands stage only this lesson; include another file explicitly if your implementation also changed it.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/04-streaming/01-broker"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete st01 broker"
git push -u origin HEAD
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: AI08](../../03-ai-data/08-capstone/guide.md) · [Next: ST02](../02-producer/guide.md)


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
