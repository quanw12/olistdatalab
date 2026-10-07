# AI01 — Define document identity and provenance

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the Cloud track locally or live. Review Python strings/files and DE22 verified AI use. No paid LLM or GPU is required. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

~~~powershell
Set-Location "C:\DE Courses\05-extensions\03-ai-data\01-documents"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "../../checks/check.py" AI01
~~~
The first run should fail because the implementation is unfinished. Write your own small tests, then use the checker, which includes changed inputs.

## Commit completed work — Windows PowerShell

Use your existing feature/... branch, or create feature/extensions-ai01 from a clean starting point. Inspect your current work before changing branches. These commands stage only this lesson; include another file explicitly if your implementation also changed it.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/03-ai-data/01-documents"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete ai01 documents"
git push -u origin HEAD
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: CL08](../../02-cloud/08-capstone/guide.md) · [Next: AI02](../02-text/guide.md)
