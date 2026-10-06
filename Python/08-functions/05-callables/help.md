# Help — Built-ins, named functions, and lambdas

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

In apply_to_all, operation is a local parameter containing a function. Call it with one item, not the whole list.
~~~python
def apply_once(value, operation):
    return operation(value)

print(apply_once("abc", len))
~~~
If you write normalize_city() while passing the argument, it runs immediately and lacks its required text argument. Supply the function value instead.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is passing len different from passing len(values)? What makes a function easier to test independently?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
