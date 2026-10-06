# Expected results — Boolean values and truthiness

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
False
True
True
False
False
True
False
~~~

## Additional checks

A whitespace-only string is non-empty. Compare bool(' ') with bool(' '.strip()) in a separate scratch run.

## Explain your result

Why is 'False' truthy? Why is truthiness insufficient to validate a temperature?
