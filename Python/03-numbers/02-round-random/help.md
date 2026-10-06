# Help — Rounding, display precision, and randomness

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use the f-string format specifier :.2f inside the braces.
~~~python
value = 6.5
print(f"{value:.2f}")
~~~
For random draws, keep separate generator variables. Drawing twice from one generator advances its state and is not the same experiment. Check the range with 1 <= draw <= 6.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why should expected results avoid one exact unseeded random number? Why do equal-looking rounded/formatted results have different types?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
