# Indexing and slicing without off-by-one errors

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=8216s), assigned window **02:16:56–02:39:04**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Indexes begin at zero. text[0] is the first character; text[-1] is the last. An out-of-range single index raises IndexError.

The slice text[start:stop:step] includes start and excludes stop. Missing start/stop values use the sequence boundaries. A slice can be empty, and oversized boundaries are clipped. A step of -1 traverses backward. A step of zero is invalid.

To reason about a slice, write the character positions first. For "AB-123", positions 0/1 hold A/B, position 2 holds the dash, and positions 3–5 hold the digits. The slice [3:6] selects those three digits.

Slicing extracts positions; it does not prove the text has a valid format or represents a real date. Later validation must check content and meaning.

## Syntax in a small example

~~~python
code = "AB-123"
print(code[0])
print(code[-1])
print(code[3:6])
print(code[:2])
print(code[::-1])
print(code[20:])
~~~

Expected output:

~~~text
A
3
123
AB
321-BA

~~~

## Trace what happens

The stop at 6 excludes position 6. Reversing visits every character backward. The final print produces an empty line because the slice starts beyond the string's end.


Technical reference: [Python documentation](https://docs.python.org/3.13/library/stdtypes.html#common-sequence-operations).
