# Read the program from its entry point

For an unfamiliar repository, first locate the README/run command, __main__/CLI entry, input loader, transformation, output writer and tests. Draw the call chain and state each boundary's inputs/outputs. Reproduce the symptom before editing. A wrong report can run without raising any exception.

Our lab provides buggy.py and data.json. The input is already validated: each row has a text customer_id that is nonempty after stripping, and a nonnegative integer amount_cents. Rows are separate order lines, so repeating a customer means add amounts, not discard a duplicate customer. This lesson fixes grouping; DE04 teaches full record validation.

## Use the debugger to inspect values

In Windows PowerShell:

~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\01-workflow\03-debugging"
& "C:/DE Courses/.venv-engineering/Scripts/python.exe" -m pdb buggy.py
~~~

At the **(Pdb)** prompt, type debugger commands, not PowerShell commands:

| Command | Use |
|---|---|
| l | Show nearby source lines |
| b 8 | Break at line 8 of the supplied buggy.py |
| c | Continue to a breakpoint |
| n | Execute the next line without stepping inside called functions |
| s | Step into a call when its internals matter |
| p row | Inspect the current row |
| p totals | Inspect current aggregate state |
| where | Inspect the call stack |
| q | Quit the debugger |

The highlighted line is normally about to execute. A variable assigned on that line may not exist yet. In a scratch file, breakpoint() can pause at a chosen location too. Remove temporary breakpoints before delivery.

## Prove the repair with a regression test

A regression test fails on the buggy behavior and passes after the intended fix. Inspecting a printout is useful, but preserve a repeatable test. Use an unrelated syntax example:

~~~python
import unittest

class TextTests(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(" north ".strip(), "north")

if __name__ == "__main__":
    unittest.main()
~~~

Run this toy example in its own scratch file; test_report.py should test your build_report. Include repeated keys and a changed input so a hard-coded dictionary cannot pass. Check that the function leaves the source data unchanged.

## Profile after correctness

cProfile reports where time was spent and how often functions were called. The provided benchmark invokes your implementation on 50,000 synthetic rows, five times. Run it only after the checker and your tests pass. Inspect cumulative time and call counts; repeat the same workload before claiming an improvement. Profiling adds overhead, so tiny timing differences are not a reliable conclusion.

A dictionary fold visits each row once and updates its customer's total; under ordinary hash-table assumptions its work scales roughly linearly. Searching an ever-growing customer list inside every row can create much more work. Bounded inputs and roughly O(k) aggregate state for k customers help explain the approach; they are not guarantees for every runtime or source.

Keep I/O wait, CPU work and memory needs distinct. A faster Python loop will not fix a wrong database join or an unavailable API. Record observations instead of inventing a before/after speedup.

## References

[Python pdb](https://docs.python.org/3.13/library/pdb.html) and [Python profiling](https://docs.python.org/3.13/library/profile.html). These commands and the original lab use standard-library facilities; no IDE extension or paid tool is required.
