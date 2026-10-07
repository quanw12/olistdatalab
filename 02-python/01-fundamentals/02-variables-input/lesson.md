# Variables and input conversion

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=3121s), assigned window **00:52:01–01:14:25**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A variable name refers to a value. Assignment uses =: evaluate the expression on the right, then bind the name on the left. Names are case-sensitive. Use meaningful snake_case names such as study_hours.

input("Prompt: ") displays a prompt and returns the user's response as a string. Even typing 3 gives text "3". int converts valid integer text into an integer; float converts supported decimal text. Conversion can fail: int("three") raises ValueError. Exception handling comes in a later extension; this lesson uses the specified valid inputs.

An f-string starts with f before the quote. Expressions inside braces are evaluated and inserted into the text. Assignment itself does not print anything. Reassigning one variable does not recalculate earlier results automatically.

Syntax to try interactively: city = input("City: "). Save your exercise in the file, then run it in a terminal that accepts keyboard input.

## Syntax in a small example

~~~python
sessions = 2
minutes_each = 30
total_minutes = sessions * minutes_each
sessions = 3
print(total_minutes)
print(f"Planned sessions: {sessions}")
~~~

Expected output:

~~~text
60
Planned sessions: 3
~~~

## Trace what happens

total_minutes becomes 60 when sessions is 2. Rebinding sessions to 3 does not rerun the earlier multiplication. The f-string reads the current value 3.


Technical reference: [Python documentation](https://docs.python.org/3.13/library/functions.html#input).
