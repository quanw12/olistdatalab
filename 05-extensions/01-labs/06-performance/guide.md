# LAB06 — Measure and improve dimension enrichment

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the previous lesson in this track. Review the linked prerequisites when syntax is unfamiliar. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

~~~powershell
Set-Location "C:\DE Courses\05-extensions\01-labs\06-performance"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "../../checks/check.py" LAB06
~~~
The first run should fail because the implementation is unfinished. Write your own small tests, then use the checker, which includes changed inputs.

## Commit completed work — Windows PowerShell

Work on `main`.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/01-labs/06-performance"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete lab06 performance"
git push origin main
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: LAB05](../05-recovery/guide.md) · [Next: LAB07](../07-logs/guide.md)
