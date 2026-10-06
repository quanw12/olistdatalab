# Expected results — while loops and guaranteed progress

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
success_at=2, max_attempts=3:
attempt: 1
attempt: 2
success

success_at=5, max_attempts=3:
attempt: 1
attempt: 2
attempt: 3
exhausted

max_attempts=0:
exhausted
~~~

## Additional checks

Never perform more than max_attempts iterations. This is a simulation; no sleeps or API calls are needed.

## Explain your result

Why can a while loop run zero times? What guarantees that this retry simulation terminates?
