# Search with for-else

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=22719s), assigned window **06:18:39–06:40:52**. Roadmap connection: PY02. This window also contains nested loops. Study loop-else here; the next lesson reuses the window for nesting. No finer timestamp is claimed. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A loop's else block runs when the loop finishes normally without break. It also runs when the iterable is empty. It is not paired with an if inside the loop.

This fits a search: inspect candidates, break when a match is found, and report no match in else. If you use continue, the loop can still finish normally, so continue does not suppress the else block.

Indent the else at the same level as for. An else aligned with an inner if means something different.

The benefit is that you may not need a separate found flag. A flag-based search is also valid when it makes the intent clearer; here practise the exact for-else behavior.

## Syntax in a small example

~~~python
text = "dry"
for character in text:
    if character in "aeiou":
        print("found:", character)
        break
else:
    print("no vowel")
~~~

Expected output:

~~~text
no vowel
~~~

## Trace what happens

None of d, r or y matches, so the loop exhausts normally and else prints no vowel. With text='rain', the first vowel a triggers break and suppresses else.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#else-clauses-on-loops).
