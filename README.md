# Data Engineering learning workspace

Start with the [30-day foundation course](de-30-days/README.md). Every day has concepts, syntax examples, a problem statement, detailed hints, and a completion check. Future deeper Python, SQL, and internship tracks can have their own folders.

## Conventions
- Write materials in English.
- Use feature/... branches; daily branches use feature/dayNN.
- Keep exercises as problem statements; put teaching examples in lesson.md and detailed hints in help.md.
- Every guide includes commit and push commands.
- Preserve learner submissions.
- Use local PostgreSQL and pgAdmin through Day 17; introduce Docker in Day 18.

## Saved unfinished work

Your unfinished Day 12 work and related README/resources edits were saved, including untracked files:
- Original branch: feature/day12.
- Stash commit: c031987f2878b5642dd87a066ff67e0cef6d4213.
- Message: WIP Day 12 before completing the 30-day course (2026-10-06).

The stash is retained. Ignored local files are not included by --include-untracked; existing daily ignored files were moved with their folders into de-30-days.

To resume the original work, first commit the curriculum changes or save them in a separate stash. Then:

~~~powershell
Set-Location "C:\DE Courses"
git switch feature/day12
git stash apply c031987f2878b5642dd87a066ff67e0cef6d4213
~~~

This restores Day 12 at its original paths on that branch and retains the backup. Do not apply the old layout over the reorganized course branch.

## Commit this curriculum

After reviewing:

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- README.md .gitignore de-30-days
git add -u
git diff --cached --stat
git commit -m "docs(course): complete the 30-day DE foundation curriculum"
git push -u origin feature/de-30-day-course
~~~

The second staging command records the old paths' removals. Inspect staged files before committing. Day 11 is part of this branch's ancestry; merge its branch first if a later pull request should show only the curriculum changes.
