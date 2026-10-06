# C07-L07: Comprehensions and small lambda expressions
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Use raw_cities = [" hanoi ", "", " hue ", "   "].
# 2. Build clean_cities with one comprehension: strip each value, title-case it, and omit values empty after stripping.
# 3. Print clean_cities.
# 4. Use rows = [["Hanoi", 31], ["Hue", 29], ["Da Nang", 30]].
# 5. Sort rows by temperature descending using a lambda key, then print the sorted rows.
# 6. Keep rows unchanged.
#
# Additional checks: The whitespace-only string must be omitted. Equal-temperature rows retain their original relative order unless you explicitly add a tie-breaker.
# Reflection: Which part of a comprehension decides whether an item is kept? Why should complex validation remain a normal loop?
# Write your implementation below.
