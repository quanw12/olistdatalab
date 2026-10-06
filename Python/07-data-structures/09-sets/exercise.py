# C07-L09: Sets, membership, and stable deduplication
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Use incoming = ["Hue", "Hanoi", "Hue", "Da Nang", "Hanoi"].
# 2. Build an ordered unique list using seen plus an output list.
# 3. Print that ordered list and duplicate_count.
# 4. Compare expected_cities = {"Hanoi", "Hue", "Can Tho"} with the seen set.
# 5. Print sorted missing cities (expected but not seen), then sorted unexpected cities (seen but not expected).
#
# Additional checks: An empty incoming list gives [] and zero duplicates; all expected cities are then missing. Never compare the unsorted display order of a set.
# Reflection: Why does list(set(values)) not promise first-seen order? Why does {} not make an empty set?
# Write your implementation below.
