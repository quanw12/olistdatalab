# Help — Comparisons and combined rules

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Write one expression per specified pair or reassign the variables between prints. Keep the two range rules in parentheses.
~~~python
raw = ""
can_parse_positive = raw.isdecimal() and int(raw) > 0
print(can_parse_positive)
~~~
The right side is skipped for empty/nondecimal input. If your code crashes, check operand order. Do not put int(raw) before the guard.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

How is = different from ==? What exactly gets skipped during short-circuit evaluation?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
