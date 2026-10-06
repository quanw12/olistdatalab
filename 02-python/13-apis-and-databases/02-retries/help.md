# Help — Retry only transient failures

## First hint

Count total attempts, including the first call.

## Detailed approach

Use for attempt in range(max_attempts). On TimeoutError, if attempt == max_attempts-1 use bare raise; otherwise sleep(2**attempt). Return immediately from the successful call. Do not catch Exception or swallow failures into None.

## Troubleshooting

Four calls with max_attempts=3 is an off-by-one error. A final sleep wastes time because no call follows. Retrying ValueError violates the contract.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
