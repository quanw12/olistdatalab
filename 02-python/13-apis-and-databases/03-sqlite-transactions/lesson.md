# Parameterized SQL and transaction rollback

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/sqlite3.html).

## Concept and purpose

SQLite is an embedded database available in Python's standard library. Here it provides an offline transaction lab; the next lesson uses native PostgreSQL. Their SQL and parameter styles are not interchangeable.

Bind values separately from SQL: connection.execute("... WHERE id = ?", (value,)). Do not interpolate quoted text with an f-string. Parameter binding treats the value as data, including apostrophes. It does not substitute table/column names.

A transaction groups changes so they commit together or roll back on failure. With sqlite3.connect(..., autocommit=False), explicitly commit initial setup before the exercise. The connection's with block commits on success and rolls back on exception; it does not close the connection.

executemany applies one parameterized statement to multiple parameter tuples. A uniqueness constraint can prevent duplicate inserts, but ignoring conflicts also ignores corrections. This lesson handles exact replays only; the incremental lesson adds version rules.

## Syntax example

~~~python
import sqlite3
connection=sqlite3.connect(":memory:",autocommit=False)
connection.execute("CREATE TABLE sample (id TEXT PRIMARY KEY, value INTEGER CHECK(value>=0))")
connection.commit()
try:
    with connection:
        connection.execute("INSERT INTO sample VALUES (?,?)",("A",3))
    print(connection.execute("SELECT value FROM sample").fetchone()[0])
finally:
    connection.close()
~~~

## Trace

The successful transaction stores 3. close is explicit because the transaction context does not close the connection.

## DE connection

A failed batch should not leave its first few rows committed.

Use [exercise.py](exercise.py) for the exact input/output contract.
