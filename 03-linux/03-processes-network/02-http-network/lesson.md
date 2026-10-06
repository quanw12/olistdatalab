# Ports, HTTP and local network diagnosis

## Concept and purpose

A host address identifies where to connect; a port identifies a listening service. 127.0.0.1 is loopback in the current network context. A container's localhost refers to that container, a distinction needed later.

DNS maps names to addresses. A TCP connection can fail before an HTTP request exists. HTTP status describes the server response; a 404 is different from connection refused. curl -i includes headers, -f treats HTTP error statuses as failure, and timeouts bound connection/wait behavior. Do not log authorization headers or tokens.

ss -ltn shows listening TCP sockets in Ubuntu. A process must actually bind a port; naming a port in documentation does not start a server. WSL-to-Windows forwarding can vary with networking configuration, so validate within Ubuntu first. A simple http.server is a local teaching server, not production hosting.

## Syntax example — Bash in Ubuntu

~~~bash
curl --fail --silent --show-error --connect-timeout 2 --max-time 5 http://127.0.0.1:8765/events.csv
ss -ltn
~~~

## Trace the example

Run the exercise's server first. curl retrieves the fixture or reports a bounded error. ss lists actual listeners.

## Apply it to Data Engineering

Separate DNS, connection, HTTP and payload failures before adding retries.

[Reference](https://curl.se/docs/manpage.html). These explanations and exercises are original course material.
