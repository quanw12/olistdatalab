# Expected results — Clean and format strings

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
city: Ho Chi Minh City
source: open-meteo
[  ho   chi minh city  ]
~~~

## Additional checks

Try raw_city = '   ' separately: the normalized value should be an empty string. title() is acceptable under this exercise's rule, not a universal rule for personal/place names.

## Explain your result

Why does strip alone not collapse internal spaces? Why should the normalization rule be documented?

</details>
