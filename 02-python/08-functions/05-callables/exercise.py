# C08-L05: Built-ins, named functions, and lambdas
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Define normalize_city(text), returning stripped title-case text.
# 2. Define apply_to_all(values, operation), returning a new list with operation applied to each input.
# 3. Print apply_to_all([" hanoi ", " hue "], normalize_city).
# 4. Print apply_to_all([1, 2, 3], lambda value: value * value).
# 5. Print len of the first returned list.
# 6. Avoid modifying the input lists.
#
# Additional checks: Pass normalize_city without calling it at the call site. Empty values must return an empty list without calling the operation.
# Reflection: Why is passing len different from passing len(values)? What makes a function easier to test independently?
# Write your implementation below.
