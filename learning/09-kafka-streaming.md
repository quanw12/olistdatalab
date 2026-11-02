# 09 · Streaming with Kafka

**Time:** weeks 11–12 · **Stack:** Apache Kafka (KRaft), confluent-kafka Python client

## Why
Orders, clicks and payments arrive continuously. Streaming questions (offsets, delivery
guarantees, late events) are common in interviews for e-commerce and fintech.

## Learn
- Topic, partition, offset, consumer group, rebalance — [Kafka intro](https://kafka.apache.org/intro)
- Keys and ordering (ordering is per partition)
- At-most-once / at-least-once / exactly-once; idempotent producer
- Event time vs processing time; late and out-of-order events; dead-letter queues
- Schema evolution (why events carry `schema_version`)

## Read in this repo
- `src/olist_platform/streaming.py` — producer keyed by `order_id`; consumer commits after the write.
- `tests/test_streaming.py` — idempotency, out-of-order, dead letter, without a broker.

## Build
1. `docker compose up -d kafka`, `pip install -e ".[stream]"`. In two terminals:
   `olist stream-consume --idle 30` and `olist stream-produce --limit 500`.
   **Check:** `live.order_events` count = events produced; `live.order_status` = one row per order.
2. Kill the consumer mid-way (Ctrl+C), restart it. Prove no duplicates and no loss with a query.
3. Add a windowed metric: orders per 10-minute window of *event time*, written to `live.orders_per_window`.
4. Add a `payment_received` event type with schema version 2; keep the consumer accepting v1 and v2.
5. Run 3 consumers in the same group (`--partitions 3`); watch the rebalance in the logs.
6. Optional: Kafka Connect or Spark Structured Streaming reading the same topic.

## Break it
- Produce a message that is not JSON with the console producer
  (`docker compose exec kafka /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic olist.orders.v1`).
  Where does it end up?
- Commit offsets *before* writing, crash in between. What is lost?

## Interview questions
- How does your consumer behave if it crashes after writing but before committing?
- Why key by `order_id`?
- How do you handle an event that arrives 2 hours late?

## Done when
- [ ] End-to-end run with the broker, crash/restart proof query saved
- [ ] Windowed metric and schema v2 merged with tests
