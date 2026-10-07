# Run a script, comments, and print

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=0s), assigned window **00:00–00:52:01**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A script is a text file containing Python statements. The interpreter executes the top-level statements in order. The terminal is where you issue the command to run that file; it is not the file itself. An editor helps you change the text.

In Python, a comment starts with # outside a string and continues to the end of that line. A quoted string is text data. print(...) calls a built-in function: parentheses contain its arguments. Commas separate multiple arguments; print inserts spaces between them unless you set sep. Its default end is a newline.

A syntax error means Python cannot parse your code. Check quotes and parentheses at the reported line. A NameError usually means a name is missing or misspelled. File-not-found messages from the terminal often mean you are in the wrong folder.

You already have Python installed. Verify the interpreter using setup.md; do not install a second copy simply to follow the installation segment.

## Syntax in a small example

~~~python
# A comment explains intent; it is not printed.
print("Batch preview")
print("Accepted:", 4)
print("A", "B", sep=" | ")
print("done", end="!\n")
~~~

Expected output:

~~~text
Batch preview
Accepted: 4
A | B
done!
~~~

## Trace what happens

The first call prints one string. The second receives two arguments and separates them with a space. sep changes only the third call. The final call replaces the default newline with an exclamation mark followed by a newline.


Technical reference: [Python documentation](https://docs.python.org/3.13/library/functions.html#print).
