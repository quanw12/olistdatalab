# Help — Search strings and define validation limits

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Translate each requirement into one Boolean or integer expression. Do not write conditional branches yet.
~~~python
tag = " REPORT.JSON ".strip().lower()
print(tag.endswith(".json"))
~~~
For the identifier, combine isascii() and isdecimal() with and. If find returns 0, that means a match at the first character, not failure. The missing-value sentinel here is -1.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is a digit-character test insufficient for a decimal number such as '-7.5'? Why is find's missing result different from index?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
