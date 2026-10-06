# Imports, modules, and entry points

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/tutorial/modules.html).

## Concept and purpose

A module is a Python file. Importing it executes its top-level statements. Reusable definitions belong there, but prompting, requests and file writes should wait for an explicit entry point.

if __name__ == "__main__": runs when the file is executed as the entry script. Importing it uses the module name instead. A main(argv) function makes its logic callable in tests.

A package groups modules, usually with __init__.py. python -m package.module resolves imports through that package. Begin with small sibling modules before introducing packaging tools.

Do not name your files json.py, csv.py or requests.py: they can shadow real modules. text_rules.py is a supplied dependency for this exercise. In larger projects, separate pure transformation functions from CLI and external I/O.

## Syntax example

~~~python
def main(argv):
    return [word.upper() for word in argv]

if __name__ == "__main__":
    print(main(["raw","clean"]))
~~~

## Trace

Direct execution prints ['RAW', 'CLEAN']; importing defines main without running the demonstration.

## DE connection

Test runners and orchestration systems import code. Importing should not unexpectedly start a pipeline.

Use [exercise.py](exercise.py) for the exact input/output contract.
