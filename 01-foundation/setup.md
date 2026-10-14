# Setup and working folders

## Python

Use Python 3.13 for a consistent course environment. This machine already has a Python 3.13 installation.

Run once in PowerShell:
~~~powershell
Set-Location "C:\DE Courses"
& "C:\Users\DELL\AppData\Local\Programs\02-python\Python313\python.exe" -m venv .venv-course
.\.venv-course\Scripts\Activate.ps1
python --version
python -m pip install --upgrade pip
~~~

If the interpreter moved, use py -3.13 instead of its absolute path. If activation is blocked, invoke the environment's interpreter explicitly:

~~~powershell
& "C:\DE Courses\.venv-course\Scripts\python.exe" --version
& "C:\DE Courses\.venv-course\Scripts\python.exe" -m pip install requests
~~~

The leading & runs a quoted executable path in PowerShell. Replace python in later commands with that full invocation when activation is unavailable. No machine-wide execution-policy change is needed.

Days 1–3 use the standard library. Each later guide introduces its dependencies. Use python -m pip with the interpreter that runs the exercises:
~~~powershell
python -c "import sys; print(sys.executable)"
~~~

The path should point to .venv-course.

## Working directories

For daily practice:
~~~powershell
Set-Location "C:\DE Courses\01-foundation\day-13"
~~~
For the project from Day 14 onward:
~~~powershell
Set-Location "C:\DE Courses\01-foundation\capstone"
~~~
For Git, return to C:\DE Courses. Relative data paths depend on the working directory unless code anchors them to its own file.

## PostgreSQL and pgAdmin

Days 8–12 retain weather_day08 and weather_day09. pgAdmin is the client; PostgreSQL is the server.

Day 13 uses a separate database, **weather_course**. In pgAdmin, right-click Databases → Create → Database, enter weather_course, and choose your local owner. Open Query Tool from that database and verify SELECT current_database(); before DDL.

Set Python connection details in the current PowerShell terminal:
~~~powershell
$env:PGHOST = "localhost"
$env:PGPORT = "5432"
$env:PGDATABASE = "weather_course"
$env:PGUSER = "postgres"
$courseDbSecret = Read-Host "Local PostgreSQL password" -AsSecureString
$env:PGPASSWORD = [System.Net.NetworkCredential]::new("", $courseDbSecret).Password
~~~

Use your actual local username/port if different. Psycopg reads these PG variables. Ordinary Python does not automatically load .env. Keep passwords out of source files; .env files are ignored.

## Later services

Day 18 introduces PostgreSQL 18 in Docker on host port **5433**, separate from the local server on 5432. Initialize the container database using your own DDL and loader; local tables do not migrate automatically.

Days 20–21 use a local Prefect server and runner in separate terminals. Keep them open for scheduling; the lesson does not install a permanent background service.

## Evidence

Intermediate data goes in ignored output/. Small selected charts and sanitized logs for the portfolio go in evidence/ and can be committed. Record the input fixture behind every result.

Sources: [venv](https://docs.python.org/3.13/library/venv.html), [PostgreSQL environment variables](https://www.postgresql.org/docs/18/libpq-envars.html), [pgAdmin databases](https://www.pgadmin.org/docs/pgadmin4/latest/database_dialog.html).
