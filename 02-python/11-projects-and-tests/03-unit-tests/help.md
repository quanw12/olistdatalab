# Help — Tests that detect meaningful defects

## First hint

Define a TestCase inside build_suite to capture the supplied callable.

## Detailed approach

Write separate tests for uppercase text, outer spaces, blank text, and None. Use assertEqual and with self.assertRaises(...). Return defaultTestLoader.loadTestsFromTestCase(YourCase) without running it. Suites are consumed during execution, so do not cache one suite globally.

## Troubleshooting

If every implementation passes, your assertions are too weak. If the correct function fails, inspect the contract's exception types.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

## Build a suite one case at a time

~~~python
import unittest

def make_suite(operation):
    class OperationTests(unittest.TestCase):
        def test_one_value(self):
            self.assertEqual(operation(3), 6)

    return unittest.defaultTestLoader.loadTestsFromTestCase(OperationTests)

result = unittest.TestResult()
make_suite(lambda value: value * 2).run(result)
print(result.wasSuccessful())
~~~

The inner test class can access operation from the enclosing function. Every method whose name starts with test is discovered by the loader. The returned suite has not run yet.

For your task, define independent tests for trimming, lowercase conversion, blank input and wrong type. Use with self.assertRaises(ValueError): around the operation expected to fail. Construct a new suite on every build_suite call: unittest may consume a suite when it runs. See [pytest practice](testing-notes.md) after completing the unittest contract.
