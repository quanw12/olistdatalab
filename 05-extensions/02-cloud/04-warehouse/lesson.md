# CL04 — Learn

## Keep raw events and current entities distinct

History contains several revisions of one event_id. The current table has one row per ID, including a delete marker. Rank history by business version, then select latest rows; remove tombstones only in an active report. Filtering deletes before ranking resurrects old records.

## Syntax — portable SQL / GoogleSQL

~~~sql
ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY version DESC)
~~~
A window numbers rows inside each entity. Equal-version differing payloads are contract conflicts: detect them before materialization. An arbitrary tie-breaker hides the problem. Repeated identical revisions may be deduplicated.

In BigQuery, staging/load jobs and MERGE have separate boundaries. A deterministic load job ID helps recover an uncertain load request; inspect job.result() and the existing job when a request ID already exists. It does not create a cross-service transaction. [Load documentation](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-json).

[Assignment](exercise.md) · [Hints](help.md)
