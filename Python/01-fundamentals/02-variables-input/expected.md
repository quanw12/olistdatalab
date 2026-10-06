# Expected results — Variables and input conversion

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
For inputs Hanoi, then 3:
City: Hanoi
Next count: 4

For inputs Hue, then 0:
City: Hue
Next count: 1
~~~

## Additional checks

Do not hardcode the output city/count. Prompts are additional output and may differ. The task assumes valid integer input; invalid-input handling is not required yet.

## Explain your result

Why does input return text even when you type digits? Why did changing sessions not change total_minutes in the example?
