# Help — Ports, HTTP and local network diagnosis

## First hint

First decide which network/HTTP layer failed.

## Detailed approach

A 200 response serves the file. With -i, curl displays response headers/body and does not automatically fail on 404. With -f, an HTTP error yields nonzero status (commonly 22); capture it immediately. After stopping the server, connection refusal is a transport outcome. --connect-timeout limits connection establishment and --max-time bounds the transfer. Use the same port in both terminals. No external endpoint is required.

## Troubleshooting

A successful TCP connection can still return a bad HTTP status. A server serving the wrong --directory can give a 404 for an existing file. Running the server in foreground occupies that terminal until stopped.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
