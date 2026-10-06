# Expected results — Comparisons and combined rules

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
True
True
True
False
False
~~~

## Additional checks

Test humidity = -1 and humidity = 101 separately: both fail. The isdecimal guard here accepts only digit strings, not signed or decimal numbers.

## Explain your result

How is = different from ==? What exactly gets skipped during short-circuit evaluation?
