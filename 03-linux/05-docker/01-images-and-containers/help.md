# Help — Docker images, containers and the engine

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

The CLI and engine are separate components.

</details>

<details>
<summary>Detailed approach</summary>

Run docker context show and docker version first. An engine connection error belongs to setup, not app.py. With Docker Desktop running, choose Linux containers and enable Settings > Resources > WSL Integration for Ubuntu. Use docker ps -a --filter name=le-demo. inspect's exit code is 0 for normal completion. Do not reset Docker Desktop or remove other containers to repair a lab name collision.

</details>

<details>
<summary>Troubleshooting</summary>

A missing named pipe or unavailable socket indicates an engine/context issue. Docker's internal docker-desktop WSL distribution is not your Ubuntu learning shell.

</details>
