# Define and call small functions

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=40185s), assigned window **11:09:45–11:28:12**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

def creates a function object and binds it to a name. The indented body does not run at definition time; it runs when the function is called. A parameter is a name in the definition. An argument is the value supplied by the caller.

Use parentheses to call the function: show_city("Hue"). Writing show_city alone refers to the function object. This distinction also explains why key=len works in sorting.

A function can print as a side effect, return a value, or both, but a clear design separates these roles. This first lesson practises a small printing function; returning data gets its own lesson.

A docstring is a string at the beginning of a function body describing its purpose. Keep function names action-oriented and specific. Defining a function before its call avoids a missing-name error in a simple top-level script.

## Syntax in a small example

~~~python
def show_stage(name):
    """Print one stage label."""
    print(f"Stage: {name}")

print("before")
show_stage("validate")
show_stage("load")
print("after")
~~~

Expected output:

~~~text
before
Stage: validate
Stage: load
after
~~~

## Trace what happens

The function body is skipped during definition. Each call creates a new local binding for name and executes the body once.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions).
