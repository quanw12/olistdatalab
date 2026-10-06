# Clean and format strings

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=6414s), assigned window **01:46:54–02:16:56**. Roadmap connection: PY01/PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A string is an immutable sequence of characters. A method call such as text.strip() returns a result; it does not replace the original variable automatically. Assign the returned string if you want to keep it.

strip() removes whitespace at the ends, not repeated spaces in the middle. lower() changes letter case. replace(old, new) replaces occurrences. split() with no argument splits on whitespace and handles repeated spaces; separator.join(parts) combines strings. We use the returned pieces here as a simple group, then study lists in Chapter 7.

You can chain calls: text.strip().lower(). Read from left to right, checking the intermediate value. Avoid applying cleanup blindly: changing a human name's case or punctuation can change its meaning. For this lab, the exact normalization rule is part of the specification.

An f-string can combine cleaned values and labels. Keep raw input in a separate variable when you may need to debug where a value came from.

## Syntax in a small example

~~~python
raw_label = "  NORTH   ZONE  "
words = raw_label.split()
clean_label = " ".join(words).lower()
print(clean_label)
print(f"[{raw_label}]")
~~~

Expected output:

~~~text
north zone
[  NORTH   ZONE  ]
~~~

## Trace what happens

split creates two words despite the repeated whitespace. join inserts one space. lower changes the letters. The original string still contains its spaces.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/stdtypes.html#string-methods).
