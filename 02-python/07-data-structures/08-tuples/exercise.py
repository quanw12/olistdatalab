# C07-L08: Tuples and fixed-shape records
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Create reading = ("Hanoi", "2026-10-01", 31.0).
# 2. Unpack it into city, observed_date, and temperature.
# 3. Build key = (city, observed_date), and print key.
# 4. Print temperature and the length of a one-item tuple containing city.
# 5. In a scratch run, attempt reading[0] = "Hue"; inspect the error, then remove the failing assignment.
#
# Additional checks: Use a two-field tuple for the key, not a concatenated string. A tuple containing a list has different mutability/hashability properties.
# Reflection: What creates a one-item tuple? Can a tuple contain an object that is itself mutable?
# Write your implementation below.
