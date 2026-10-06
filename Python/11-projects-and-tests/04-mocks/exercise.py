# C11-L04 — Dependency injection and mocked HTTP
# Implement your own solution below these problem statements.
#
# Implement fetch_count(client) -> int.
# Call client.get("/orders", timeout=5) exactly once.
# Call response.raise_for_status() before response.json().
# Require a dict with count whose exact type is int and value is nonnegative; otherwise raise ValueError.
# Return count. Propagate client/status exceptions unchanged. Do not construct a real client.
# See help.md for hints and expected.md for cases.
