# C14-L02 — Data-quality checks and fixed-clock freshness
# Implement your own solution below these problem statements.
#
# Implement quality_report(rows, now, max_age_hours=24) -> dict.
# now is an aware datetime; timestamps in rows are valid canonical aware ISO text. Reject naive now or a negative max_age_hours with ValueError.
# Return exactly: rows, duplicate_ids, blank_city, invalid_amount, stale, future.
# duplicate_ids counts occurrences after the first.
# blank_city counts nonstring/blank city. invalid_amount counts values not exact nonnegative int.
# stale counts age > threshold; future counts event time > now. Check each independently.
# No calling datetime.now inside this function; no mutation.
# See help.md for hints and expected.md for cases.
