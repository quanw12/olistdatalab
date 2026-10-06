# CI that catches a real regression

## Concept and purpose

Continuous integration runs defined checks on proposed changes in a fresh runner environment. A passing local run does not prove the same paths/line endings/interpreter work on Linux. A workflow declares triggers, jobs, runner labels and steps.

Use read-only contents permission for a job that only checks code. Select Python explicitly; no dependencies are required by the supplied app. A failing test must fail the job rather than being ignored with continue-on-error. Syntax checks alone cannot prove the script's behavior.

A workflow file under project/ is only a draft. GitHub activates YAML under .github/workflows after you deliberately place and push it there. This course creates no active workflow automatically. Test a deliberate regression in an isolated lab copy and record both failure and repaired success.

## Syntax example — workflow YAML syntax; this toy example is not the complete assignment

~~~yaml
name: Toy Python check
on: [workflow_dispatch]
permissions:
  contents: read
jobs:
  check:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -c "print('runner ready')"
~~~

## Trace the example

The job checks out code, selects Python 3.12 and runs a toy command. It does not install packages or publish an image.

## Apply it to Data Engineering

A useful CI job rejects a behavior regression, not just malformed syntax.

[Reference](https://docs.github.com/en/actions/tutorials/build-and-test-code/python). These explanations and exercises are original course material.
