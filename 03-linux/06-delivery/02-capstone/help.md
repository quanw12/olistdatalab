# Help — Capstone: deliver and recover a Linux batch pipeline

Keep this closed until the timed/independent attempt ends. Reading an approach first makes the attempt guided practice; record that honestly.

<details>
<summary>First hint</summary>

Combine current process status/logs with fresh contract checks.

</details>

<details>
<summary>Detailed approach</summary>

The failed one-shot command is:
~~~bash
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" run --rm batch --input /data/missing.csv --output /output
~~~
The service ENTRYPOINT still selects app.py; the trailing arguments replace its command. Record the nonzero status and the error event. Then run the valid default batch again and collect its 0 status plus successful logs and fresh report validation.

Do not use down -v to simulate ordinary restart. If a clean empty-volume rehearsal is desired later, use a different project name and record it explicitly. No production database is part of this capstone.

</details>

<details>
<summary>Troubleshooting</summary>

curl returning the previous report while a batch failed is expected preservation, not a successful ingestion. A stale log can also mislead if you capture the wrong service/run.

</details>
