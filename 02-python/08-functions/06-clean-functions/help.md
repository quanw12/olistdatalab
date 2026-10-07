# Help — Clean functions and a weather-report mini-project

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

First implement and call normalize_city alone. Reuse split/join/title from Chapter 2; use isinstance(value, str) before string methods.

Next, implement validate_record in the specified order. Use row.get for missing fields and early returns. This tiny different example shows the failure-pair pattern:
~~~python
def validate_count(value):
    if type(value) is not int:
        return None, "count must be an integer"
    return value, None

count, error = validate_count(4)
~~~
For the temperature check, type(value) in (int, float) intentionally excludes Boolean values. not (-20 <= value <= 50) rejects values outside the contract, including NaN.

For aggregation, initialize fresh dictionaries inside summarize_weather. On an error, increment rejection_reasons[error] with get(error, 0) + 1 and continue. For a clean record, create a per-city list if absent, then append its temperature.

After validation finishes, iterate through those per-city lists to compute count and mean. None of these groups is empty, because a group is created only for an accepted row. The entire cities result may still be empty.

Return the report instead of printing inside the helpers. In the outer display code, sort the city keys and the reason keys. Use f"{average:.1f}" for one decimal.

Test helpers before assembling everything: one valid row, one missing city, one Boolean temperature, one range failure, then the full batch. Finally call the report twice to reveal accidental global/default state.

</details>

<details>
<summary>Check your explanation</summary>

Why must validation order be explicit? How does returning data make the report easier to test and reuse?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
