# Git states, branches, diffs and scoped undo

## Concept and purpose

Git tracks committed history, the staging index and working files. git diff compares unstaged work; git diff --cached compares staged work with HEAD. A commit includes everything already staged, not only the latest path you added.

A branch names a line of commits; switching branches does not create an independent directory. git switch -c creates a new branch. Inspect status before switching or undoing. git restore --staged changes the index; git restore discards working edits for the named tracked path. Use the latter only when that exact change is disposable.

The lab uses local per-repository identity and a feature/... branch. Do not change global Git configuration as part of this exercise.

## Syntax example — Bash in Ubuntu

~~~bash
git status --short
git diff
git diff --cached
git log --oneline --max-count=5
~~~

## Trace the example

Run these inside the separate repository you create. Each view shows a different state; an unstaged edit does not appear in the cached diff.

## Apply it to Data Engineering

Small reviewed commits make pipeline changes traceable and recoverable.

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository). These explanations and exercises are original course material.
