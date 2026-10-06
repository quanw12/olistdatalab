# Merge conflicts and preserving both intentions

## Concept and purpose

A merge combines histories. Git can automatically combine non-overlapping changes, but overlapping edits may need a human decision. Conflict markers show alternatives; they are not valid final program content.

Inspect git status and the disputed lines. Understand both branches' intent before editing. Remove markers, keep the chosen combined result, stage the resolved file and complete the merge. git merge --abort returns from an unfinished merge when you intentionally abandon it; do not invent a resolution merely to silence Git.

After resolving source code, rerun relevant tests. A conflict-free merge is not proof that behavior remains correct. This lab uses an isolated text file to teach the mechanics before touching real pipeline code.

## Syntax example — Bash in Ubuntu

~~~bash
git status
git diff --check
git log --oneline --graph --all --max-count=12
~~~

## Trace the example

During a conflict, status identifies unmerged paths. diff --check may detect conflict markers or whitespace errors; graph displays the diverging histories.

## Apply it to Data Engineering

Team pipeline changes often overlap on configuration or transformations. Preserve both required behaviors and verify after merging.

[Reference](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging). These explanations and exercises are original course material.
