# Help — Positional, keyword, and default arguments

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use a default string in the signature and one f-string after return.
~~~python
def badge(name, prefix="ID"):
    return f"{prefix}: {name}"

print(badge("station", prefix="KEY"))
~~~
Trace each call as city -> value, count -> value, label -> value. If Python says multiple values for an argument, check for a positional value already assigned to that keyword.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

When is a default value evaluated? Why can a list default accidentally share state?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
