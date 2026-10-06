# Container networks, service names and published ports

## Concept and purpose

Containers have network namespaces. localhost inside one container refers to that container. A user-defined Docker bridge network provides service/container-name lookup among attached containers. Publishing a port makes a selected container service reachable from the host.

A server inside a container must bind an address reachable from its container network, commonly 0.0.0.0. Binding the published host port to 127.0.0.1 keeps this lab reachable only locally. These two bindings describe different sides of the connection.

Containers on the same network use the container port; the host uses the published host port. Do not publish every internal service automatically. Health, connectivity and correct report data are distinct checks.

## Syntax example — Bash in Ubuntu

~~~bash
docker network create le-network
docker run -d --name le-web --network le-network -p 127.0.0.1:8765:8000 python:3.12-slim python -m http.server 8000 --bind 0.0.0.0
curl --fail --max-time 5 http://127.0.0.1:8765/
~~~

## Trace the example

The host reaches container port 8000 through local host port 8765. The teaching server serves its current container directory; use the exercise mount/directory for artifacts.

## Apply it to Data Engineering

Correct service addresses prevent confusing database/API failures when moving a working program into containers.

[Reference](https://docs.docker.com/engine/network/). These explanations and exercises are original course material.
