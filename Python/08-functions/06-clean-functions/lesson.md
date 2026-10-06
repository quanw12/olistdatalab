# Clean functions and a weather-report mini-project

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=45969s), assigned window **12:46:09 to the end of the video**. Roadmap connection: PY04/PY05/PY12 (partial). The weather mini-project is original companion practice after the clean-functions segment. It is not one of the instructor's paid-program projects. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A clean function has one understandable job, a clear input/output contract, and a name that explains its purpose. Keep normalization, validation, aggregation and display as separate steps so an error has a small place to hide.

A contract states accepted inputs and returned values, including failure cases. This project returns a pair (record, error): exactly one is non-None. The caller decides whether to accept or reject. Type hints and formal schemas can follow later.

Use early returns for invalid records. Check rules in a documented order so each rejected row has one reproducible reason. Do not mutate input dictionaries: create a new cleaned dictionary for accepted records.

A function can call other functions. The orchestration function connects the steps; it should not contain every detail itself. Keep printing at the outer boundary. Standard-library-only, in-memory data is enough to practise this structure.

For checking, assert condition raises AssertionError when the condition is false. Assertions can verify your exercise results but must not be the sole validation of external data in production. Here they are optional self-checks, not an additional testing framework.

## Syntax in a small example

~~~python
def normalize_label(text):
    return text.strip().upper()

def validate_amount(value):
    if type(value) not in (int, float):
        return None, "not numeric"
    if not 0 <= value <= 10:
        return None, "outside range"
    return value, None

def describe(label, value):
    amount, error = validate_amount(value)
    if error is not None:
        return error
    return f"{normalize_label(label)}: {amount}"

print(describe(" batch ", 4))
print(describe(" batch ", True))
assert describe("x", 20) == "outside range"
~~~

Expected output:

~~~text
BATCH: 4
not numeric
~~~

## Trace what happens

describe delegates the numeric rule, then formats only an accepted value. Exact type membership rejects bool, even though bool is an int subclass. The assertion passes silently.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#intermezzo-coding-style).
