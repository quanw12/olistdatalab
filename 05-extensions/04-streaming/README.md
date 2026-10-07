# Streaming and CDC

[Part 5](../README.md) · [Setup](../setup.md) · [Progress](../progress.md)

Cross a real continuous-change boundary. [Live lab](live-lab.md) explains Docker/listeners/source/connector/client/restart steps. Kafka/CDC evidence requires actually running that stack; offline decoders do not substitute.

Follow these eight lessons in order. Read each guide, then concepts/syntax, assignment, progressive help and acceptance criteria. A lesson is a unit of work, not necessarily a calendar day. Commit commands are included in every guide.

| Lesson | Focus | Verification |
|---|---|---|
| [ST01](01-broker/guide.md) | Understand topics, partitions and a local broker | Manual evidence |
| [ST02](02-producer/guide.md) | Publish keyed records and confirm delivery | Offline contract + evidence |
| [ST03](03-offsets/guide.md) | Commit only the safe processed prefix | Offline contract + evidence |
| [ST04](04-sink/guide.md) | Make a transactional sink tolerate replay | Offline contract + evidence |
| [ST05](05-rejections/guide.md) | Quarantine poison data without hiding infrastructure failures | Offline contract + evidence |
| [ST06](06-cdc/guide.md) | Interpret real PostgreSQL change envelopes | Offline contract + evidence |
| [ST07](07-restart/guide.md) | Capture changes and recover after a consumer crash | Manual evidence |
| [ST08](08-capstone/guide.md) | Deliver a streaming and CDC recovery demo | Manual evidence |

## Exit check

Keyed Kafka records and PostgreSQL CDC with manual offsets, a transactional sink and crash/restart proof. Demonstrate one successful run, one failure and recovery, one unfamiliar input and a clear English explanation. Record guided versus independent work honestly. Update only progress you have actually demonstrated.
