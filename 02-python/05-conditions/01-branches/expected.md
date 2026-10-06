# Expected results — if, elif, else, and boundary order

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
temperature 19.9 -> cool
temperature 20 -> warm
temperature 29.9 -> warm
temperature 30 -> hot
~~~

## Additional checks

Each run prints exactly one label. Labels and boundaries follow the exercise contract, which differs slightly from the example.

## Explain your result

Why can several separate if statements print multiple labels? Which branch handles exactly 30?
