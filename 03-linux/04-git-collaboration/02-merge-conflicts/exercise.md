# LE14 assignment

Starting from the lab's main branch, create a shared file policy.txt containing retries=1 and commit it. Create feature/retry-policy and change that same line to retries=3, then commit. Switch to main, change the line to retries=2 and commit. Merge feature/retry-policy into main; expect a conflict. Record both intended changes, choose/document the final policy, remove markers, add the file and complete the merge. Record git status and log. If no conflict occurred, explain what input/history differed rather than claiming one.

## Deliverables

notes.md with the actual conflict, final policy and reasoning; retain the lab merge commit.

## Reflection

Why is keeping one branch's entire file without reading the other branch a risky resolution?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
