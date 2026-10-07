# Comparisons and combined rules

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=13353s), assigned window **03:42:33–04:06:13**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Comparisons include ==, !=, <, <=, >, and >=. = assigns a value; == compares values. Chaining bounds such as 0 <= humidity <= 100 is readable and includes both boundaries.

and requires both operands to be truthy; or accepts either; not reverses truth. For Boolean operands the result is Boolean. More generally and/or return one of their operands, so "ready" or "fallback" returns a string. Here we combine comparisons, which are Boolean.

Short-circuit evaluation means and skips the right operand when the left is false. or skips it when the left is true. Put a guard before an operation that would otherwise fail.

Use parentheses around groups when multiple conditions encode a business rule. Whitespace and explanatory variable names help you inspect each part.

## Syntax in a small example

~~~python
temperature = 26
humidity = 90
valid = (-20 <= temperature <= 50) and (0 <= humidity <= 100)
print(valid)
raw_count = "18"
print(raw_count.isdecimal() and int(raw_count) > 10)
print("" or "unknown")
~~~

Expected output:

~~~text
True
True
unknown
~~~

## Trace what happens

Both range comparisons are true. The digit check is evaluated before int. The final or expression returns its fallback string because the empty string is false.


Technical reference: [Python documentation](https://docs.python.org/3.13/reference/expressions.html#boolean-operations).
