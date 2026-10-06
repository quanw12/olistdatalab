# C13-L03 — Parameterized SQL and transaction rollback
# Implement your own solution below these problem statements.
#
# Implement load_sqlite(connection, rows) -> int.
# The provided connection has a committed table orders(order_id TEXT PRIMARY KEY, city TEXT NOT NULL, amount_cents INTEGER CHECK(amount_cents>=0), updated_at TEXT NOT NULL).
# Rows are dictionaries with those fields. In one transaction, executemany a parameterized INSERT ... ON CONFLICT(order_id) DO NOTHING.
# Return the number actually inserted (cursor.rowcount). Do not close the caller's connection or create/drop tables.
# Any constraint failure must propagate and roll back the entire batch.
# See help.md for hints and expected.md for cases.
