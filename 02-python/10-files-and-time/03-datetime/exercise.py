# C10-L03 — Aware time, UTC, and deterministic clocks
# Implement your own solution below the problem statements.
#
# Implement utc_text(text) -> str.
# Accept an ISO datetime string with a timezone offset (including Z), parse it, reject naive values with ValueError.
# Return the equivalent UTC ISO string with microsecond precision and +00:00, preserving the instant.
# For this function inputs are strings; malformed strings raise ValueError.
# Example: 2026-10-01T08:00:00+07:00 -> 2026-10-01T01:00:00.000000+00:00.
#
# Read expected.md for concrete cases and help.md for graded hints.
