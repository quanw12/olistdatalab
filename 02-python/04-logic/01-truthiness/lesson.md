# Boolean values and truthiness

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=12484s), assigned window **03:28:04–03:42:33**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

True and False are Boolean values; their capitalization matters. bool(value) applies Python's truth-value rules. Zero, empty strings, None, and empty collections are false. Most other values are true.

Truthiness answers whether a value is considered true in a condition. It does not answer whether the value is valid for your application. A temperature of 0 is a valid measurement; a non-empty string "invalid" is truthy but not a valid temperature.

not reverses a truth value. not None is True. Applying not to a value produces a Boolean; applying it twice effectively checks truthiness.

When a field can be absent, distinguish absence from zero. Later use value is None for that specific question instead of not value. The identity lesson explains is.

## Syntax in a small example

~~~python
print(bool(0))
print(bool("0"))
print(bool(""))
print(bool(None))
print(not "ready")
print(not not 5)
~~~

Expected output:

~~~text
False
True
False
False
False
True
~~~

## Trace what happens

The first value is numeric zero. The second is a one-character string. Python treats those differently. Two not operators turn the final value into its Boolean interpretation.


Technical reference: [Python documentation](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing).
