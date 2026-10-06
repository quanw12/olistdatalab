# Help — Capstone: deliver and recover a Linux batch pipeline

## First hint

Combine current process status/logs with fresh contract checks.

## Detailed approach

The failed one-shot command is:
~~~bash
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" run --rm batch --input /data/missing.csv --output /output
~~~
The service ENTRYPOINT still selects app.py; the trailing arguments replace its command. Record the nonzero status and the error event. Then run the valid default batch again and collect its 0 status plus successful logs and fresh report validation.

Do not use down -v to simulate ordinary restart. If a clean empty-volume rehearsal is desired later, use a different project name and record it explicitly. No production database is part of this capstone.

## Troubleshooting

curl returning the previous report while a batch failed is expected preservation, not a successful ingestion. A stale log can also mislead if you capture the wrong service/run.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
