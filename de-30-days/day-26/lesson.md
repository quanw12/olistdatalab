# Day 26 — Continuous integration with GitHub Actions


## What CI verifies

Continuous integration runs checks when code changes. A workflow describes triggers and jobs; a runner executes a job; steps run commands or reusable actions. A green check proves only the checks you actually ran. It does not certify cloud deployment or production reliability.

The workflow file must be at repository root under .github/workflows/ci.yml. This is the one necessary placement exception to keeping the curriculum inside de-30-days. Create that file yourself today; the provided day-26/ci.yml is only a problem statement.

## YAML syntax

This unrelated example shows indentation, a job and steps:

~~~yaml
name: Example
on: [push, pull_request]
permissions:
  contents: read
jobs:
  demo:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.13"
      - run: python --version
~~~

The action versions above were checked on 2026-10-06 in their repositories. Recheck release notes when deliberately updating them. Major-version tags are convenient for this lab; production teams may pin reviewed commit SHAs.

## Working directories differ

Checkout places your repository on a fresh Linux runner. It has no C:\DE Courses, local PostgreSQL password or activated Windows venv. Set defaults.run.working-directory to de-30-days/capstone, install runtime/development requirements, then run python -m pytest -m "not integration" -q.

checkout and setup-python are actions, not shell run steps; working-directory applies to run steps. Use a Python 3.13 version explicitly rather than inheriting the runner's default.

The required workflow runs unit tests only. They must not need live API calls, DB credentials, Docker Desktop or Prefect server. Keep integration tests marked and side-effect-free during collection. A later optional CI job can create an isolated PostgreSQL service.

## A useful failure demonstration

Temporarily change one expected value locally and run tests to see failure; restore it. For CI, push the valid workflow on your feature branch and inspect Actions logs. If you deliberately demonstrate a failing pushed commit, follow with a fix before considering the work complete. Do not add write permissions or account secrets just to make unit tests pass.

Read: [Python CI](https://docs.github.com/en/actions/tutorials/build-and-test-code/python), [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python).
