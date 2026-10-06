# Hints for DE03

## First hint

Compare the key from the first row with the second row, character by character. Then inspect what an assignment to an existing dictionary key does to its previous value.

## Exact debugger sequence

Run the PowerShell command from lesson.md. At (Pdb), enter one line at a time:

~~~text
b 8
c
n
p row
n
p customer_id
n
p totals
where
~~~

You have now inspected the first row and its dictionary write. Continue with n and the p commands to inspect later iterations. If you modified buggy.py, use l to find the loop's actual line instead of assuming it is still line 8. Use q to leave; normal completion under pdb may restart the program.

## Syntax to investigate

- text.strip() returns text with surrounding whitespace removed.
- mapping.get(key, default) reads a value or supplies the default when missing.
- mapping[key] = value stores/replaces a value for that key.
- total + increment creates the next aggregate amount.

Use those operations to reason about state before and after each row. A repeated customer is another amount to aggregate. Return the new mapping after processing all rows; returning from inside the loop stops early.

## Tests

Use unittest.TestCase and assertEqual from the lesson example. Import build_report from buggy first to capture a failure, then from exercise after implementing. Use copy.deepcopy on a small input to test that it was not modified. Include one case with the same customer separated by another customer's row, not only adjacent repetition.

If unittest reports 0 tests, check the test_ method name and TestCase inheritance; that is not a passing exercise. If the supplied checker says “implement build_report first”, compare your definition name and imported exercise.py. Run from the lesson folder for your test import.

Profile only the corrected implementation. Benchmark assertions fail if the aggregate is incorrect. The profile is not a substitute for correctness tests and does not need to be committed as a binary artifact.
