# LE13 assignment

1. Create a new directory $LE_LAB_ROOT/git/basics and git init -b main there. If it already contains a repository, inspect it instead of resetting it.
2. Set local user.name 'DE Student', user.email 'student@example.test' and commit.gpgsign false for this lab only.
3. Create README.md with one line, add/commit it.
4. Create feature/logging, change README.md and create a new notes.txt.
5. Stage only README.md and compare both diffs/status.
6. Unstage only README.md with git restore --staged -- README.md; explain that its edit remains.
7. Stage/commit the intended files and inspect log. Save the evidence in this course lesson's notes.md.

## Deliverables

notes.md with state transitions, staged-file list and actual lab commit IDs. Lab .git stays outside the learning repository.

## Reflection

Why might git commit include a file you did not add in your most recent command?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
