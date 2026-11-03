# 02 · Git, terminal and Linux

> **Theory notes:** [[Git Branches PRs and Review]] · [[Shell Linux and PowerShell]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 1–3 · **Prerequisites:** 01 started

## Goal
Work like a team member from day one: branches, commits with clear messages, pull requests, and
enough terminal (PowerShell and Bash) to run, inspect and debug a pipeline.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Git and GitHub for Beginners — freeCodeCamp](https://www.youtube.com/watch?v=RGOj5yH7evk) | All | 1 h 08 |
| [Missing Semester L1: The Shell](https://www.youtube.com/watch?v=Z56Jmr9Z34Q) | All | 48 min |
| [Missing Semester L2: Shell Tools and Scripting](https://www.youtube.com/watch?v=kgII-YWo3Zw) | All | 49 min |
| [Linux Command Line for Beginners — Keep On Coding](https://www.youtube.com/watch?v=16d2lHc0Pe8) | All, inside WSL2 (Ubuntu) | 59 min |

## 2. Read
- [Pro Git book ch. 2–3](https://git-scm.com/book/en/v2) (basics, branching)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) — the message style used in this repo
- [Install WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) — you need Linux for Spark, Airflow and Docker later

## 3. Syntax sheet
```bash
git switch -c feat/lab-01            # new branch
git status                          # what changed
git add labs/01-python              # stage specific paths, not everything
git commit -m "feat(lab-01): parse Olist timestamps to UTC"
git push -u origin feat/lab-01      # then open a PR on GitHub
git log --oneline --graph -10
git diff main...HEAD                # what your branch changes
git restore file.py                 # throw away local edits to a file

# Bash (WSL / Git Bash)
ls -la; cd data; pwd
head -5 file.csv; wc -l file.csv     # first lines, line count
grep -c "delivered" file.csv         # count matching lines
cut -d, -f3 file.csv | sort | uniq -c | sort -rn | head   # value counts of column 3
tail -f logs/ingest.log              # follow a log while a job runs
export VAR=value; echo $VAR

# PowerShell equivalents
Get-Content file.csv -TotalCount 5
(Get-Content file.csv).Count
Select-String -Path file.csv -Pattern "delivered" | Measure-Object
$env:VAR = "value"
```

## 4. Practice
1. Create a throwaway repo, make 3 commits, branch, change the same line on both branches, merge, resolve the conflict.
2. With only Bash commands, answer for `data/landing/olist/olist_orders_dataset.csv`: how many rows? how many per status? (Note: `cut` breaks on quoted commas — why is that a problem for real CSVs?)
3. Write a 10-line Bash script `count_rows.sh` that prints the row count of every CSV in a folder.

## 5. Apply to the project
1. Install WSL2 + Ubuntu and Docker Desktop (WSL2 backend). Check: `wsl -l -v`, `docker run hello-world`.
2. Clone this repo inside WSL too and run `pytest` there.
3. From now on every lab goes on its own branch + PR into `main`. Write the PR description:
   what, why, how you tested.
4. Write `scripts/landing_report.sh` that prints, for each landing CSV, its size, row count and
   SHA-256 (`sha256sum`). Compare the hashes with `audit.ingest_manifest` after `olist ingest`.

## 6. Self-check
- What is the difference between `git fetch`, `git pull` and `git merge`?
- Why never commit `.env` or the dataset? Where is that enforced in this repo?
- How do you find which process is holding a file or a port?

## Done when
- [ ] WSL2 + Docker working
- [ ] Lab 01 merged through a PR
- [ ] `landing_report.sh` committed and its hashes match the manifest
