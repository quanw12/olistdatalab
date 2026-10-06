# Capstone: reproducible retail ingestion

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/sqlite3.html).

## Concept and purpose

This project combines the language skills into one local pipeline: raw CSV -> validation/quarantine -> latest order state -> report and manifest. It uses the fixed fixtures in 02-python/data, with no live API or account dependency.

Define one clean row as the latest snapshot for an order_id. updated_at is a source version in UTC; amount_cents is exact integer money. Preserve bad source rows separately with one deterministic reason.

Use a content hash of source bytes as a batch identity. In one database transaction, apply the state changes and record the successful batch. A failed transaction must not record completion. A previously applied file may be recognized, but output artifacts still need rebuilding if publication failed afterward.

The database and filesystem are separate transactional systems. Commit data first, then write each artifact through atomic file replacement. Publish manifest last as an operational completion signal. This does not create a multi-file or database-plus-files atomic transaction. On failure, rerun the same input to rebuild artifacts without duplicating data. Concurrent-reader snapshots would need a stronger versioned-output design.

This is deliberately a single-writer lab. Reuse your completed parsing/validation helpers or copy them into small sibling modules. The exercise file remains the public entry point for the checker. Do not import code from a lesson that still has unimplemented prompts.

## Syntax example

~~~python
import hashlib
payload=b"order_id,amount\nA1,10.00\n"
batch_id=hashlib.sha256(payload).hexdigest()
print(len(batch_id))
print(batch_id==hashlib.sha256(payload).hexdigest())
~~~

## Trace

SHA-256 gives a 64-character hexadecimal identity; identical source bytes produce the same batch ID. It identifies bytes, not semantic equality between differently formatted files.

## DE connection

An internship portfolio should demonstrate reruns, corrections, failures and recovery, not only one successful run.

Use [exercise.py](exercise.py) for the exact input/output contract.
