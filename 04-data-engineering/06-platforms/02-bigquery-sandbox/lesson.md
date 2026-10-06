# An optional BigQuery sandbox lab

## Understand it

A sandbox can expose warehouse query behavior without enabling billing. Its capabilities differ from a paid project, and table expiry means it is not durable portfolio storage. As inspected on Oct 6, 2026, current docs list no DML/streaming/Data Transfer Service, automatic expiry after 60 days, a lifetime storage allowance and a monthly processed-query allowance. Recheck before use.

## Syntax and trace

~~~sql
-- GoogleSQL syntax pattern. Replace the project/dataset explicitly.
SELECT customer_id, COUNT(*) AS order_count, SUM(amount_cents) AS total_cents
FROM `your_project.engineering_lab.active_orders`
GROUP BY customer_id;
~~~

An analytical SELECT is permitted; do not assume the sandbox supports your local UPSERT/MERGE workflow.

## Engineering connection

Transfer local warehouse concepts with precise dialect and platform limits.

[Reference](https://docs.cloud.google.com/bigquery/docs/sandbox). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

