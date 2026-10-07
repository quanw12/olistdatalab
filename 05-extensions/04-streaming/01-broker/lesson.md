# ST01 — Learn

## Events have positions

Kafka stores ordered records within a partition. A topic may have several partitions; there is no single cross-partition order. A consumer group assigns partitions to consumers and records progress through offsets. A committed offset names the next record to read, not the last processed record.

KRaft is Kafka's metadata controller mode; this lab needs no ZooKeeper. One broker/controller with replication factor 1 is a development setup, not high availability. Keys keep related entity events together under the chosen partitioning policy; changing partition count can change key placement.

## Syntax — inspect supplied infrastructure

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming\infra"
docker compose config --quiet
docker compose ps
~~~
Host Python connects to localhost:19092. Containers connect to broker:9092. Advertised listeners must give clients an address reachable from their network; a healthy bootstrap socket alone does not prove later broker addresses work.

The supplied Compose file is infrastructure, not an exercise solution. [Kafka 3.9 quickstart](https://kafka.apache.org/39/getting-started/quickstart/) and [Debezium 3.3 compatibility](https://debezium.io/releases/3.3/) underpin its teaching versions.

[Assignment](exercise.md) · [Hints](help.md)
