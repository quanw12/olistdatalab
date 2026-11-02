# 01 · Setup, Git and CI

**Time:** week 1 · **Stack:** Python venv, Git, GitHub Actions, pytest, ruff, PowerShell/Bash

## Why
Every team works through branches, pull requests and automated checks. An intern who can open a
clean PR with green CI is productive on day one.

## Learn
- Virtual environments and editable installs (`pip install -e .`) — [Python packaging guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- Git: branch, commit, rebase vs merge, PR review — [Pro Git ch. 3](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- pytest fixtures and parametrize — [pytest docs](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- GitHub Actions workflow syntax — [docs](https://docs.github.com/en/actions/writing-workflows)

## Read in this repo
- `pyproject.toml` — dependencies, optional extras, the `olist` console script, ruff/pytest config.
- `.github/workflows/ci.yml` — what runs on every push.
- `tests/conftest.py` — fixtures that build a sample landing folder per test.

## Build
1. Fresh clone in a new folder, follow the README quick start, get `pytest` green.
2. Install Docker Desktop with the WSL2 backend; run `docker run hello-world`. (Needed from module 06.)
3. Add a `pre-commit` config that runs ruff before each commit. **Check:** a badly formatted file is blocked.
4. Add a CI step that uploads `logs/` as an artifact when a job fails (`actions/upload-artifact`, `if: failure()`).
5. From now on: one branch + PR per exercise, even working alone.

## Break it
- Push a commit with a failing test. Read the CI log until you can point at the failing line.
- Delete `tzdata` from dependencies and run on Windows: what breaks and why?

## Interview questions
- What happens between `git push` and a green check on your PR?
- Why pin dependency versions in CI, and what does it cost?

## Done when
- [ ] Repo installs and tests pass from a fresh clone
- [ ] Pre-commit + CI artifact step merged through a PR
- [ ] You can explain every line of `ci.yml`
