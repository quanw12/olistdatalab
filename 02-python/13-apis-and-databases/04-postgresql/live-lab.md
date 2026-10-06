# Native PostgreSQL integration lab

Use pgAdmin and your installed PostgreSQL server. No Docker is required.

1. In pgAdmin, connect to your local server. Under Databases, create a dedicated database named python_de_lab using the graphical Create > Database dialog.
2. Install the optional driver in the extension environment:
~~~powershell
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" -m pip install "psycopg[binary]>=3.2,<4"
~~~
3. In this lesson's terminal, set connection details. Replace the username/port if your installation differs:
~~~powershell
$env:PGHOST = "localhost"
$env:PGPORT = "5432"
$env:PGDATABASE = "python_de_lab"
$env:PGUSER = "postgres"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check_live.py
~~~
The checker prompts for the password with getpass, so it is not echoed or stored in this file. It creates a TEMP table orders, commits setup, exercises your function, and closes the connection. Temporary tables disappear automatically. It does not create/drop a persistent table.

Expected: PASS: PostgreSQL insert/correction/replay/rollback.

If connection is refused, verify the server service and port. If authentication fails, use the same account that works in pgAdmin. A missing database must be created first. A SQL syntax or constraint error after connection belongs to the exercise implementation.

The offline checker cannot substitute for this check. No live database verification was claimed when preparing the course.
