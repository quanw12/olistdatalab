# Data types and explicit conversion

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=4465s), assigned window **01:14:25–01:46:54**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

The first scalar types to recognize are str (text), int (whole numbers), float (floating-point numbers), bool (True or False), and NoneType (the type of None, used for an absent value).

type(value) returns a type object. type(value).__name__ gives its readable name; the dot accesses an attribute. isinstance(value, int) asks whether a value is an instance of a type. A subtlety: bool is a subclass of int, so isinstance(True, int) is True. We will define deliberate validation rules rather than accept every numeric-looking value.

"23" is text, while 23 is an integer. int("23") converts text. int(3.9) truncates toward zero; it does not round. float("3.9") creates a float. str(23) produces text. bool("False") is True because a non-empty string is truthy; it does not parse the word False.

Collections are introduced properly in Chapter 7. For now, recognize that lists/dictionaries hold groups of values, without needing to implement them.

## Syntax in a small example

~~~python
raw_temperature = "28.5"
temperature = float(raw_temperature)
print(type(raw_temperature).__name__)
print(type(temperature).__name__)
print(int(3.9))
print(bool("False"))
~~~

Expected output:

~~~text
str
float
3
True
~~~

## Trace what happens

Conversion produces a new float. raw_temperature stays a string. The last two results demonstrate truncation and truthiness rather than semantic parsing.


Technical reference: [Python documentation](https://docs.python.org/3.13/library/stdtypes.html).
