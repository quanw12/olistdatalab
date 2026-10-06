# Help — Clean and format strings

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

First produce the whitespace-normalized string, then call title().
~~~python
label = "  river   station "
collapsed = " ".join(label.split())
print(collapsed.title())
~~~
Use strip().lower() for the source. If multiple internal spaces remain, you used strip without split/join. If your raw value changed, check which variable you reassigned.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why does strip alone not collapse internal spaces? Why should the normalization rule be documented?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
