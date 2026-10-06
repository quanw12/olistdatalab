# C09-L02 — Logging and observable failures
# Implement your own solution below the problem statements.
#
# Implement emit_event(logger, event, details) -> dict.
# Build a NEW dictionary containing event plus only allowlisted details: run_id, accepted, rejected.
# Call logger.info exactly once with that dictionary as its sole argument, then return it.
# Do not mutate details. Drop all other fields, including token/password.
# Logger is any supplied object with an info method; do not configure global logging here.
#
# Read expected.md for concrete cases and help.md for graded hints.
