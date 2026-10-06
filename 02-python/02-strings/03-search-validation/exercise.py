# C02-L03: Search strings and define validation limits
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Use filename = " WEATHER.CSV " and code = "0042".
# 2. Trim/lowercase filename, then print whether it ends with ".csv".
# 3. Print the index returned when finding "rain" in the normalized filename.
# 4. Print whether code contains only ASCII decimal digits.
# 5. Print whether "-7" is decimal-only and whether an empty string is decimal-only.
# 6. Print whether "meteo" occurs in "open-meteo".
#
# Additional checks: Repeat the code validation using Arabic-Indic digits '١٢': isdecimal alone passes, but the specified ASCII-only rule must fail.
# Reflection: Why is a digit-character test insufficient for a decimal number such as '-7.5'? Why is find's missing result different from index?
# Write your implementation below.
