# Help — Boolean values and truthiness

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Inspect the type and content before predicting truthiness. Quotes make the value text.
~~~python
raw = "   "
print(bool(raw))
print(bool(raw.strip()))
~~~
Do not convert the word False with bool and expect semantic parsing. For values that need specific meanings, define explicit accepted strings later.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is 'False' truthy? Why is truthiness insufficient to validate a temperature?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
