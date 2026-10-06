# Rounding, display precision, and randomness

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=11493s), assigned window **03:11:33–03:28:04**. Roadmap connection: PY01.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

round(value, digits) returns a rounded numeric value. Formatting with f"{value:.2f}" creates a string with exactly two decimal places. These operations answer different questions: what numeric result do I use, and what text do I show?

Python rounds ties to the even choice for exactly halfway cases such as round(2.5) and round(3.5). Binary floating-point representation can make decimal-looking ties less obvious. Do not assume every .5-looking decimal follows a business rule such as always rounding up.

The random module is part of Python's standard library. import random makes it available. random.Random(seed) creates a separate pseudo-random generator. randint(a, b) includes both endpoints. Repeating the same seeded operations in the same environment supports reproducible exercises; unseeded random values must not have a single fixed expected answer.

Use range checks to validate generated values. Randomness here is for practice, not secrets or security tokens.

## Syntax in a small example

~~~python
import random

measurement = 12.346
print(round(measurement, 2))
print(f"{12.3:.2f}")
print(round(2.5), round(3.5))
left = random.Random(19)
right = random.Random(19)
print(left.randint(1, 6) == right.randint(1, 6))
~~~

Expected output:

~~~text
12.35
12.30
2 4
True
~~~

## Trace what happens

Formatting displays a trailing zero but does not modify 12.3. The two independent generators start in equivalent states, so their first equivalent operation agrees.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/random.html).
