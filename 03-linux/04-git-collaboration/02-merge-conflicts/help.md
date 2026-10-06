# Help — Merge conflicts and preserving both intentions

## First hint

Resolve the behavior, not only the marker text.

## Detailed approach

Make both edits to the same committed base line on separate branches. Commit each before switching. git merge feature/retry-policy on main should expose that overlap. Open policy.txt and identify <<<<<<<, ======= and >>>>>>> sections. Replace them with the final valid line and explain the choice. git add -- policy.txt marks it resolved; git commit completes the merge. Check git diff --check and status.

If you need exact steps, run these in the LE13 lab after committing its work. Start on main, with a clean status:

~~~bash
cd "$LE_LAB_ROOT/git/basics"
git switch main
git status --short
printf 'retries=1\n' > policy.txt
git add -- policy.txt
git commit -m 'docs(lab): establish shared retry policy'
git switch -c feature/retry-policy
printf 'retries=3\n' > policy.txt
git add -- policy.txt
git commit -m 'feat(lab): increase retry budget'
git switch main
printf 'retries=2\n' > policy.txt
git add -- policy.txt
git commit -m 'feat(lab): adjust baseline retries'
git merge feature/retry-policy
git status
cat policy.txt
~~~

The merge's nonzero status is intentional. Decide the final policy and edit policy.txt; do not blindly keep both numbers. Then:

~~~bash
git add -- policy.txt
git diff --cached
git diff --check
git commit -m 'merge(lab): reconcile retry policy'
git status
~~~

If the branch already exists, inspect it instead of repeating branch creation. `git merge --abort` cancels an unresolved practice merge if you need to return to the clean pre-merge state.

## Troubleshooting

Changing different lines may merge automatically. A branch not based on the same shared file may produce a different conflict. Uncommitted edits can block switching/merging.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
