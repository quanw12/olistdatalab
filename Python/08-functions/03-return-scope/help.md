# Help — Return values, early return, and scope

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Start with the empty-list guard, then calculate the nonempty result. Reuse the aggregation syntax from Chapter 7.
~~~python
def span(values):
    if not values:
        return None
    return max(values) - min(values)

result = span([3, 8])
print(result)
~~~
If your caller gets None despite visible numbers, check whether you only printed the summary. Every intended path needs the correct return value.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is print not a replacement for return? Can a function mutate an argument despite its variable names being local?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
