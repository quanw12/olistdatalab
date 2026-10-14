# Workspace conventions

[Home](../README.md) · [Roadmap](../roadmap.md)

## Folder layout

The root has one README, one roadmap, four numbered core courses and [05-extensions](../05-extensions/README.md). `docs/` holds shared guidance. Use lowercase hyphenated folder names. Keep solutions inside the lesson folder; put generated output in `output/` or paths named in the guide.

Each course owns setup, lesson index, progress and sources. SQL remains an independent track alongside the current course.

## Git: work on `main`

Commit after you verify a lesson. Pull before starting a new session.

~~~powershell
Set-Location "C:\DE Courses"
git checkout main
git pull origin main
git status
# Use the scoped git add paths from the lesson guide.md
git diff --cached --stat
git commit -m "feat(day-01): complete the daily DE exercise"
git push origin main
~~~

Do not commit passwords, `.env`, live database dumps, or secrets. Review the staged diff every time.

Lesson guides contain the exact folder to stage. Stage `progress.md` when you check off completion.

## Clean local feature branches (optional)

If you still have old `feature/day*` branches locally:

~~~powershell
Set-Location "C:\DE Courses"
git checkout main
git branch | ForEach-Object { $_.Trim() } | Where-Object {
  $_ -notmatch '^\*' -and $_ -ne 'main' -and $_ -ne 'master'
} | ForEach-Object { git branch -D $_ }
~~~

To remove matching branches on the remote (only when you no longer need them):

~~~powershell
git push origin --delete feature/day01  # repeat per branch name
~~~

## Evidence and fixtures

Do not edit supplied fixtures unless a guide tells you to copy them to a scratch path. Label evidence as offline, native database, container, or CI as directed in [study.md](study.md).
