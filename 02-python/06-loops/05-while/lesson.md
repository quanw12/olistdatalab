# while loops and guaranteed progress

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=24052s), assigned window **06:40:52–07:10:04**. Roadmap connection: PY02.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

while checks its condition before each iteration. It may run zero times. Unlike for over a fixed sequence, you must ensure something can change the condition or reach break.

A counter loop needs an initial value, a condition and an update. Missing the update can create an infinite loop. continue can accidentally skip the update if you place it at the bottom, so inspect every path.

while True is an intentional indefinite loop with explicit exit logic. Use it when that logic is clear; do not use an unbounded loop for retries. A retry process needs a maximum attempt count.

This exercise simulates attempts without waiting or calling a network. Real retry timing, exception handling and logging belong to the later pipeline track.

## Syntax in a small example

~~~python
attempt = 1
while attempt <= 2:
    print("attempt:", attempt)
    attempt += 1
print("next:", attempt)
~~~

Expected output:

~~~text
attempt: 1
attempt: 2
next: 3
~~~

## Trace what happens

The body runs with attempt 1 and 2. The next update makes it 3, which fails the condition. The value remains 3 afterward.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement).
