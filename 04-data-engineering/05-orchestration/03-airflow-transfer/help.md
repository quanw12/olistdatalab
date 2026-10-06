# Help — Airflow concepts and orchestration transfer

## First hint

Reuse the library; keep logic out of framework glue.

## Detailed approach

Start schedule=None. Translate dependencies/failure propagation, then read intervals/timetables before scheduling daily. Do not copy old airflow db init commands unchecked. Separate Airflow dependencies from dbt/Prefect. Pass a storage path rather than a whole dataset as task metadata.

## Troubleshooting

A Python import is not an executed DAG. catchup=False does not solve source event-time correctness.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

