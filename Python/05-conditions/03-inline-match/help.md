# Help — Conditional expressions and match

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Read the conditional expression as 'choose A when condition is true, otherwise choose B'. For match, keep the colon and indentation at both levels.
~~~python
extension = "json"
match extension:
    case "json":
        print("structured")
    case _:
        print("other")
~~~
If Python flags unreachable patterns, check whether you wrote an unquoted name that captures everything.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

When is a full if block clearer than an inline expression? Why must string case labels be quoted?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
