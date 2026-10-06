# Search strings and define validation limits

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=9544s), assigned window **02:39:04–02:59:31**. Roadmap connection: PY01/PY02.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

in checks whether a substring exists and returns a Boolean. find returns the first matching index or -1 if absent. index performs a similar search but raises ValueError when missing. count counts non-overlapping occurrences. startswith/endswith check a boundary.

isdecimal/isalpha/isalnum describe characters, not complete business validity. An empty string fails these checks. "-3" and "2.5" are not all-decimal-character strings. Unicode decimal digits may pass isdecimal; add isascii if a field must contain only ASCII digits.

lower()/upper()/casefold() normalize case for a comparison. casefold is useful for case-insensitive text matching beyond simple English text. Python string searches are otherwise case-sensitive.

Checking that a string contains @ is not complete email validation. Similarly, checking digits is not a complete date or numeric parser. State the exact promise made by each check.

## Syntax in a small example

~~~python
filename = "Weather.CSV"
normalized = filename.lower()
print(normalized.endswith(".csv"))
print(normalized.find("rain"))
print("023".isascii() and "023".isdecimal())
print("-2".isdecimal())
~~~

Expected output:

~~~text
True
-1
True
False
~~~

## Trace what happens

Lowercasing makes the suffix comparison succeed. A missing search returns -1. The digit check accepts leading zeroes because it checks characters, not numeric meaning.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/stdtypes.html#str.isdecimal).
