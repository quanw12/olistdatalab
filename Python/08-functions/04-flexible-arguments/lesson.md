# Collect and unpack arguments with * and **

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=41292s), assigned window **11:28:12–12:20:31**. Roadmap connection: PY04. Flexible-argument practice is a companion extension tied to the parameters section; its exact coverage/timing within the video was not verified. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

In a definition, *args collects extra positional arguments into a tuple. **kwargs collects extra keyword arguments into a dictionary. The names args and kwargs are conventions; the stars cause the behavior.

At a call site, *values unpacks a sequence into positional arguments, and **options unpacks a dictionary into keyword arguments. The two directions are different: definitions collect; calls expand.

Prefer named parameters when your function has a clear contract. Flexible arguments are useful for wrappers and variable-length inputs, but can hide mistakes if accepted keywords are not validated. Unpacking also does not bypass normal argument-binding rules.

With a signature def total(*values), calling total([1, 2]) supplies one list argument. total(*[1, 2]) supplies two numeric arguments. Trace the shape before applying sum.

## Syntax in a small example

~~~python
def total(*values):
    return sum(values)

def describe(city, **metadata):
    return city, sorted(metadata)

print(total(2, 3, 4))
numbers = [5, 6]
print(total(*numbers))
print(describe("Hue", source="demo", unit="C"))
~~~

Expected output:

~~~text
9
11
('Hue', ['source', 'unit'])
~~~

## Trace what happens

The first values tuple is (2, 3, 4). The expanded list supplies two arguments in the second call. Keyword names become metadata keys.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists).
