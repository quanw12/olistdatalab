# Day 13 — Load PostgreSQL from Python


## The driver, connection, and cursor

A database driver lets Python send SQL to PostgreSQL and receive rows. We use Psycopg 3, imported as psycopg. A connection represents a database session; a cursor executes statements and reads results. The server still enforces constraints.

Create a new weather_course database in pgAdmin. Keep weather_day09 for your earlier SQL lessons. Configure PGHOST, PGPORT, PGDATABASE, PGUSER and PGPASSWORD using [setup.md](../setup.md).

## Parameter syntax

This read-only example can run before you create course tables:

~~~python
import psycopg

with psycopg.connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT %s::integer + %s::integer", (4, 5))
        answer = cursor.fetchone()
        print(answer[0])  # 9
~~~

The tuple contains values; %s is a Psycopg placeholder even for numbers. Do not quote it. A one-element tuple is (value,). F-strings and concatenation mix data into SQL text before the driver can keep values separate. Table and column identifiers cannot use value placeholders; keep identifiers fixed in this course.

## Transactions and ownership

A transaction groups writes: either all commit or all roll back. The connection context commits on normal exit, rolls back if an exception escapes, then closes the connection. The cursor context closes only its cursor. Catch a failure outside the connection block if you want rollback. Do not commit each row separately.

Our load_records(connection, rows) receives a connection and must not commit or close it. The caller owns the transaction. On Day 14, this will let staging and mart changes succeed or fail together.

## Identity and UPSERT

Read [the shared contract](../capstone/contract.md). Create staging.weather_observations with seven normalized columns. Identity is (city, observed_at, source). Including source deliberately extends Day 12's single-provider design.

UPSERT inserts a missing key or updates a conflicting one. Syntax on an unrelated table:

~~~sql
INSERT INTO example_inventory (item_code, quantity)
VALUES (%s, %s)
ON CONFLICT (item_code)
DO UPDATE SET quantity = EXCLUDED.quantity;
~~~

EXCLUDED is the incoming proposed row. A matching UNIQUE/PRIMARY KEY constraint must exist. Today incoming values replace the same identity; Day 17 adds a newer-request condition.

## Parsing before writing

json.load(file) reads a list; datetime.fromisoformat(text) parses timestamps. Require a non-null utcoffset(), finite temperature, and integral humidity. Reject bool values because Python considers bool a subtype of int. Validate all rows before opening the write transaction.

Read: [Psycopg parameters](https://www.psycopg.org/psycopg3/docs/basic/params.html), [transactions](https://www.psycopg.org/psycopg3/docs/basic/transactions.html).
