# DE03 — Read, debug and profile unfamiliar code

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Course](../../README.md) · [Setup](../../setup.md) · [Overall roadmap](../../../roadmap.md)

## Before starting

Complete the Foundations, Python and Linux courses, or demonstrate their exit checks. This is a core lesson. Allow 2–4 hours and split debugging work into sessions when needed.

Read [lesson.md](lesson.md), then attempt [exercise.md](exercise.md). Use [help.md](help.md) progressively. Compare with [expected.md](expected.md) after your attempt, answer the reflection in notes.md and update [progress](../../progress.md). The [shared study guide](../../../docs/study.md) explains the routine.

## Verify

In Windows PowerShell, after implementing build_report in exercise.py:

~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\01-workflow\03-debugging"
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "../../checks/check.py" DE03
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" -m unittest test_report -v
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" -m cProfile -s cumulative benchmark.py
~~~

Write your own regression tests first; test_report.py initially contains prompts. The supplied checker adds changed-input cases. A performance profile is evidence of the run you performed, not a required speed threshold.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/01-workflow/03-debugging"
git diff --cached --stat
git diff --cached
git commit -m "feat(de): complete de03 debugging"
git push -u origin HEAD
~~~

Use your feature/... branch and inspect all staged files. Generated profiles/output stay ignored. See [workspace conventions](../../../docs/workspace.md).

## Continue

[Previous: DE02](../02-tasks/guide.md) · [Next: DE04](../../02-data-design/01-contracts/guide.md)
