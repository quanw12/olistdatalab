# LAB08 — Learn

## Integrate a repair, not a new stack

An intern ticket usually involves an existing system. Choose a narrow change, reproduce the failure, define acceptance criteria and preserve its public contract. The repository owner needs to know what changed, how you checked it and how to recover if the change fails.

## Syntax — Python CLI boundary

~~~python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--batch-id", required=True)
args = parser.parse_args()
~~~
CLI arguments are strings, not validated business data. Connect the boundary to functions you have tested; make a failed batch exit nonzero. Keep library functions independently testable. Review Python CLI and Linux exit status rather than embedding print statements in every function.

Use AI for a hypothesis or test review only after reproducing the problem. Verify each proposed change; explain your own final implementation.

[Assignment](exercise.md) · [Hints](help.md)
