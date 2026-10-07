# LAB03 — Extend a schema without losing existing data

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the previous lesson in this track. Review the linked prerequisites when syntax is unfamiliar. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

~~~powershell
Set-Location "C:\DE Courses\05-extensions\01-labs\03-migration"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "../../checks/check.py" LAB03
~~~
The first run should fail because the implementation is unfinished. Write your own small tests, then use the checker, which includes changed inputs.

## Commit completed work — Windows PowerShell

Use your existing feature/... branch, or create feature/extensions-lab03 from a clean starting point. Inspect your current work before changing branches. These commands stage only this lesson; include another file explicitly if your implementation also changed it.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/01-labs/03-migration"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete lab03 migration"
git push -u origin HEAD
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: LAB02](../02-api-change/guide.md) · [Next: LAB04](../04-backfill/guide.md)


## Independent variation

Demonstrate old-writer omission versus explicit NULL and a pre-commit failure in a disposable database. The one-line checker is only a drill.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
