# CL07 — Learn

## Estimate before execution

BigQuery dry runs estimate query bytes without executing the query. An on-demand query's maximum_bytes_billed can reject a query above a byte limit. This does not cap Cloud Run, Storage, builds or your total cloud bill. Actual price/limits vary; check your project's billing model and current pricing.

## Syntax — Python

~~~python
from google.cloud import bigquery
cfg = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
job = client.query(sql, job_config=cfg)
estimated = job.total_bytes_processed
run_cfg = bigquery.QueryJobConfig(maximum_bytes_billed=chosen_byte_limit)
~~~
Call result() for the actual execution and record processed/billed bytes. Partition pruning and selecting required columns reduce scanned data; a LIMIT alone generally does not establish a scanned-byte bound. [Query documentation](https://docs.cloud.google.com/bigquery/docs/running-queries).

Cleanup is a deliverable: inventory owned resources, pause triggers, retain useful sanitized evidence, then remove only the lab resources you intend to retire.

[Assignment](exercise.md) · [Hints](help.md)
