# Expected results — Clean functions and a weather-report mini-project

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
accepted: 5
rejected: 3
Da Nang: count=1, avg=30.0
Hanoi: count=2, avg=32.0
Hue: count=2, avg=30.0
city missing: 1
temperature not numeric: 1
temperature outside range: 1
~~~

## Additional checks

summarize_weather([]) must return {"accepted_count": 0, "rejected_count": 0, "rejection_reasons": {}, "cities": {}}.
validate_record({"city": "Hue", "temperature": True}) returns (None, "temperature not numeric").
validate_record({"city": None, "temperature": 999}) returns (None, "city missing") because city is checked first.
Temperatures -20 and 50 pass; -21 and 51 fail. NaN/infinity, if supplied as floats, fail the chained range check.
Missing temperature is treated as not numeric. Missing city is treated as city missing.
All-invalid input returns no city summaries. The original rows must remain unchanged.
Calling summarize_weather twice with the same rows returns equal dictionaries and does not accumulate earlier counts.

## Explain your result

Why must validation order be explicit? How does returning data make the report easier to test and reuse?

</details>
