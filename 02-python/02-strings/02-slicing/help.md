# Help — Indexing and slicing without off-by-one errors

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Write positions 0 through 10 under VN-HCM-2026. The first hyphen is at 2 and the second at 6. For a three-character segment beginning at index k, its stop is k + 3.
~~~python
sample = "Q-789"
print(sample[2:5])
~~~
Use an f-string with square brackets around the empty slice so you can see that it is empty.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is the stop index excluded? What happens to a slice when its boundaries are beyond the string?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
