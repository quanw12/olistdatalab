# Help — Iterables, enumerate, zip, and filtering

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Initialize hot_cities once, then unpack each zip pair into two names. Append only the city after checking its temperature.
~~~python
names = ["A", "B"]
scores = [1, 4]
for name, score in zip(names, scores, strict=True):
    print(name, score)
~~~
zip aligns positions. If you need matching by a business ID, this simple pattern is not a substitute for a keyed join.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why can ordinary zip hide data? Why might filter(None, readings) incorrectly remove a valid reading?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
