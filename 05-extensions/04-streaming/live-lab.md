# Streaming live lab — owned, isolated development stack

[Track](README.md) · [Setup](../setup.md) · [Sources](../sources.md)

Use this alongside ST01–ST08. Compose configuration/SQL/connector config are supplied infrastructure; your producer, consumers and sinks remain unfinished. No services were started during authoring. The versioned images are teaching pins with registry digests, not a recommendation to operate old releases in production.

## 1. Inspect the environment (ST01)

Complete Linux LE16–LE18 first. Open Docker Desktop and confirm its Linux engine is running. Keep your native PostgreSQL/pgAdmin server separate. The stack binds only localhost, uses local-only demonstration passwords and contains synthetic data. Do not expose it or reuse its credentials elsewhere.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming\infra"
docker version
docker compose config --quiet
docker compose config --images
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail 80 broker connect source
~~~

Wait for broker/source readiness and Connect's REST response; if a command fails, inspect logs before continuing. Pulling images needs network/disk space. Host ports: Kafka 19092, source 55432, Connect 18083. Container addresses: broker:9092/source:5432. PostgreSQL is 17.6 here because Debezium 3.3 lists tested support through 17; this does not declare your native 18 incompatible with every Debezium version.

Create the synthetic topic and the CDC topic explicitly with one partition:

~~~powershell
docker compose exec broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --create --if-not-exists --topic p5-stock-events --partitions 1 --replication-factor 1
docker compose exec broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --create --if-not-exists --topic p5-cdc.public.stock --partitions 1 --replication-factor 1
docker compose exec broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --describe --topic p5-stock-events
Invoke-RestMethod "http://localhost:18083/connector-plugins"
~~~

## 2. Install the client only now (ST02)

~~~powershell
Set-Location "C:\DE Courses"
& "./.venv-extensions/Scripts/python.exe" -m pip install -r "05-extensions/requirements-streaming.txt"
& "./.venv-extensions/Scripts/python.exe" -m pip check
~~~

Implement producer.py to accept --bootstrap, --topic, --input and --batch. It reads b1/b2 from the supplied JSON wrapper and emits each row with the tested ST02 codec. Implement consumer.py with --bootstrap, --topic, --group, --db and --max-messages (plus a finite timeout). The following are target interfaces you must implement, not finished applications:

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "02-producer/producer.py" --bootstrap localhost:19092 --topic p5-stock-events --input ../data/batches.json --batch b1
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "02-producer/producer.py" --bootstrap localhost:19092 --topic p5-stock-events --input ../data/batches.json --batch b2
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "03-offsets/consumer.py" --bootstrap localhost:19092 --topic p5-stock-events --group p5-stock --db output/synthetic.sqlite --max-messages 5
~~~

consumer.py must import/use your ST04 sink or a documented module interface. Initialize its own new database with ST04/schema.sql once. Disable auto commit/store. Check poll errors; process each record durably before synchronous offset acknowledgement; close the client in finally. Re-running the producer adds new transport positions: logical replay handling must still keep state correct. Inspect group progress and database entities, not only message counts.

## 3. Register CDC (ST06–ST07)

init.sql runs once on a fresh owned source volume. It seeds M1/M2, grants the replication reader and creates p5_pub. The provided connector uses pgoutput and that publication. Keep default replica identity for the PK-only delete exercise.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming\infra"
docker compose exec source psql -U p5_admin -d p5_inventory -c "SELECT * FROM public.stock ORDER BY event_id;"
$p5ConnectorBody = Get-Content -LiteralPath "connector.json" -Raw
Invoke-RestMethod -Method Post -Uri "http://localhost:18083/connectors" -ContentType "application/json" -Body $p5ConnectorBody
Invoke-RestMethod "http://localhost:18083/connectors/p5-stock-cdc/status"
~~~

Register once. If already registered, inspect its config/status rather than repeatedly POSTing or resetting it. Require connector/task state RUNNING. Use the Kafka console consumer in a separate terminal to inspect actual events, with a finite timeout:

~~~powershell
docker compose exec broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server broker:9092 --topic p5-cdc.public.stock --from-beginning --max-messages 2 --timeout-ms 15000
~~~

## 4. Apply a native change and inspect it

~~~powershell
docker compose exec source psql -U p5_admin -d p5_inventory -c "UPDATE public.stock SET units=8 WHERE event_id='M1'; DELETE FROM public.stock WHERE event_id='M2'; INSERT INTO public.stock VALUES('M3','p02',5);"
docker compose exec source psql -U p5_admin -d p5_inventory -c "SELECT SUM(units) AS active_units FROM public.stock;"
~~~

The expected active source total is 13. Run this change sequence once; repeating the INSERT would correctly fail its primary key. A delete envelope may have only before.event_id; decode it before the following null transport tombstone. The stream is not ST02's six-field versioned event contract.

## 5. Implement the CDC sink and inject a crash

Target sink.py arguments: --bootstrap, --topic, --group, --db, --max-messages, --timeout-seconds and --crash-after-commit. Use a separate CDC database and group from the synthetic pipeline. Keep documentable stream epoch and per-entity source position; one topic/partition is an explicit assumption. Skip reapplication of ledgered positions; apply remaining accepted records in order. A transport null is a processed no-op, not another versioned delete.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming"
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "07-restart/sink.py" --bootstrap localhost:19092 --topic p5-cdc.public.stock --group p5-cdc-sink --db output/cdc.sqlite --max-messages 20 --timeout-seconds 20 --crash-after-commit
& "C:/DE Courses/.venv-extensions/Scripts/python.exe" "07-restart/sink.py" --bootstrap localhost:19092 --topic p5-cdc.public.stock --group p5-cdc-sink --db output/cdc.sqlite --max-messages 20 --timeout-seconds 20
~~~

The injected process exit must occur after SQLite commit but before Kafka commit. The second run reuses group/database and should safely replay that record. Create your own verification command/tests: active M1=8/M3=5; M2 retained deleted; active total 13; ledger position unique; no reapplication. Null/metadata behavior makes a fixed total Kafka record count an unsuitable acceptance criterion.

## 6. Troubleshoot and stop

Missing Docker pipe → engine unavailable. Broker connection after bootstrap → check advertised listener and host/container address. Connector FAILED → inspect task trace and source grants/wal_level/publication/slot. Empty sink → verify topic/group/start offset, poll errors and decoder. Do not suppress all connector errors or reset offsets to make a demonstration look successful.

~~~powershell
Set-Location "C:\DE Courses\05-extensions\04-streaming\infra"
docker compose logs --tail 100 connect broker
docker compose exec source psql -U p5_admin -d p5_inventory -c "SELECT slot_name,active,restart_lsn FROM pg_replication_slots;"
docker compose ps
docker compose down
~~~

down stops/removes only this owned Compose stack's containers/network and preserves its volumes. Do not use down -v during restart evidence: it destroys source and broker history. If you later deliberately reset the entire lab, inventory/back up the named p5-streams volumes and assign a new source epoch and matching sink/group; never reuse old position ledgers with newly created source topics. An inactive replication slot can retain WAL; this is a stopped local lab, not unattended production monitoring.
