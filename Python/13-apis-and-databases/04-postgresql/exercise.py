# C13-L04 — Native PostgreSQL with Psycopg
# Implement your own solution below these problem statements.
#
# Implement upsert_postgres(connection, rows) -> None.
# Rows contain order_id, city, amount_cents and aware updated_at values/strings.
# Use one connection.transaction() block and one cursor context with executemany.
# Bind ordered value tuples with %s placeholders into orders.
# ON CONFLICT(order_id) update city, amount_cents, updated_at only when the incoming timestamp is strictly newer.
# Do not create/drop tables, close the connection or interpolate values.
# Run check.py offline first; follow live-lab.md for the real integration check.
# See help.md for hints and expected.md for cases.
