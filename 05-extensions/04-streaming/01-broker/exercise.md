# ST01 — Assignment

Follow [live-lab.md](../live-lab.md) to inspect and start only the owned p5-streams stack, create a one-partition synthetic topic and describe it. Draw producer → topic/partition → consumer group → sink. Record broker version, port/listener mappings and replication limitations.

Do not connect the connector to your native PostgreSQL server. The provided isolated source uses PostgreSQL 17 on host port 55432, Connect on 18083 and Kafka on 19092. If Docker is unavailable, complete the concept diagram but label broker evidence incomplete.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
