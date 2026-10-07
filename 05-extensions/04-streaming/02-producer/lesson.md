# ST02 — Learn

## Enqueueing is not delivery

Producer.produce queues a record in the client. Delivery callbacks are serviced by poll/flush; you must check errors and undelivered messages before claiming success. A broker acknowledgement still does not prove that a consumer's database committed the event. [Python client API](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html).

## Syntax — Python

~~~python
from confluent_kafka import Producer
producer = Producer({"bootstrap.servers": "localhost:19092", "enable.idempotence": True})
producer.produce(topic, key=key_bytes, value=value_bytes, on_delivery=delivery_callback)
producer.poll(0)
remaining = producer.flush(10)
~~~
Supply your own callback that collects delivery errors. Idempotent producer transport behavior does not replace consumer-side replay handling. Keys use business entity ID; the event's version belongs in its payload, not a new key for every revision.

The offline contract checks bytes and keys. A live lesson additionally records topic/partition/offset from actual delivery.

[Assignment](exercise.md) · [Hints](help.md)
