# Return values, early return, and scope

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=41292s), assigned window **11:28:12–12:20:31**. Roadmap connection: PY04. Focus on return values and scope within the shared parameter/return section. Scope examples are companion explanations. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

return sends a value to the caller and exits the current function call. Code after that return in the same path is not executed. A function with no explicit return produces None.

print writes text to output and itself returns None. That is why result = print("hello") displays hello but stores None. Computation functions should normally return reusable data; display belongs at the caller boundary.

A name assigned inside a function is normally local. Rebinding a local name does not rebind an outer variable with the same spelling. However, mutating a list/dictionary passed in can change the shared object: local names do not create deep copies.

Early return handles special cases such as empty input before the main calculation. Returning multiple comma-separated values constructs a tuple, which callers can unpack.

## Syntax in a small example

~~~python
def average(values):
    if not values:
        return None
    return sum(values) / len(values)

number = 10
def shifted(number):
    number = number + 1
    return number

print(average([2, 4]))
print(average([]))
print(shifted(number))
print(number)
~~~

Expected output:

~~~text
3.0
None
11
10
~~~

## Trace what happens

The empty case returns before division. shifted rebinds its local number to 11, leaving the outer integer binding at 10.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions).
