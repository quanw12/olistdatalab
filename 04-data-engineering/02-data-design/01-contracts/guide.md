# DE04 — Data contracts, types and evolution

[Course](../../README.md) · [Setup](../../setup.md) · [Overall roadmap](../../../roadmap.md)

## Prerequisites and pace

Complete the preceding courses and DE01–DE03. You should be able to write/test Python functions, read analytical SQL and run a program in the named environment.

**Core lesson.** Demonstrate the behavior before marking it complete. Budget 2–4 hours; integrations may need more than one session.

## Study order

1. Read [lesson.md](lesson.md), predict the example and trace it.
2. Complete [exercise.md](exercise.md); starter files contain prompts only.
3. Use [help.md](help.md) one hint at a time.
4. Verify with [expected.md](expected.md), including a failure case.
5. Explain the reflection in notes.md, then mark [progress](../../progress.md).

## Verification

In Windows PowerShell with the Engineering environment prepared:
~~~powershell
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" "C:/DE Courses/04-data-engineering/checks/check.py" DE04
~~~
The provided checker verifies stated fixture contracts; add at least one meaningful changed-input test.

## Commit completed work — Windows PowerShell

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/02-data-design/01-contracts"
git diff --cached --stat
git diff --cached
git commit -m "feat(engineering): complete de04 contracts"
git push -u origin HEAD
~~~

Use your feature/... branch. Review previously staged files too. Runtime databases, secrets and generated files stay ignored or outside the repository.

## Continue

[Previous: DE03](../../01-workflow/03-debugging/guide.md) · [Next: DE05](../02-grain-and-history/guide.md)
