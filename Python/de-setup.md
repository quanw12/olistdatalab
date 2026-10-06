# Python-for-DE extension setup

Use this page before Chapter 9. Chapters 1–8 need only Python; follow [their setup](setup.md) first.

## The tested environment

The extension examples and offline reference checks are tested with Windows and Python **3.13.5**. Python 3.13 is the target for this package set. Your machine's verified interpreter is:

~~~text
C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe
~~~

This is separate from the Python 3.14 path used in earlier daily lessons. Using one explicit interpreter avoids installing packages into one version and running another. If you move to a different computer, replace the base interpreter path with its installed Python 3.13 executable.

## Create the dedicated environment once

Run in PowerShell. Do not type the PS prompt or the fence markers.

~~~powershell
Set-Location "C:\DE Courses"
& "C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe" --version
& "C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe" -m venv .venv-python-de
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" -m pip install -r ".\Python\requirements-de.txt"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" -m pip check
~~~

The ampersand calls an executable whose quoted path contains spaces. -m runs a module using that exact interpreter. venv creates an isolated package environment; it does not copy your lesson files. No activation or execution-policy change is needed.

Installation needs internet access. The requirements pin the four direct packages used by the examples: pandas 2.3.3, requests 2.32.5, pyarrow 21.0.0 and pytest 9.0.2. These are the tested versions, not a claim that they are the newest. Transitive packages are resolved by pip; this is a teaching environment, not a fully locked deployment.

## Confirm and run

~~~powershell
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" -c "import sys, pandas, requests, pyarrow, pytest; print(sys.version); print(pandas.__version__, requests.__version__, pyarrow.__version__, pytest.__version__)"
Set-Location "C:\DE Courses\Python\09-errors-and-types\01-exceptions"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

An untouched exercise should report FAIL because parse_count does not exist yet. That means the checker started correctly. Implement the task, then run it again. Do not use python -O: the checks use assertions.

In VS Code, use Python: Select Interpreter and choose .venv-python-de\Scripts\python.exe. The commands in each guide work even if the editor selection is different.

## Dependencies by section

| Section | Requirement |
|---|---|
| 09 errors/types, 10 files/time | Standard library |
| 11 modules/CLI/unittest/mocks | Standard library; pytest only for the additional testing practice |
| 12 generators | Standard library |
| 12 pandas/Parquet | pandas and pyarrow |
| 13 offline API/pagination/retry exercises | Standard library; requests for the optional HTTP adapter example |
| 13 SQLite | Standard library |
| 13 PostgreSQL offline checker | Standard library mocks; no server connection |
| 13 PostgreSQL live lab | Your native PostgreSQL server, pgAdmin and optional psycopg driver |
| 14 reliability/capstone | Standard library |

The [PostgreSQL lab](13-apis-and-databases/04-postgresql/live-lab.md) gives its separate installation and connection steps. pgAdmin is a client, not the database engine. No Docker setup is used here. The live lab was not executed during author verification.

## Working directories and paths

Each guide first changes into its lesson folder. .\check.py means the checker in that folder. The supplied checkers locate their exercise using their own file path and use temporary directories for generated data. The capstone demonstration uses its ignored output folder.

Keep the shared [data](data/README.md) unchanged. Test variants belong in your lesson's output folder or a temporary directory. A repository-relative path in your code is not automatically relative to the script: use pathlib and an explicit base when needed.

## Troubleshooting

| Symptom | Next action |
|---|---|
| Executable path is missing | Verify that Python 3.13 is installed and replace the base path with its actual location; do not guess a new path |
| No module named pandas/pyarrow | Run pip install using the same .venv-python-de interpreter as the checker |
| Cannot open check.py | Use the Set-Location command from that lesson's guide |
| FAIL: AttributeError | Define the exact function name and signature requested in exercise.py |
| FAIL: AssertionError | Read the failing assertion and the corresponding contract; compare one small input manually |
| A run pauses unexpectedly | Remove input() and breakpoint() from imported code; put demonstrations under a main guard |
| Permission denied writing output | Close the file in other programs and use the lesson's own output directory |
| PostgreSQL connection refused | Check the native server is running and its port matches the live-lab configuration |
| Authentication failure | Use your own database account; keep the password out of code and Git |
| Package installation cannot find a compatible wheel | Confirm Python 3.13 and the interpreter architecture before changing versions; preserve the error for diagnosis |

Run python -m pip freeze with the explicit environment interpreter to inspect installed versions. Do not commit the environment folder. The repository ignores .venv-python-de, output, caches and .env files.

Continue with [how to study independently](self-study.md), then [C09-L01](09-errors-and-types/01-exceptions/guide.md).
