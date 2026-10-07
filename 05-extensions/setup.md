# Extension setup — install at the boundary you are learning

[Course](README.md) · [Sources](sources.md)

## Local core: Python and SQLite

Engineering Labs, cloud concept checks and AI Data core use only Python's standard library. Reference checks use Windows Python 3.13; Python 3.14 can run these standard-library tasks if its SQLite includes FTS5. Do not recreate a working venv blindly; inspect its interpreter first. No server/paid account is needed for these checks.

~~~powershell
Set-Location "C:\DE Courses"
python --version
python -m venv .venv-extensions
& "./.venv-extensions/Scripts/python.exe" --version
& "./.venv-extensions/Scripts/python.exe" -c "import sqlite3; print(sqlite3.sqlite_version); c=sqlite3.connect(':memory:'); c.execute('CREATE VIRTUAL TABLE probe USING fts5(text)'); print('FTS5 available')"
& "./.venv-extensions/Scripts/python.exe" "05-extensions/checks/check.py" LAB01
~~~

The starter check should FAIL because query.sql is unfinished. Use the exact venv interpreter in guides; no activation is necessary. Databases/profiles/output are ignored. The checker creates isolated in-memory databases and does not read/change previous practice databases.

## Optional GCP live mode

Use [the cloud live lab](02-cloud/live-lab.md). You need an owned project, compatible resource locations, deliberate billing/budget choices, the CLI and Docker only when building the worker. Install the Python clients at CL02, not at the start of Part 5:

~~~powershell
Set-Location "C:\DE Courses"
& "./.venv-extensions/Scripts/python.exe" -m pip install -r "05-extensions/requirements-cloud.txt"
& "./.venv-extensions/Scripts/python.exe" -m pip check
~~~

Pins were checked against package metadata, not an authored cloud deployment. Local ADC and attached runtime identities are different. Do not create/download service-account private keys. Cloud runtime writes only to your listed lab resources. Choose local-only mode and label it accurately when deployment is unavailable.

## Optional real embeddings

Use [embedding-lab.md](03-ai-data/embedding-lab.md) after AI05. It creates .venv-embeddings, checks compatible packages and downloads a model to an ignored cache only when you deliberately run it. Core vector fixtures have no model dependency and prove only the numeric contract. Record real model/revision and measured retrieval results separately.

## Live Kafka/CDC

Use [the streaming live lab](04-streaming/live-lab.md) after Linux Docker/Compose. The supplied stack is named p5-streams, binds localhost and uses owned volumes. Native PostgreSQL/pgAdmin remains separate: container source17 is mapped to 55432; Kafka 19092; Connect 18083. Do not stop other projects' containers or delete course databases.

~~~powershell
Set-Location "C:\DE Courses"
& "./.venv-extensions/Scripts/python.exe" -m pip install -r "05-extensions/requirements-streaming.txt"
& "./.venv-extensions/Scripts/python.exe" -m pip check
~~~

The live stack is not started during preparation. Compose configuration validation is not a running-broker test. Consumer restart preserves volumes/group/sink; source reset requires a deliberate new source epoch and matching progress state.

## When an environment fails

Record shell, interpreter, version, exact command and error. Distinguish logic failures from missing FTS5, SDK wheels, credentials, billing, Docker daemon or broker addressing. Use the shared [study guide](../docs/study.md). Do not weaken a contract to accommodate a missing external service. Never claim live/model completion from an offline PASS.
