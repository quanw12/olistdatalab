# C12-L03 — Parquet and explicit storage schemas
# Implement your own solution below these problem statements.
#
# Implement write_read_parquet(rows, path) -> list[dict].
# Rows contain order_id, city, amount_cents, updated_at.
# Build a DataFrame with those columns even for empty rows; use pandas string dtype for text and int64 for cents.
# Write using pyarrow, index=False; read back and return records in original order.
# Parent directory exists. Overwrite on rerun; do not mutate rows.
# See help.md for hints and expected.md for cases.
