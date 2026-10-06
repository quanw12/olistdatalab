# CLI options, configuration, and environments

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/argparse.html).

## Concept and purpose

argparse translates command-line text into a Namespace. add_argument("--input", required=True) requires an option; type=int converts its value. parse_args(argv) accepts a test-provided list without modifying the real process arguments.

Configuration stores choices, not logic. Validate it before doing work. JSON booleans must not count as positive integer batch sizes merely because bool subclasses int.

Environment variables are strings read through os.environ or os.getenv. Keep credentials out of committed files. Define precedence when combining sources, such as CLI over environment over configuration default.

A virtual environment isolates dependencies. Install with the chosen interpreter's -m pip rather than an unrelated pip executable. de-setup.md gives exact commands and tested package versions.

## Syntax example

~~~python
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--limit",type=int,default=10)
options=parser.parse_args(["--limit","3"])
print(options.limit)
~~~

## Trace

The value is integer 3. Conversion does not by itself prove it is positive.

## DE connection

Paths and batch sizes should change through configuration rather than source edits.

Use [exercise.py](exercise.py) for the exact input/output contract.
