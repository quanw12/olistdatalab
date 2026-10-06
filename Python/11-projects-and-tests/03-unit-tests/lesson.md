# Tests that detect meaningful defects

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/unittest.html).

## Concept and purpose

Arrange input, act by calling the function, then assert the result. Cases should come from a contract: ordinary values, boundaries, empty input and errors. Tests that only check a result is not None often miss incorrect values.

unittest is built into Python. Subclass TestCase and write test_ methods. assertEqual compares values; assertRaises checks error behavior. TestSuite groups cases, and a runner executes them.

pytest supports concise assert-based tests, fixtures and parametrization. It can also run unittest tests. A pytest fixture supplies isolated setup such as tmp_path; @pytest.mark.parametrize runs multiple input/expected pairs. See the local testing-notes.md for a runnable pytest example.

A green test suite is stronger evidence if deliberately faulty implementations fail it. This exercise evaluates your tests against four known defects. Do not inspect the callable's name or source: test behavior.

## Syntax example

~~~python
import unittest
class ArithmeticCheck(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2+3,5)
suite=unittest.defaultTestLoader.loadTestsFromTestCase(ArithmeticCheck)
result=unittest.TestResult()
suite.run(result)
print(result.wasSuccessful())
~~~

## Trace

One test executes and produces True. Incorrect expectations would register a failure.

## DE connection

A test should catch real regressions such as lost normalization or accepted invalid records.

Use [exercise.py](exercise.py) for the exact input/output contract.
