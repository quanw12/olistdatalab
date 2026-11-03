---
tags: [decourse, kafka, streaming]
module: 13
---

# Kafka: Offsets, Replay and Ordering

> [!info] Learning goals
> After this note you can: explain topics, partitions, offsets, producers, consumer groups and retention; choose message keys for ordering; reason about delivery semantics (at-most-once, at-least-once, effectively-once); commit offsets correctly; build an idempotent sink; handle out-of-order and late events with versions and watermarks; use a dead-letter queue; and replay safely.

## 1. Why event streaming

Batch pipelines process data periodically. Some needs are continuous: update order status within seconds, feed several consumers (warehouse, notifications, fraud model) from one event stream, and **replay** history into a new consumer. Kafka is a distributed, durable, append-only **log** that many producers write to and many consumers read from independently.

Kafka does not decide your business key, your event time, or give you exactly-once writes into an external database. Those are your design.

## 2. Core concepts

| Concept | Meaning |
|---|---|
| Topic | A named stream (`orders.events`) |
| Partition | An ordered, append-only log; a topic has N partitions for parallelism |
| Offset | Position of a record within one partition (0, 1, 2…); not a business time |
| Key | Determines the partition (hash of key); same key → same partition → ordered |
| Producer | Writes records; `acks=all` + idempotent producer avoids loss/duplicates on the write path |
| Consumer group | Consumers sharing work: each partition is read by exactly one consumer in the group |
| Committed offset | Where the group will resume after a restart |
| Lag | Records written but not yet processed (in offsets, not seconds) |
| Retention | How long records are kept (time/size) or compaction (keep the latest per key) |

**Ordering is per partition only.** There is no global order across partitions. If all events of an order must be processed in order, key them by `order_id`. Adding partitions later changes the key→partition mapping for new records.

**Parallelism is capped by partitions:** a group with more consumers than partitions leaves the extra consumers idle.

## 3. Delivery semantics

The question is where you commit the offset relative to processing:

| Semantics | Order of steps | Failure outcome |
|---|---|---|
| At-most-once | commit → process | Crash after commit loses the message |
| At-least-once | process → commit | Crash before commit reprocesses it (duplicate) |
| Effectively-once | at-least-once + idempotent sink | Duplicates are absorbed by the sink |

Kafka's transactional "exactly-once" covers Kafka-to-Kafka processing. When the sink is an external database, the practical answer is **at-least-once + idempotent writes** keyed by `event_id` or by `(entity, version)`.

```python
# Pattern; write_idempotently and dead_letter must be implemented durably in your lab.
messages = consumer.consume(num_messages=100, timeout=1.0)
for message in messages:
    if message.error():
        handle_broker_error(message.error())
        continue
    write_idempotently(message)  # DB transaction: event_id + state update, or DLQ
    consumer.commit(message=message, asynchronous=False)
```

Disable `enable.auto.commit` (auto-commit can commit offsets of messages you have not processed yet). If you manage offsets in batches, understand what the stored offset covers. **Never commit past a record that failed** unless it was written to the DLQ or otherwise handled by policy.

## 4. An idempotent, order-safe sink

```json
{
  "event_id": "order-o1-version-2",
  "order_id": "o1",
  "version": 2,
  "event_time": "2026-11-02T10:00:00Z",
  "schema_version": 1,
  "status": "delivered"
}
```

```python
# runnable
processed_ids: set[str] = set()
state: dict[str, dict] = {}

def handle(event: dict) -> None:
    if event["event_id"] in processed_ids:          # redelivery after a crash: ignore
        return
    current = state.get(event["order_id"])
    if current is None or event["version"] > current["version"]:
        state[event["order_id"]] = event            # only newer versions move state forward
    processed_ids.add(event["event_id"])            # in a real sink: same DB transaction

stream = [
    {"event_id": "e1", "order_id": "o1", "version": 1, "status": "shipped"},
    {"event_id": "e2", "order_id": "o1", "version": 2, "status": "delivered"},
]
for event in stream + stream[:1] + list(reversed(stream)):   # duplicates + out of order
    handle(event)
assert state["o1"]["status"] == "delivered" and len(processed_ids) == 2
```

