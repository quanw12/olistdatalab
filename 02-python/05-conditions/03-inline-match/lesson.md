# Conditional expressions and match

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=17853s), assigned window **04:57:33–05:24:56**. Roadmap connection: PY02.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A conditional expression chooses one value: value_if_true if condition else value_if_false. Use it for a small choice you can read easily; a full if statement is clearer for multiple operations.

match compares a subject against patterns. For simple literal alternatives, write case "a":. A wildcard case _: handles anything not matched earlier. Pattern matching is broader than a switch statement, but literal routing is enough here. Use Python 3.10 or newer.

A bare name in a case is usually a capture pattern, not a comparison with a previously defined constant. Quote string literals. Only the selected case body runs; you do not add break as in some other languages.

Prefer ordinary if/elif for numeric ranges. Do not compress a long validation pipeline into nested conditional expressions.

## Syntax in a small example

~~~python
count = 0
message = "has data" if count > 0 else "empty"
print(message)

mode = "preview"
match mode:
    case "preview":
        action = "show"
    case "load":
        action = "save"
    case _:
        action = "unknown"
print(action)
~~~

Expected output:

~~~text
empty
show
~~~

## Trace what happens

The expression chooses empty. match compares preview with the first quoted literal and runs that branch.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#match-statements).
