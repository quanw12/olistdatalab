# Day 27 — Use AI assistance with deterministic verification


## Let AI propose; keep the pipeline accountable

An LLM can help explain a traceback, draft documentation, suggest SQL/tests and summarize a verified report. Its output is a proposal. Syntax validity does not prove correct joins, time windows, units or facts.

A useful prompt contains: task, relevant schema/input, exact output contract, examples/constraints, and verification criteria. Keep it small enough to inspect. Supply synthetic/redacted data and the specific error, not passwords or your entire environment.

For this exercise, require exactly four JSON fields: observation_count, observed_city_count, hottest_city, highest_temperature_c. Define hottest_city as the city with the highest individual recorded temperature in the fixed base fixture. Configured city count 4 is different from observed city count 3.

## JSON parsing and validation

~~~python
import json

text = '{"count": 3}'
proposal = json.loads(text)
if type(proposal) is not dict:
    raise ValueError("Expected a JSON object")
if set(proposal) != {"count"}:
    raise ValueError("Unexpected fields")
if type(proposal["count"]) is not int:
    raise ValueError("count must be an integer")
~~~

json.loads parses structure; it does not prove the contents. Require exact keys/types, reject Boolean numbers, and compare each value against independently calculated trusted metrics. Do not 'repair' a wrong number silently and call the proposal accepted. Record the rejection reason.

No live LLM API is required. data/llm_cases.json contains five saved proposal strings, including malformed and misleading outputs. The accept flag is the expected test result, not an input your validator may use to decide.

## AI in a DE workflow

For SQL assistance, provide the schema, expected grain and edge cases such as Hue. Read the proposed SQL and run read-only checks on a lab database. Never automatically execute arbitrary generated SQL or shell commands.

For debugging, ask for a hypothesis and a small distinguishing experiment; test it. For tests, ask which edge cases your contract misses, then write assertions yourself. For documentation, verify commands against a fresh rehearsal. Keep model/tool/date/prompt/output and your decision when live assistance is used.

## Bridge toward ML

A future ML workflow needs versioned features, a target, time-respecting evaluation and leakage checks. A model must not receive observations that occurred after its prediction time. This capstone practices reliable data delivery; it does not claim predictive accuracy from eight demo rows.

Read: [Python JSON](https://docs.python.org/3.13/library/json.html). The lesson is provider-independent; no new account or paid API is required.
