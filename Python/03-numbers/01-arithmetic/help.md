# Help — Integers, floats, and arithmetic

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Compute the quotient and remainder separately. For the Celsius expression, Python evaluates multiplication/division before addition, but parentheses may make your intent clearer.
~~~python
total_units = 19
group_size = 6
print(total_units // group_size, total_units % group_size)
~~~
For the negative example, verify -7 = (-3 * 3) + 2. Floor means toward negative infinity.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

When do you want / instead of //? Why is integer cents useful for exact arithmetic?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
