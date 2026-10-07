# DE02 assignment

You receive this ticket:

> Build a daily customer order-total export from the retail change feed. Run it daily, support reruns and reject bad records. Give the analyst a clear output and tell us when it fails.

## Lab clarification card

These are declared for this exercise; on a real assignment you would confirm them:

- Use [the supplied retail changes](../../data/all_changes.json); no live API is required.
- Event days are UTC, with [start, end) boundaries. Corrections affect the original event day, even if received later.
- Input uses one currency with two decimal places, represented by integer cents. A real currency code and permitted currency mixing remain questions for the owner before publication.
- Highest version per ID wins; retain deletes as state. Exact equal-version replay is allowed; conflicting equal-version content fails the batch.
- Group active order amounts/counts by customer and event day. Customers with no active orders are omitted from this lab export.
- Invalid individual records are quarantined with field reasons. System failures and source-version conflicts fail the batch; progress must not move beyond durable successful state.

Create four documents in this lesson:

1. **task.md:** goal, input/output contract, confirmed lab requirements, at least three real-world questions, out-of-scope items and acceptance criteria. Do not pretend the unanswered currency/source guarantees are verified.
2. **plan.md:** at most six implementation slices, dependencies and a useful check for each. Start with reading/running an existing program, not installing another platform.
3. **test-cases.md:** a table of input/setup, action, expected behavior and defect caught. Cover valid input, empty input, correction, delete, replay, malformed record, equal-version conflict and injected write/publication failure. State which failures must preserve the checkpoint.
4. **handoff.md:** a reusable handoff structure with command, evidence and limitations fields. Since you have not implemented the task here, mark runtime evidence as not executed.

Use the shared fixture to write at least two exact expected amounts/counts. Do not write the whole loader yet: DE04–DE17 develop its implementation.

## Reflection

Which unknowns can you investigate independently, and which need a stakeholder decision before you can claim the task is correct?


## Inspect before planning

Before writing plan.md, inspect the supplied raw input. In task.md record its row
count, field names, apparent types, at least one repeated ID and one correction/delete.
Distinguish observed facts from source guarantees you still need to ask about.
This is a brief discovery step; DE27 later assesses a different source with a full profile.
