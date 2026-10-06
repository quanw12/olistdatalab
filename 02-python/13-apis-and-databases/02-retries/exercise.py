# C13-L02 — Retry only transient failures
# Implement your own solution below these problem statements.
#
# Implement retry(operation, sleep, max_attempts=3).
# Require exact positive int max_attempts, otherwise ValueError.
# Call operation until success and return its result.
# Catch only TimeoutError. Sleep 1, then 2, then 4, ... seconds BETWEEN retryable failed attempts.
# After the final failure re-raise TimeoutError without another sleep.
# Propagate other exceptions immediately. No real sleep or network calls in the checker.
# See help.md for hints and expected.md for cases.
