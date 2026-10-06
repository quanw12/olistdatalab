# Native PostgreSQL with Psycopg

Original Python-for-DE extension. [Source reference](https://www.psycopg.org/psycopg3/docs/basic/transactions.html).

## Concept and purpose

Psycopg connects Python to PostgreSQL. Install psycopg[binary] in the extension environment for the live lab. pgAdmin is a client; a running PostgreSQL server is still required.

Psycopg uses %s placeholders for values, even integers. Pass a tuple separately. Do not quote the placeholder or interpolate it with Python's % operator. For dynamic identifiers use psycopg.sql.Identifier rather than value placeholders.

connection.transaction() defines a transaction block. On an idle connection it commits/rolls back that transaction; inside an existing transaction it uses a savepoint. The owner must understand the connection's existing state. Our live checker commits table setup before calling your function.

An UPSERT uses a unique key to choose insert versus update. A newer source version may update an existing row. Replaying an equal/older version must not overwrite newer state. This lesson ignores equal-version conflicts; the next lesson teaches detecting them explicitly.

Credentials belong in environment configuration. Do not print a connection string containing a password. The provided live checker uses a temporary table that disappears when its connection closes.

## Syntax example

~~~python
SQL = """
INSERT INTO orders(order_id,city,amount_cents,updated_at)
VALUES (%s,%s,%s,%s)
ON CONFLICT(order_id) DO UPDATE
SET city=EXCLUDED.city, amount_cents=EXCLUDED.amount_cents,
    updated_at=EXCLUDED.updated_at
WHERE EXCLUDED.updated_at > orders.updated_at
"""
values=("A","Hue",100,"2026-10-01T01:00:00+00:00")
print(len(values))
~~~

## Trace

The four bound values remain separate from SQL. EXCLUDED refers to the proposed incoming row. No database connection is made by this syntax example.

## DE connection

Correct parameter binding, transactions and version rules protect ingestion from quoting bugs, partial writes and stale updates.

Use [exercise.py](exercise.py) for the exact input/output contract.
