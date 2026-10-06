# Local remotes, pull requests and review evidence

## Concept and purpose

A remote names another repository. fetch updates remote-tracking references without automatically merging into your current branch. pull fetches and integrates under its configured policy. push sends commits; it is distinct from writing a message or opening a review.

A bare repository holds history without a working checkout and can simulate a central remote locally. Two clones model two contributors. A pull request is a hosting-platform review proposal; it is not a built-in Git object. A local diff can still teach review before publishing anything.

A useful review explains the problem, changed behavior, validation and remaining limitation. Compare against the intended base, inspect file names and test evidence. Avoid force pushes in this beginner shared-history exercise.

## Syntax example — Bash in Ubuntu

~~~bash
git remote -v
git fetch origin
git branch -vv
git diff main...feature/change
~~~

## Trace the example

Inside the lab clone, fetch updates knowledge of the remote. The three-dot comparison shows branch changes since the merge base.

## Apply it to Data Engineering

A reviewer must understand a data change's effect on counts, keys and recovery, not only syntax.

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes). These explanations and exercises are original course material.
