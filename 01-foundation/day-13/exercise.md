# Day 13 — Load PostgreSQL from Python


1. Write schema.sql for staging.weather_observations using the shared contract; execute it once on empty weather_course.
2. In load.py implement validation, load_records(connection, rows), an argparse --input CLI, and main. Use parameterized SQL and one transaction.
3. Load ../data/weather_batch.json twice. Report input count and stored count.
4. Change humidity to110 in a COPY of the input. Reject this batch before writes. Separately demonstrate rollback after a database CHECK failure in a scratch transaction.
5. Explain who commits, EXCLUDED, and why SQL values are passed separately.

Write the full implementation yourself; keep passwords outside code.
