# C09-L02 — Logging and observable failures

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../self-study.md)

[Previous lesson](../../09-errors-and-types/01-exceptions/guide.md) · [Next lesson](../../09-errors-and-types/03-dataclasses/guide.md)

## Before you start

Finish earlier lessons in order. This lesson uses only Python's standard library. Budget one or two focused sessions; the capstone takes several sessions. These are original DE extension lessons, not additional chapters from Baraa's video.

## Study and practise

1. Read [lesson.md](lesson.md). Predict the small example before running it in scratch.py.
2. Implement the exact names/contracts in [exercise.py](exercise.py). Keep executable demonstrations under an if __name__ == "__main__" guard so importing the file does not start work.
3. Use [help.md](help.md) in stages. Every required input and output is specified locally.
4. Run the provided checker:

~~~powershell
Set-Location "C:\DE Courses\Python\09-errors-and-types\02-logging"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Read its first failure, correct one cause and rerun. Missing functions are expected before implementation. check.py is provided checking infrastructure; do not edit it to make a solution pass.
6. Compare [expected.md](expected.md), explain the result, then mark [progress](../../progress.md).

The checker uses temporary data/files and no Codex account. It checks the stated contract, not every possible production behavior.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "Python/09-errors-and-types/02-logging"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c09-l02 logging"
git push -u origin HEAD
~~~

Use your existing feature/... branch. Inspect all previously staged changes too. Shared course setup can be committed using the course README's command.
