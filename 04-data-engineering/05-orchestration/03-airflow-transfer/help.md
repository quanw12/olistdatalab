# Help — Airflow concepts and orchestration transfer

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Reuse the library; keep logic out of framework glue.

</details>

<details>
<summary>Detailed approach</summary>

Start schedule=None. Translate dependencies/failure propagation, then read intervals/timetables before scheduling daily. Do not copy old airflow db init commands unchecked. Separate Airflow dependencies from dbt/Prefect. Pass a storage path rather than a whole dataset as task metadata.

</details>

<details>
<summary>Troubleshooting</summary>

A Python import is not an executed DAG. catchup=False does not solve source event-time correctness.

</details>
