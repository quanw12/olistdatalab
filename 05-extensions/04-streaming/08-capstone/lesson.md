# ST08 — Learn

## Separate contracts, connect evidence

The synthetic versioned event pipeline and the native CDC pipeline both use Kafka, but their source semantics differ. Keep two explicit adapters/sink contracts. Share tested transport validation, logging and manual offset behavior only where the interfaces agree.

## Syntax — inspect the live system

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming\infra"
docker compose exec broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server broker:9092 --describe --group p5-stock
Invoke-RestMethod "http://localhost:18083/connectors/p5-stock-cdc/status"
~~~
Group lag reports position progress, not business correctness. Reconcile the sink's active entities/units to the source and check delete markers. A topic full of messages does not prove a correct report.

Keep the runbook explicit about one broker, one CDC partition, source epoch, WAL retention, quarantine/outbox behavior and the two commit boundaries. Scale/distributed exactly-once operation is outside this small lab.

[Assignment](exercise.md) · [Hints](help.md)
