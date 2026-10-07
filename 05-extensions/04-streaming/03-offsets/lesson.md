# ST03 — Learn

## Acknowledge after durable processing

If a consumer commits before its sink transaction succeeds, a restart may skip lost data. If it commits later, replay is possible, so the sink must tolerate duplicates. For this lab disable automatic offset commit and automatic offset storage; commit synchronously after successful sink work.

## Syntax — Python client

~~~python
from confluent_kafka import Consumer, TopicPartition
consumer = Consumer({"bootstrap.servers":"localhost:19092", "group.id":"p5-stock",
                     "enable.auto.commit":False, "enable.auto.offset.store":False,
                     "auto.offset.reset":"earliest"})
consumer.commit(offsets=[TopicPartition(topic, partition, next_offset)], asynchronous=False)
~~~
Maintain progress separately for each partition. In a batch, do not acknowledge a later success past an earlier failed delivered record. Kafka offsets can contain gaps; compute the successful prefix of delivered records, not a made-up contiguous range of every integer.

On a rebalance, partition ownership may change. Do not continue committing a revoked partition's work; the first live consumer uses one process and finite batches.

[Assignment](exercise.md) · [Hints](help.md)
