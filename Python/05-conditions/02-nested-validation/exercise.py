# C05-L02: Nested conditions and validation order
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Set raw_humidity to a test string, then strip surrounding whitespace.
# 2. Print missing if the stripped string is empty.
# 3. Otherwise print bad format if it is not ASCII decimal digits.
# 4. Otherwise convert it to int. Print out of range if it is above 100; otherwise print accepted.
# 5. Rerun for " ", "72", "100", "101", "-1", and "12.5".
#
# Additional checks: Each run prints one result. ' 72 ' is accepted after stripping. No exception handler is required because the input contract and guards control conversion.
# Reflection: Why does validation order change the reported error? Why should parsing happen after the character guard?
# Write your implementation below.
