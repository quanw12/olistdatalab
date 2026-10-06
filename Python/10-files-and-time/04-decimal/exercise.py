# C10-L04 — Decimal parsing and exact money
# Implement your own solution below the problem statements.
#
# Implement to_cents(text) -> int.
# Require a str; nonstrings raise TypeError. Strip text and parse Decimal; malformed, nonfinite, negative, or greater than 1000000 units raises ValueError.
# Reject any fractional cent (1.001 invalid, 1.2300 valid).
# Return exact integer cents. Zero is valid. Never round away invalid sub-cent precision.
#
# Read expected.md for concrete cases and help.md for graded hints.
