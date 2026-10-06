# Built-ins, named functions, and lambdas

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=44431s), assigned window **12:20:31–12:46:09**. Roadmap connection: PY04/PY05. The video labels this region Types of Python Functions. The categories and examples below are our teaching choices, not a claim to reproduce the instructor's exact taxonomy. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

You have already called built-in functions such as len and sum. A function defined with def is a named user-defined function. A lambda creates a function from one expression. These are useful teaching categories, not an exhaustive classification of every callable object.

Functions are values: you can assign one to another name, pass it as an argument, or call it later. This explains key functions in sorted and predicates in filter. A callable is something that can be called with parentheses.

A higher-order function takes or returns another function. That phrase describes a role, not a separate syntax. For example, a helper can receive a cleaning function and apply it to each value.

A pure calculation avoids externally visible mutation/output and returns a result based on its inputs. A printing or file-writing function has side effects. Both can be useful; keeping their roles clear improves testing.

Recursion, generators and decorators are later extensions. This lesson concentrates on the callable forms needed to understand the course exercises.

## Syntax in a small example

~~~python
def normalize(text):
    return text.strip().lower()

operation = normalize
print(operation(" A "))

def transform(values, operation):
    return [operation(value) for value in values]

print(transform([" X ", "Y "], normalize))
print(transform([2, 3], lambda value: value * 10))
~~~

Expected output:

~~~text
a
['x', 'y']
[20, 30]
~~~

## Trace what happens

operation refers to the same function object as normalize. transform calls its supplied operation once per item. The lambda supplies an alternative one-expression transformation.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#lambda-expressions).
