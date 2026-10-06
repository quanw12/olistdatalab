# Exceptions and deliberate validation

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/tutorial/errors.html).

## Concept and purpose

A syntax error prevents parsing. An exception happens during execution and carries a type plus a traceback. Read the last line first, then follow the frames into your own code.

Use try around the smallest operation that may fail, except for the failures you know how to handle, and raise when your own contract is broken. An else block runs after a successful try; finally runs during normal or exceptional exit and is useful for cleanup. Do not return from finally: it can hide the original failure.

Convert external strings at the boundary. Distinguish a bad value from a programmer mistake. Catching Exception and continuing silently makes a pipeline look successful while losing records. raise ValueError("message") from exc retains the original cause when translating a conversion error.

For debugging, reproduce the issue with one row, inspect its type, and use breakpoint() to inspect local values interactively. Remove the breakpoint before automated checks.

## Syntax example

~~~python
def percentage(text):
    try:
        value = float(text)
    except (TypeError, ValueError) as exc:
        raise ValueError("percentage must be numeric") from exc
    if not 0 <= value <= 100:
        raise ValueError("percentage outside range")
    return value

print(percentage("25"))
try:
    percentage("bad")
except ValueError as error:
    print(error)
~~~

## Trace the example

The first call returns 25.0. The second catches a conversion failure and exposes a domain-specific ValueError. A failure is visible rather than replaced by zero.

## Apply it to DE

A rejected row must carry a reason; an unavailable source or broken program should not be counted as a valid empty batch.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.
