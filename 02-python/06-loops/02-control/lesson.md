# break, continue, and pass

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=20877s), assigned window **05:47:57–06:18:39**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

break exits the nearest enclosing loop immediately. continue skips the rest of the current iteration and moves to the next iteration. pass does nothing: execution continues with the next statement.

pass is useful when syntax requires a body but you have not implemented it. It is not a filter and it does not skip the next statement. This distinction explains why leaving pass in a validation branch can still let later code run.

Place stop conditions before work that must not happen after the stop marker. Put continue before code you want to skip for a rejected item. Ordering determines which records are processed.

In nested loops, break affects only the innermost loop. The next lesson on nested iteration explores that separately.

## Syntax in a small example

~~~python
for character in "a-b!c":
    if character == "!":
        break
    if character == "-":
        continue
    print(character)
pass
print("finished")
~~~

Expected output:

~~~text
a
b
finished
~~~

## Trace what happens

The dash is skipped. The exclamation mark exits before c is visited. pass performs no action, and the final print still executes.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements).
