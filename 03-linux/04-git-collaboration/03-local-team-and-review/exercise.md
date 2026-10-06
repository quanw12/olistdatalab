# LE15 assignment

Create a NEW local bare repository at $LE_LAB_ROOT/git/team/origin.git using git init --bare --initial-branch=main. Clone it into alice and bob. Configure lab-local identities as in LE13. Alice commits a README on main and pushes it locally. Bob fetches and uses git switch -c main --track origin/main if no local main exists, otherwise fast-forward pulls. Bob creates feature/change, commits one documented improvement and pushes that branch locally. Alice fetches and reviews main...origin/feature/change. Write review.md with problem, behavior, validation and one meaningful question; write a proposed PR description in pr.md. Do not contact anyone or publish remotely as part of this task.

## Deliverables

review.md, pr.md and notes.md with remote paths and the actual diff. Optional: later use the same review steps in a private repository you deliberately choose.

## Reflection

What does fetch change, and what does it leave for you to decide?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
