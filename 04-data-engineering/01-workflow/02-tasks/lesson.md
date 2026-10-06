# Turn a ticket into observable behavior

An intern task is often smaller than a course project: add a field, fix a duplicate load, implement a report or diagnose an incorrect total. Start by understanding the existing interfaces and expected behavior. Do not rewrite the whole repository before reproducing the problem.

## Clarify the boundary

Write the goal, input, output, owner, constraints and acceptance criteria. Separate questions that block correctness from choices you can resolve reversibly. For “daily totals”, clarify the timezone, event/update time, currency, grouping key, empty groups, corrections and cutoff.

A useful question names the uncertainty and consequence: “Should the report group by the order's UTC event day? Using the extraction day would move a late order to a different business date.” A vague “What should I do?” makes it harder for a teammate to answer.

Keep **confirmed requirements**, **explicit lab assumptions**, **open questions** and **out-of-scope work** separate. An elapsed deadline is not confirmation of an assumption. On a real task, escalate a blocking requirement and continue independent investigation or tests.

## Use small implementation slices

1. Read the README, entry point and interfaces. Run existing checks and record the baseline.
2. Reproduce one valid case and one reported failure using synthetic or authorized data.
3. Define a small contract and its test before modifying behavior.
4. Implement one slice with a clear boundary. Keep external I/O separate from transformation where useful.
5. Test normal, empty, boundary, malformed, replay and failure cases that the contract actually requires.
6. Inspect the diff for scope, fixtures, secrets and unintended behavior changes.
7. Deliver a handoff: what changed, how to run it, evidence, limits and any remaining decision.

Example Python assertion syntax, using an unrelated toy value:

~~~python
expected_count = 2
actual_count = len(["north", "south"])
assert actual_count == expected_count, "region count mismatch"
~~~

An assertion compares actual behavior with a declared expectation. A test that always asserts True gives no evidence. A useful acceptance example identifies the input and why a wrong implementation would fail.

## Define failure ownership

Some record errors can be quarantined. A database disconnect or conflicting source version may fail a batch and prevent progress from advancing. Specify who sees that failure, what output may be visible and how to retry. “Catch every exception and continue” can conceal missing data.

After the task, document what was observed rather than copying planned test results. A concise handoff lets another person reproduce and assess your work without reading the conversation.
