# C14-L01 — Incremental state, replays, and corrections
# Implement your own solution below these problem statements.
#
# Implement merge_latest(existing, incoming) -> list[dict].
# Inputs are clean records with order_id, city, amount_cents, canonical UTC updated_at. Existing IDs are unique.
# Insert unseen IDs; replace only with a strictly newer version.
# Equal version + identical record is a replay; equal version + different content raises ValueError.
# Ignore older versions. Return new dictionaries sorted by order_id and do not mutate input.
# Multiple incoming entries for one ID follow the same rules in input order.
# See help.md for hints and expected.md for cases.
