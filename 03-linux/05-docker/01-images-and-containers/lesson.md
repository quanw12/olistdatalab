# Docker images, containers and the engine

## Concept and purpose

An image packages files/configuration; a container is a runnable instance. The Docker CLI sends requests to an engine. Having docker.exe installed does not prove the engine is available. docker version must show a reachable server before this lab starts.

Docker Desktop provides the selected Linux-container engine on Windows. Enable WSL integration for your Ubuntu distribution rather than installing a second competing engine there. A one-shot container can finish normally with status 0; a stopped container is not always a failure.

run creates and starts; ps lists running containers; ps -a includes stopped ones; logs reads captured output; inspect exposes configuration/state. --rm removes the disposable container after it exits, so inspect it before removal when evidence is needed. Tags can change over time; record the pulled image digest rather than claiming perfect reproducibility from a tag alone.

## Syntax example — Bash in Ubuntu

~~~bash
docker version
docker run --name le-demo python:3.12-slim python --version
docker ps -a --filter name=le-demo
docker logs le-demo
docker inspect le-demo --format '{{.State.ExitCode}}'
docker rm le-demo
~~~

## Trace the example

The container runs Python, exits, and retains logs/state until you explicitly remove this named lab container. The engine must be reachable first.

## Apply it to Data Engineering

Distinguish application failure from an unavailable container engine.

[Reference](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/). These explanations and exercises are original course material.
