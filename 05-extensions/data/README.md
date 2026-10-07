# Supplied synthetic data

These fixtures are original teaching data, not production records. Read them, but do not overwrite them. Outputs belong under a lesson's output/ folder. Inventory events, documents and source CDC envelopes use different contracts; an API version, document revision, business event version and Kafka offset are not interchangeable.

- inventory.json: products, movements and audit rows for join/debugging labs.
- batches.json: versioned business changes for cloud and synthetic streaming work.
- documents.json: document ingestion, edits/deletes and retrieval evaluation.
- cdc.json: PostgreSQL snapshot/update/delete/null examples, including a PK-only delete.
