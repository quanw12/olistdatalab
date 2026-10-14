# CL04 — Load history and materialize current state

**Difficulty: Integrate.** 2–6 hours across several sessions. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Track](../README.md) · [Setup](../../setup.md) · [Roadmap](../../../roadmap.md)

## Start

Complete the previous lesson in this track. Review the linked prerequisites when syntax is unfamiliar. Use the difficulty and pace above.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Your implementation belongs in this lesson folder. Use [help.md](help.md) one hint at a time; compare with [expected.md](expected.md) after attempting the task. Record reflections and evidence in [notes.md](notes.md), then update [progress](../../progress.md).

## Verify

~~~powershell
Set-Location "C:\DE Courses\05-extensions\02-cloud\04-warehouse"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "../../checks/check.py" CL04
~~~
The first run should fail because the implementation is unfinished. Write your own small tests, then use the checker, which includes changed inputs.

## Commit completed work — Windows PowerShell

Work on `main`.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "05-extensions/02-cloud/04-warehouse"
git diff --cached --stat
git diff --cached
git commit -m "feat(extensions): complete cl04 warehouse"
git push origin main
~~~

Keep generated databases, profiles, credentials and output out of commits. [Workspace rules](../../../docs/workspace.md) explain staging and branches. Files under this course's data/ directory are supplied fixtures; do not edit them to make a check pass.

## Continue

[Previous: CL03](../03-jobs/guide.md) · [Next: CL05](../05-iam/guide.md)


## Avoid repeating DE12

The offline latest-state query is a refresher. If you can explain and pass a changed
version/delete case without hints, do not repeat the earlier tutorial. The new work
is the live warehouse load/MERGE, its permissions and the comparison with a rebuild.
Record offline and live evidence separately; only the latter demonstrates deployment.
