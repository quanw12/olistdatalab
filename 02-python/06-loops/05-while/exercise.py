# C06-L05: while loops and guaranteed progress
# Read lesson.md first. Open help.md only when you need a hint.
# All lines below are problem statements; implement your own solution.
#
# 1. Set attempt = 1, max_attempts = 3, and success_at = 2.
# 2. While attempts remain, print attempt: <number>.
# 3. If attempt equals success_at, print success and break.
# 4. Otherwise increment attempt. Use the loop's else to print exhausted if the loop ends without success.
# 5. Rerun with success_at = 5, then with max_attempts = 0.
#
# Additional checks: Never perform more than max_attempts iterations. This is a simulation; no sleeps or API calls are needed.
# Reflection: Why can a while loop run zero times? What guarantees that this retry simulation terminates?
# Write your implementation below.
