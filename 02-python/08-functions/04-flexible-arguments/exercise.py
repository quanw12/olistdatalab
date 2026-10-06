# C08-L04: Collect and unpack arguments with * and **
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Define average_of(*values), returning None for no values and the arithmetic mean otherwise.
# 2. Print average_of(28, 30, 32), average_of(), and average_of(*[0, 10]).
# 3. Define describe_batch(name, **metadata), returning {"name": name, "metadata_keys": sorted(metadata)}.
# 4. Print describe_batch("demo", source="fixture", city="Hue").
# 5. Explain why average_of([28, 30]) is outside this numeric-varargs contract.
#
# Additional checks: Do not silently flatten arbitrary nested inputs. Keep the input contract as zero or more numeric positional arguments.
# Reflection: What do * and ** mean in a definition versus a call? Why are explicit parameters often easier to validate?
# Write your implementation below.
