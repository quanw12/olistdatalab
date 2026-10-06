# Compose for a batch job and report viewer

## Concept and purpose

Compose describes services, mounts, networks and lifecycle in YAML. A service can be a one-shot batch rather than a long-running server. depends_on with service_completed_successfully can delay the viewer until the batch exits successfully; it does not make later reruns transactional.

Use the project name le-capstone to scope resources. The batch builds from the project directory and writes a named artifacts volume; web reads it and serves HTTP. The relative input bind ../data is resolved from the Compose project/file base. Do not mix Windows paths into the app's container arguments.

up -d creates/starts; run --rm batch runs a new one-shot invocation; logs and ps inspect state; down removes project containers/network while ordinary named volumes remain without -v. Artifact files are individually replaced by the supplied app; this is not a coherent multi-file snapshot for concurrent readers.

## Syntax example — Bash in Ubuntu

~~~bash
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" config --quiet
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" up --build -d
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" ps --all
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" logs batch
~~~

## Trace the example

Configuration validation checks the model before starting. A normally completed batch may be Exited (0) while web keeps running.

## Apply it to Data Engineering

A small explicit service configuration makes startup, data ownership and shutdown reproducible.

[Reference](https://docs.docker.com/compose/how-tos/startup-order/). These explanations and exercises are original course material.
