# C08-L03: Return values, early return, and scope
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Define summarize_temperatures(values).
# 2. For empty input, return {"count": 0, "minimum": None, "maximum": None, "average": None}.
# 3. For nonempty numeric input, return the same keys with computed values.
# 4. Do not print inside the function and do not mutate values.
# 5. Print the returned dictionaries for [29.0, 31.0, 33.0], [], and [0.0], using the key insertion order shown above.
#
# Additional checks: A valid zero reading must not be mistaken for absent input. Only the caller prints. Reuse the returned average in another expression to demonstrate it is available.
# Reflection: Why is print not a replacement for return? Can a function mutate an argument despite its variable names being local?
# Write your implementation below.
