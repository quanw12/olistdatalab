# C07-L04: Aliases, shallow copies, and nested data
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Create original = [["Hanoi", 30], ["Hue", 28]].
# 2. Make alias by assignment, shallow by .copy(), and deep by copy.deepcopy.
# 3. Change alias[0][1] to 31.
# 4. Append ["Da Nang", 29] to shallow.
# 5. Print original, shallow, and deep in that order.
# 6. Explain which outer and inner objects are shared.
#
# Additional checks: Mutating deep[1][1] afterward must not affect original. Adding an outer element to shallow must not extend original.
# Reflection: Why does a shallow copy not isolate nested rows? What is the difference between changing a row cell and replacing a whole row?
# Write your implementation below.
