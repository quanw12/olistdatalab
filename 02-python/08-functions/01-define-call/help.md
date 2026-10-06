# Help — Define and call small functions

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Write the definition first, then leave a blank line and write calls without indentation.
~~~python
def announce(topic):
    """Display the current topic."""
    print(f"Topic: {topic}")

announce("files")
~~~
If nothing prints, check for the parentheses that actually call your function. If the second city appears inside the first function body, check indentation.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

What is the difference between a parameter and an argument? When does a def body execute?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
