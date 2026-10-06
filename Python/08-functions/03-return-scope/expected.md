# Expected results — Return values, early return, and scope

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
{'count': 3, 'minimum': 29.0, 'maximum': 33.0, 'average': 31.0}
{'count': 0, 'minimum': None, 'maximum': None, 'average': None}
{'count': 1, 'minimum': 0.0, 'maximum': 0.0, 'average': 0.0}
~~~

## Additional checks

A valid zero reading must not be mistaken for absent input. Only the caller prints. Reuse the returned average in another expression to demonstrate it is available.

## Explain your result

Why is print not a replacement for return? Can a function mutate an argument despite its variable names being local?
