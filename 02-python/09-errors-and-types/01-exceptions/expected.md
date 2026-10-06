# Expected results — Exceptions and deliberate validation

parse_count(' 0042 ') = 42; parse_count('0') = 0; parse_count('10000') = 10000. ''/'-1'/'1.2'/'١٢'/'10001' raise ValueError. None and 4 raise TypeError.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why should an invalid count not silently become zero?

<details>
<summary>Reveal the reasoning after answering</summary>

Zero is a valid count. Replacing malformed input with zero hides the difference between absent/invalid data and a genuine measurement.

</details>
