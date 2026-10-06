# Workspace conventions

[Home](../README.md) · [Roadmap](../roadmap.md)

## Folder and naming rules

The root contains one README, one overall roadmap and four numbered courses. `docs/` holds shared guidance. Use lowercase folder names with hyphens; course numbers define learning order. Keep notes and solutions inside their lesson. Keep generated artifacts in output/ or a scoped external lab directory.

Each course owns its setup, lesson index, progress and source references. These describe that course; they do not create a second overall study schedule. SQL remains your independent learning track.

Old completed work is preserved under [01-foundation/submissions](../01-foundation/submissions/README.md). Its original bytes and old command text are historical evidence. Use the active lesson guides for current paths.

## Day 12 and the existing stash

Your unfinished schema is at [01-foundation/day-12/schema.sql](../01-foundation/day-12/schema.sql). The older stash `c031987f2878b5642dd87a066ff67e0cef6d4213` is retained. It references the old folder layout; do not blindly apply it over the reorganized course. Inspect it first if you need a historical file. The current schema is already in the workspace, so restoring the stash is not a step required to continue Day 12.

A recoverable copy of the pre-cleanup course files is stored outside this repository at `C:\Users\DELL\AppData\Local\Temp\de-course-cleanup-20261006\before.zip`. The same backup folder contains a hash manifest and old-to-new path map. The cleanup preserved learner submissions and Day 12's schema.

## Git: keep your feature/... convention

Lesson guides contain scoped commands for their work. Run them in **Windows PowerShell**, inspect the current branch and staged diff, then commit only what you intend. If you are starting a new branch, inspect status first and use a name such as `feature/day12` or `feature/course-cleanup`. Check whether the name exists before creating it. Uncommitted changes are not isolated by a branch name.

The cleanup changes many paths. To save it together with your current Day 12 work, review and use:

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -A -- .
git diff --cached --stat
git diff --cached
git commit -m "docs(course): organize the DE learning path and preserve practice"
git push -u origin HEAD
~~~

This migration command stages the whole workspace, including tracked removals and the current Day 12 schema: inspect its diff before committing. It does not restore the stash. For later lesson commits, use that guide's smaller path list and review any files already staged.

No branch switch, commit, push or stash operation is performed by editing the course materials.
