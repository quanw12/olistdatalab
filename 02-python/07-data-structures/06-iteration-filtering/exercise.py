# C07-L06: Iterables, enumerate, zip, and filtering
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Use cities = ["Hanoi", "Hue", "Da Nang"] and temperatures = [31, 29, 30].
# 2. Pair them with zip(..., strict=True).
# 3. Build hot_cities containing names whose temperature is at least 30.
# 4. Print hot_cities.
# 5. Use enumerate(..., start=1) to print each selected city as <position>: <city>.
# 6. In a scratch run, shorten temperatures and inspect the strict zip error.
#
# Additional checks: Do not mutate cities while filtering. For all temperatures below 30, print [] and no numbered entries.
# Reflection: Why can ordinary zip hide data? Why might filter(None, readings) incorrectly remove a valid reading?
# Write your implementation below.
