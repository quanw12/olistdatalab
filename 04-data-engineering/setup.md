# Engineering setup and environment boundaries

## Start with concepts, install only at the matching lesson

DE01–DE02 need only your editor and fixture inspection. DE03/DE04/DE08/DE09/DE10/DE16/DE22/DE24 checks need only Python standard library. PostgreSQL begins in DE05–DE06 and reuses your native pgAdmin/server. Warehouse packages begin in DE12–DE13. Prefect reuses foundation Days 20–21. Docker skills come from Linux LE16 onward. Airflow/Spark/cloud runtime remain optional.

Nothing here installs a server, starts a service or provisions a cloud account automatically.

## Windows PowerShell — a separate environment

~~~powershell
Set-Location "C:\DE Courses"
python --version
python -m venv .venv-engineering
& "./.venv-engineering/Scripts/python.exe" --version
& "./.venv-engineering/Scripts/python.exe" "04-data-engineering/checks/check.py" DE03
~~~

The initial checker should FAIL with 'implement build_report first'; the starter is intentionally unfinished. Existing Python environments and learner files are separate. Avoid changing the system Python or activating multiple environments. If .venv-engineering already exists, inspect its interpreter and reuse it instead of recreating it blindly.

At DE12:
~~~powershell
& "./.venv-engineering/Scripts/python.exe" -m pip install -r 04-data-engineering/requirements-warehouse.txt
& "./.venv-engineering/Scripts/python.exe" -m pip check
& "./.venv-engineering/Scripts/dbt.exe" --version
~~~

Direct versions were installed and reference transformations tested in an isolated Windows Python 3.13 author environment. requirements-warehouse pins direct dependencies, not a full transitive lock. If installation fails, record Python version/full error; prefer matching the verified interpreter before changing random packages. Do not mix this environment with Airflow/Spark.

## Native PostgreSQL — your current pgAdmin

Use a new learning database to preserve previous exercises. Connect to the native server in pgAdmin, right-click Databases -> Create -> Database and name it engineering_lab. Confirm the Query Tool is connected there:
~~~sql
SELECT current_database(), current_user, version();
~~~

DE05 creates your own schema; DE06 teaches transactions with your own implementation. Reuse the [Python native PostgreSQL lab](../02-python/13-apis-and-databases/04-postgresql/live-lab.md) for driver/authentication setup. At DE06, if this new environment lacks the driver:
~~~powershell
& "./.venv-engineering/Scripts/python.exe" -m pip install "psycopg[binary]>=3,<4"
$env:PGHOST = "localhost"
$env:PGPORT = "5432"
$env:PGDATABASE = "engineering_lab"
~~~
Set PGUSER to your actual local database role. Use a prompted password or your existing local credential mechanism; never commit it, paste it into notes, or hard-code it. Your loader can call getpass.getpass when PGPASSWORD is unset. SQL examples use PostgreSQL syntax unless labeled DuckDB/GoogleSQL/dbt.

No live PostgreSQL test is claimed merely from an offline checker. Verify transactions from a new connection after commit/rollback.

## dbt/DuckDB — local file warehouse

Configuration and the tiny seed are supplied; model SQL is unfinished. Run from its project folder:
~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\project\dbt"
& "C:/DE Courses/.venv-engineering/Scripts/dbt.exe" debug --profiles-dir .
~~~

profile points to warehouse.duckdb in this working directory. It contains synthetic lab data only. DE13 commands build the models; DE14 adds tests; DE15 adds incremental state. target/, logs/ and warehouse files are ignored. Do not run two writers concurrently. Close your own reader connections before building.

## Ubuntu, Docker and CI

Follow [Linux setup](../03-linux/setup.md) for Ubuntu/WSL. Windows venv executables are not a Linux venv. Use a Linux-native environment for Bash/runtime:
~~~bash
export ENG_COURSE_ROOT='/mnt/c/DE Courses/04-data-engineering'
export ENG_LAB_ROOT="$HOME/de-labs/engineering"
mkdir -p "$ENG_LAB_ROOT"
python3 -m venv "$ENG_LAB_ROOT/venv"
"$ENG_LAB_ROOT/venv/bin/python" -m pip install -r "$ENG_COURSE_ROOT/requirements-warehouse.txt"
~~~
This Linux installation is learner runtime evidence; the author verified Windows for the warehouse reference. Use python >=3.10 and record the exact interpreter; Python 3.13 is the author reference. Linux courses' LE variables remain separate.

Keep active GitHub workflows under the repository's .github/workflows only when you deliberately activate your finished draft. CI should run offline tests first; real database/container integration is a separately configured job. No workflow is activated during material preparation.

## Prefect and optional tools

Use foundation Day 20 setup, install Prefect 3 in its separate orchestration environment and record the version. DE17 manual runs precede schedules. Explicitly configure the local server if you want UI evidence.

DE18 links current Airflow 3 instructions; do not install it into the warehouse environment. DE21 links version-specific PySpark installation; match Java/Python requirements to the chosen release. DE20 uses a sandbox only, with billing disabled; if unavailable, the local warehouse is sufficient for the core.

## Independent file checks

All guide commit commands are in Windows PowerShell. Most data exercises are Python/SQL, not Bash. Every syntax example identifies its language. Errors about a missing database, package or daemon are environment failures; isolate them from logic tests. Keep generated artifacts under an output/ directory or native lab path, never in source fixtures.

