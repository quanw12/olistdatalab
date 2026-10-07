# Integers, floats, and arithmetic

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=10771s), assigned window **02:59:31–03:11:33**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Use +, -, *, /, //, %, and ** for addition, subtraction, multiplication, true division, floor division, remainder, and powers. / returns a float for integer operands. // rounds the quotient downward, so -7 // 3 is -3, not -2.

Operator precedence matters. Parentheses make the intended calculation explicit: (a + b) / 2 differs from a + b / 2. Write intermediate variables when the expression represents several business decisions.

A common use of // and % is batching: total // batch_size full batches and total % batch_size leftover records. If leftovers exist, you need another partial batch. This lesson asks only for the full-batch and remainder counts; branching comes later.

Float arithmetic approximates many decimal fractions. Keep integer units when possible for exact simple counts and minor currency units. Decimal money handling will be a later extension.

## Syntax in a small example

~~~python
records = 14
batch_size = 4
print(records // batch_size)
print(records % batch_size)
print(records / batch_size)
print((2 + 4) * 3)
~~~

Expected output:

~~~text
3
2
3.5
18
~~~

## Trace what happens

There are three full groups of four and two records left. True division reports 3.5. Parentheses make addition happen before multiplication.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/introduction.html#numbers).
