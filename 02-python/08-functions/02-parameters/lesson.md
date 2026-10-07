# Positional, keyword, and default arguments

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=41292s), assigned window **11:28:12–12:20:31**. Roadmap connection: PY04. This long video section is split across three lessons: argument binding, returns/scope, and flexible arguments. The window is shared; no finer timestamp is claimed. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Positional arguments bind by position. Keyword arguments bind by parameter name. For def label(city, unit="C"), city is required and unit has a default. label("Hue") uses C; label(city="Hue", unit="F") is explicit.

Do not supply the same parameter twice, as in label("Hue", city="Hanoi"). It raises TypeError. Required parameters normally precede parameters with defaults. Parameters after a bare * are keyword-only: def report(city, *, unit="C"). This can make optional settings clearer; basic calls remain the main exercise.

Default expressions are evaluated when the function is defined. A mutable default such as items=[] can unexpectedly share data across calls. Use None as a sentinel and create a new list inside the function instead.

Argument binding should be understood before using *args/**kwargs. Draw a small mapping from each argument to its parameter.

## Syntax in a small example

~~~python
def format_reading(city, temperature, unit="C"):
    return f"{city}: {temperature} {unit}"

print(format_reading("Hue", 28))
print(format_reading(temperature=82, city="Hue", unit="F"))
~~~

Expected output:

~~~text
Hue: 28 C
Hue: 82 F
~~~

## Trace what happens

The first call fills the first two positions and uses the default C. The second call maps names directly, regardless of their written order.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#default-argument-values).
