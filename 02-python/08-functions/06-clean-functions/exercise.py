# C08-L06: Clean functions and a weather-report mini-project
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# Build an in-memory weather report using only concepts already taught.
#
# Provided input to create in your implementation:
# rows = [
#     {"city": " hanoi ", "temperature": 31},
#     {"city": "Hue", "temperature": 29},
#     {"city": "Hanoi", "temperature": 33},
#     {"city": " da nang ", "temperature": 30},
#     {"city": "Hue", "temperature": 31},
#     {"city": "", "temperature": 28},
#     {"city": "Hanoi", "temperature": "hot"},
#     {"city": "Hue", "temperature": 55},
# ]
#
# 1. Define normalize_city(value): return collapsed-whitespace title-case text for strings; return "" for other types.
# 2. Define validate_record(row): the row itself is a dictionary. Return (clean_record, None) when accepted, otherwise (None, reason).
# 3. Validate in this order: normalized city must be nonempty (reason "city missing"); temperature must have exact type int or float, excluding bool (reason "temperature not numeric"); it must be from -20 through 50 inclusive (reason "temperature outside range").
# 4. A clean_record contains only city and temperature. Construct a new dictionary; do not change row.
# 5. Define summarize_weather(rows): call validate_record, count accepted/rejected, count rejection reasons, and group accepted temperatures by city.
# 6. Return a dictionary with accepted_count, rejected_count, rejection_reasons, and cities. Each cities entry maps a city to {"count": n, "average": numeric_mean}.
# 7. At top level, call summarize_weather and print accepted/rejected counts, then city lines sorted by city, then reason lines sorted by reason. Format city averages to one decimal place. The exact layout is in expected.md.
# 8. Run the empty-input and invalid-type cases in expected.md. Explain how each helper contributes. No files, APIs, pandas, or database are needed for this in-memory contract.
#
# Additional checks: summarize_weather([]) must return {"accepted_count": 0, "rejected_count": 0, "rejection_reasons": {}, "cities": {}}.
# validate_record({"city": "Hue", "temperature": True}) returns (None, "temperature not numeric").
# validate_record({"city": None, "temperature": 999}) returns (None, "city missing") because city is checked first.
# Temperatures -20 and 50 pass; -21 and 51 fail. NaN/infinity, if supplied as floats, fail the chained range check.
# Missing temperature is treated as not numeric. Missing city is treated as city missing.
# All-invalid input returns no city summaries. The original rows must remain unchanged.
# Calling summarize_weather twice with the same rows returns equal dictionaries and does not accumulate earlier counts.
# Reflection: Why must validation order be explicit? How does returning data make the report easier to test and reuse?
# Write your implementation below.
