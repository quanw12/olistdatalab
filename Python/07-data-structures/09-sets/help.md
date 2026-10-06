# Help — Sets, membership, and stable deduplication

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Increment duplicate_count only on the repeated branch. Membership and insertion use the same value/key.
~~~python
seen = set()
for value in ["X", "X"]:
    if value in seen:
        print("duplicate")
    else:
        seen.add(value)
~~~
Difference is directional: required - actual answers what is missing, while actual - required answers what is unexpected.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why does list(set(values)) not promise first-seen order? Why does {} not make an empty set?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
