# C04-L02: Comparisons and combined rules
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Define a valid reading as temperature from -20 through 50 inclusive AND humidity from 0 through 100 inclusive.
# 2. With separate named variables, print validity for (30, 75), (-20, 0), (50, 100), and (51, 70). Do not use loops yet.
# 3. For raw = "oops", print the result of raw.isdecimal() and int(raw) > 0.
# 4. Explain why the last expression does not raise ValueError.
#
# Additional checks: Test humidity = -1 and humidity = 101 separately: both fail. The isdecimal guard here accepts only digit strings, not signed or decimal numbers.
# Reflection: How is = different from ==? What exactly gets skipped during short-circuit evaluation?
# Write your implementation below.
