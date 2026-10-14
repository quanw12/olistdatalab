# C13-L04 — Native PostgreSQL with Psycopg

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../../docs/study.md)

[Previous lesson](../03-sqlite-transactions/guide.md) · [Next lesson](../../14-reliable-pipelines/01-incremental/guide.md)

## Study order

Finish earlier lessons first. Offline checker needs no database. The separate live lab needs your native PostgreSQL server and psycopg. These are original DE extensions, not additional video chapters.

1. Read [lesson.md](lesson.md), predict its example, and try it in scratch.py.
2. Implement the exact contracts in [exercise.py](exercise.py). Put demonstrations under a main guard.
3. Read [help.md](help.md) progressively when stuck.
4. Run:

~~~powershell
Set-Location "C:\DE Courses\02-python\13-apis-and-databases\04-postgresql"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Correct the first failure, rerun, and compare [expected.md](expected.md).
6. Answer the reflection before revealing its answer, then mark [progress](../../progress.md).

check.py is provided checking infrastructure. Missing functions are expected initially. Do not edit the checker to pass. The default checker verifies SQL parameter binding and transaction usage using fakes. Only check_live.py confirms behavior on a real PostgreSQL server.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "02-python/13-apis-and-databases/04-postgresql"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c13-l04 postgresql"
git push origin main
~~~

Commit on `main` and inspect previously staged changes too.


## Independent variation

Run the live checker, then explain transaction ownership. Offline binding checks alone do not prove PostgreSQL rollback.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
