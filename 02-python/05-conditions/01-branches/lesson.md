# if, elif, else, and boundary order

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=15559s), assigned window **04:19:19–04:40:34**. Roadmap connection: PY02.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

An if statement starts with a condition followed by a colon. Its body is indented. elif adds another condition if earlier ones were false. else handles the remaining case. Python runs only the first matching branch in one if/elif/else chain.

Separate if statements are different: more than one may run. Choose a chain when the output categories are mutually exclusive.

Order boundary checks carefully. If temperature >= 30 is checked before temperature >= 35, a value of 36 is already captured by the first branch. Either order strongest thresholds first or use increasing upper bounds.

Indentation is syntax, not decoration. Use four spaces per level consistently. After the conditional block, unindented statements run regardless of which branch was selected.

## Syntax in a small example

~~~python
temperature = 24
if temperature < 20:
    label = "cool"
elif temperature < 30:
    label = "mild"
else:
    label = "hot"
print(label)
~~~

Expected output:

~~~text
mild
~~~

## Trace what happens

24 fails the first comparison and passes the second. Python assigns mild, skips else, then prints the selected label.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements).
