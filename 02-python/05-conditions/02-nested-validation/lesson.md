# Nested conditions and validation order

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=16834s), assigned window **04:40:34–04:57:33**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Nested conditions express dependent decisions. For example, only parse a number after checking that the input has the permitted format. An inner block needs another indentation level.

Validation order determines which error is reported when several rules fail. Define that order explicitly. For a simple numeric text field, check missing input first, then supported syntax, then the parsed value's range.

A flat elif chain is often easier to read when rules are independent. A nested block is useful when later operations depend on earlier success. Avoid repeating conversion or assigning the result in only some branches.

This lab intentionally supports ASCII whole-number strings only. It is not a general float parser. Signed, decimal, and non-ASCII input is rejected by this contract.

## Syntax in a small example

~~~python
raw = "12"
if raw == "":
    result = "missing"
elif not (raw.isascii() and raw.isdecimal()):
    result = "bad format"
else:
    amount = int(raw)
    if amount <= 20:
        result = "within limit"
    else:
        result = "too large"
print(result)
~~~

Expected output:

~~~text
within limit
~~~

## Trace what happens

The nonempty ASCII digit string reaches the final block. Conversion is now safe for this contract, and the inner range check selects the result.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements).
