# Help — Nested conditions and validation order

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Write the checks in the required order. Do not call int until the format checks pass.
~~~python
raw = " 42 ".strip()
format_ok = raw.isascii() and raw.isdecimal()
~~~
Inside the final else, numeric comparisons become possible. If '101' is accepted, check the inclusive upper bound. If '-1' reaches a range check, you have changed the required format rule.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why does validation order change the reported error? Why should parsing happen after the character guard?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
