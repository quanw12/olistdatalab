# 13 · Streaming with Kafka

**Level:** Advanced · **Weeks:** 23–24 · **Prerequisite:** 07, 08, 10

## Goal
Move events in real time: topics, partitions, keys, consumer groups, offsets; build a consumer
that survives crashes without losing or duplicating data.

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Kafka Tutorial for Beginners — TechWorld with Nana](https://www.youtube.com/watch?v=QkdkLdMBuL0) | Concepts first | 19 min |
| [Kafka Crash Course — Hands-On Project — TechWorld with Nana](https://www.youtube.com/watch?v=B7CwU_tNYIE) | Main course (Python + Docker) | 1 h 08 |
| [Apache Kafka 101: Your First Kafka Application — Confluent](https://www.youtube.com/watch?v=oI7VAS9KSS4) | All | 10 min |
| [Apache Kafka Crash Course — KodeKloud](https://www.youtube.com/watch?v=cNFAP9OnJjo) | Second explanation if needed | 1 h 02 |

Free structured course: [Confluent — Apache Kafka 101](https://developer.confluent.io/courses/apache-kafka/events/) and the Python course on the same site.

## 2. Read
- [Kafka introduction](https://kafka.apache.org/intro) · [Kafka quickstart](https://kafka.apache.org/quickstart)
- [confluent-kafka Python client](https://docs.confluent.io/kafka-clients/python/current/overview.html)
- [Delivery semantics (at-most / at-least / exactly once)](https://docs.confluent.io/kafka/design/delivery-semantics.html)

## 3. Syntax sheet
```python
import json
from confluent_kafka import Producer, Consumer

p = Producer({"bootstrap.servers": "localhost:9092", "enable.idempotence": True, "acks": "all"})
p.produce("topic", key="order-1", value=json.dumps({"x": 1}).encode())   # same key -> same partition
p.flush()

c = Consumer({"bootstrap.servers": "localhost:9092", "group.id": "my-group",
              "auto.offset.reset": "earliest", "enable.auto.commit": False})
c.subscribe(["topic"])
while True:
    msgs = c.consume(num_messages=100, timeout=1.0)
    batch = [m.value() for m in msgs if m.error() is None]
    if not batch:
        continue
    write_to_database(batch)          # 1. write
    c.commit(asynchronous=False)      # 2. only then commit -> at-least-once
```
```bash
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
docker compose exec kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic olist.orders.v1 --from-beginning
docker compose exec kafka /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group olist-live
```

## 4. Practice
Nana's project end to end. Then: produce 10 messages with the console producer, consume them
with two consumers in the same group, then in two different groups. Explain the difference.

## 5. Apply to the project
1. Design first (in notes): which events does an order go through? What is the key? What makes an
   event unique? What should happen with an event from the past arriving late?
2. Write **your own** `labs/13-kafka/my_consumer.py`: consume `olist.orders.v1`, validate each
   event, write to a DuckDB table with a primary key on event id (`INSERT … ON CONFLICT DO NOTHING`),
   send invalid ones to a dead-letter table, commit after writing.
3. Run with the reference producer: `docker compose up -d kafka`, `pip install -e ".[stream]"`,
   `olist stream-produce --limit 500`. **Check:** events in table = events produced.
4. Crash test: kill your consumer mid-run, restart; prove with a query: no loss, no duplicates.
5. Keep a "current status per order" table that never goes backwards when events arrive out of
   order. Hint: update only if the new event time is ≥ the stored one.
6. Compare with `src/olist_platform/streaming.py` and `tests/test_streaming.py`.
   Extension: orders per 10-minute window of event time.

## 6. Self-check
- What happens if you commit before writing and then crash?
- Why key by `order_id`?
- At-least-once + idempotent sink vs exactly-once: trade-offs?

## Done when
- [ ] Your consumer passes the crash test with a saved proof query
- [ ] Out-of-order handling and dead letter demonstrated
