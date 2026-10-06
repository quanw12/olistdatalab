# Expected results — Collect and unpack arguments with * and **

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
30.0
None
5.0
{'name': 'demo', 'metadata_keys': ['city', 'source']}
~~~

## Additional checks

Do not silently flatten arbitrary nested inputs. Keep the input contract as zero or more numeric positional arguments.

## Explain your result

What do * and ** mean in a definition versus a call? Why are explicit parameters often easier to validate?
