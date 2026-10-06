# DE03 assignment

## Contract

Implement **build_report(rows)** in exercise.py. Given the prevalidated rows described in lesson.md, return a new dictionary mapping stripped customer IDs to the sum of their integer amounts. Empty input returns {}. Do not mutate rows or their dictionaries. No I/O or printing inside this function is required.

Keep buggy.py and data.json unchanged as the original reproduction. They are intentionally broken lab infrastructure, not a solution.

1. Run buggy.py and record its actual output. Write the correct output for data.json by hand.
2. Draw the caller → build_report → dictionary update path. Use pdb to inspect row, customer_id and totals across iterations. Record a short trace showing two separate logical defects.
3. In test_report.py, write regression tests against buggy.build_report and demonstrate at least one failure. Cover whitespace normalization, repeated customers, empty input, changed amounts/IDs and unchanged source data.
4. Write your corrected implementation in exercise.py. Change the test import to exercise.build_report; keep the behavioral expectations intact. Run your tests and the provided DE03 checker.
5. Run benchmark.py using cProfile. Record workload, interpreter, call count, the main cost observed and one limitation of this measurement. Explain how processing/state scale with rows/customer count. Optimization is optional; correctness is required.
6. Write bug-report.md: reproduction, cause, failing test, repair, actual verification and remaining scope. Do not add unrelated source validation or a new framework.

The expected aggregate for the provided three rows is {"c1": 30, "c2": 5}. Tests must also work on different values. The supplied checker should fail on an untouched starter.

## Reflection

Why should you reproduce the wrong behavior and preserve a failing test before changing unfamiliar code?
