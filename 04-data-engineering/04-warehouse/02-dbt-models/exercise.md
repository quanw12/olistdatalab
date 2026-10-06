# DE13 assignment

Fill project/dbt/models/stg_changes.sql, latest_changes.sql and mart_customer.sql. Stage the changes seed into explicit strings, TIMESTAMPTZ and integer types. Select latest versions including deletes. Mart aggregates active latest by customer_id into order_count and total_cents. Use refs and explicit materializations. Run seed/build, inspect compiled SQL and generate docs.

## Deliverables

Three SQL models and notes.md describing seed -> stage -> latest -> mart.

## Reflection

Does ref ingest an API?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

