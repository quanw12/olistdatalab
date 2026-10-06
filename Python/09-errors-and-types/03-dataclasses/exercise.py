# C09-L03 — Type hints, dataclasses, and simple objects
# Implement your own solution below the problem statements.
#
# Define @dataclass(frozen=True) class Order with fields order_id: str, amount_cents: int.
# In __post_init__, reject non-string/blank order_id with ValueError.
# Reject amount_cents unless its exact type is int and it is nonnegative (ValueError); bool is invalid.
# Implement order_dict(order) returning a NEW dictionary with those two fields.
# Preserve the provided nonblank order_id text; normalization is outside this record contract.
#
# Read expected.md for concrete cases and help.md for graded hints.
