# C07-L10: Dictionaries, nested records, and aggregation
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Create rows = [{"city": "Hanoi"}, {"city": "Hue"}, {"city": "Hanoi"}, {"city": ""}, {}].
# 2. Get each city with an empty-string default, then strip it.
# 3. Count blank/missing cities in rejected_count; skip them.
# 4. Build city_counts for valid rows.
# 5. Print each city and count in sorted city-name order as <city>: <count>.
# 6. Print rejected: <rejected_count>.
# 7. Keep the input records unchanged.
#
# Additional checks: The given city values are strings when present. Supporting None or other types is a later contract extension; do not assume get replaces present None. Empty rows input produces rejected: 0 and no city lines.
# Reflection: What is the difference between a missing key and a key with None? Why must the grouping dictionary be created before the loop?
# Write your implementation below.