Two layers: `event_id` dedup catches exact redeliveries; the version check stops an older event from overwriting a newer state when events arrive out of order. Deduplication by `event_id` alone does **not** keep state correct when events arrive out of order. Timestamps can tie; a version/sequence is the reliable tie-breaker.

## 5. Event time, lateness and windows

- **Event time:** when it happened (in the payload). **Processing time:** when you consume it.
- Aggregating by event time (orders per minute) needs a policy for **late** events: a **watermark** says "I assume all events up to T have arrived"; events older than the watermark are either dropped, sent to a side output, or used to correct already-emitted results.
- Window types: tumbling (fixed, non-overlapping), hopping/sliding (overlapping), session (gap-based). Stream processors (Kafka Streams, Flink, Spark Structured Streaming) implement them.

## 6. Dead-letter queues and schemas

- A **DLQ** topic receives messages that cannot be processed (invalid schema, poison messages) together with the error and original offset. Fix the cause, then **replay** the DLQ.
- A **schema** (Avro/Protobuf/JSON Schema) with a registry and compatibility rules (backward/forward) prevents producers from breaking consumers. Include `schema_version` in the envelope.

## 7. Replay

Replay = reset a consumer group's offsets (to the earliest, to a timestamp, or to a saved position) and process again. It only works if:

- the records are still within **retention**;
- the sink is **idempotent** (replay produces duplicates by design);
- side effects (emails, payments) are not repeated — separate them or guard them.

## 8. Applying it (Kafka branch)

Produce 10k events, kill the consumer **after** the DB write but **before** the offset commit, restart and reconcile by `event_id`; send a malformed message to the DLQ and replay it after a fix. Measure lag, duplicate redeliveries and recovery time. Unit tests do not prove the broker ran end to end — the drill needs a real broker (Docker Compose).

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Auto-commit with slow processing | Lost messages on crash | Manual commit after durable write |
| Commit before write | Data loss | Process → write → commit |
| No key or wrong key | Events of one entity out of order | Key by entity id |
| Dedup by event_id only | Old events overwrite new state | Version check |
| More consumers than partitions | Idle consumers | Plan partitions for parallelism |
| Replay without idempotent sink | Duplicated rows and side effects | Idempotent writes; guard side effects |

## 10. Exercises

1. Simulate a crash between write and commit with the Python sink above and prove the final state is correct.
2. Run Kafka in Docker, produce 10k keyed events, consume with 3 consumers in a group and observe partition assignment and lag.
3. Add a schema violation; route it to a DLQ with the error; fix and replay.
4. Reset the group to the earliest offset and replay everything; prove counts and state are unchanged.

## 11. Review questions

> [!question]- Does adding consumers beyond the number of partitions increase parallelism?
> No. Each partition is read by one consumer in a group; extra consumers sit idle.

> [!question]- Does a full replay need sufficient retention?
> Yes. Records deleted by retention cannot be replayed; you would need another source (e.g., raw storage) to rebuild.

> [!question]- Does dedup by event id keep state correct when events arrive out of order?
> No. It prevents processing the same event twice, but an older event with a new id can still overwrite newer state unless you compare versions.

> [!question]- Why is "exactly-once" to an external database usually implemented as at-least-once plus idempotency?
> Kafka transactions cannot include the external database's commit; making the sink idempotent turns unavoidable redeliveries into no-ops.

Related: [[Incremental CDC and Backfill]], [[Failure Drills]], [[Module 13 - Kafka]]. Sources: [Confluent Python client](https://docs.confluent.io/kafka-clients/python/current/overview.html), [Kafka delivery semantics](https://docs.confluent.io/kafka/design/delivery-semantics.html), [Apache Kafka documentation](https://kafka.apache.org/documentation/).
