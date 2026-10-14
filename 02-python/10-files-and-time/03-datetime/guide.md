# C10-L03 — Aware time, UTC, and deterministic clocks

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../../docs/study.md)

[Previous lesson](../02-csv-jsonl/guide.md) · [Next lesson](../04-decimal/guide.md)

## Before you start

Finish earlier lessons in order. This lesson uses only Python's standard library. Budget one or two focused sessions; the capstone takes several sessions. These are original DE extension lessons, not additional chapters from Baraa's video.

## Study and practise

1. Read [lesson.md](lesson.md). Predict the small example before running it in scratch.py.
2. Implement the exact names/contracts in [exercise.py](exercise.py). Keep executable demonstrations under an if __name__ == "__main__" guard so importing the file does not start work.
3. Use [help.md](help.md) in stages. Every required input and output is specified locally.
4. Run the provided checker:

~~~powershell
Set-Location "C:\DE Courses\02-python\10-files-and-time\03-datetime"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Read its first failure, correct one cause and rerun. Missing functions are expected before implementation. check.py is provided checking infrastructure; do not edit it to make a solution pass.
6. Compare [expected.md](expected.md), explain the result, then mark [progress](../../progress.md).

The checker uses temporary data/files and no Codex account. It checks the stated contract, not every possible production behavior.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "02-python/10-files-and-time/03-datetime"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c10-l03 datetime"
git push origin main
~~~

Use your existing feature/... branch. Inspect all previously staged changes too. Shared course setup can be committed using the course README's command.


## Independent variation

Use two offset representations of the same instant and one naive value. Require equivalent UTC results and rejection of the naive value.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
