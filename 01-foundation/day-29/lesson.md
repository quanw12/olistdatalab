# Day 29 — Rehearse end to end and recover from failures


## Reproducibility is an observed result

A project that works only in your current terminal is hard to review. Rehearse the README in a new terminal and a fresh dedicated database, recording every missing step. Fresh does not mean deleting your earlier work.

Create weather_course_demo in pgAdmin on the server you deliberately choose. Set PGDATABASE to that name and run your saved staging/mart/ops bootstrap SQL. Confirm current_database() before loading. The existing weather_course and test DB stay separate.

## Build an evidence matrix

For each scenario record input, command, expected result, actual result, status and evidence path. Use the fixed fixtures for exact counts. A screenshot alone should not replace the command and data state needed to reproduce it.

| Scenario | Important assertion |
|---|---|
| Fresh base load | 8 distinct observations |
| Replay base | still8 |
| Next + replay | 10, correction 32.5 retained |
| Old base replay | still10, correction retained |
| Invalid raw rows | 8 accepted/2 rejected, no bad writes |
| Database failure | transaction and checkpoint unchanged |
| Retry exhaustion | finite attempts, failed run |
| Manifest failure after commit | DB may already be updated; safe replay recovers |

## Inject failures where they matter

Use controlled fakes or temporary failpoints in a dedicated test. Do not break your machine's network or production credentials to simulate an outage. Keep failure injection explicit and remove it afterward.

A failure before commit and a failure after commit have different recovery paths. Tests should prove that distinction. End-to-end means following the complete input-to-output path, not merely importing modules.

## Reconcile accounting

Input counts are per run. Stored counts describe the database. Accepted rows can update or repeat existing identities. A unique run directory and stable database state on replay are both expected. Compare values as well as counts so a regression cannot hide behind the right number of rows.

For a clean-environment rehearsal, create a separate virtual environment and install only documented dependencies. You can also use the Docker app image. Record which route you actually tested. Fix the README when you discover hidden dependencies.
