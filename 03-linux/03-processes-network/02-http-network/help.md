# Help — Ports, HTTP and local network diagnosis

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

First decide which network/HTTP layer failed.

</details>

<details>
<summary>Detailed approach</summary>

A 200 response serves the file. With -i, curl displays response headers/body and does not automatically fail on 404. With -f, an HTTP error yields nonzero status (commonly 22); capture it immediately. After stopping the server, connection refusal is a transport outcome. --connect-timeout limits connection establishment and --max-time bounds the transfer. Use the same port in both terminals. No external endpoint is required.

</details>

<details>
<summary>Troubleshooting</summary>

A successful TCP connection can still return a bad HTTP status. A server serving the wrong --directory can give a 404 for an existing file. Running the server in foreground occupies that terminal until stopped.

</details>
