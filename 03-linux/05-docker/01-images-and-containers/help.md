# Help — Docker images, containers and the engine

## First hint

The CLI and engine are separate components.

## Detailed approach

Run docker context show and docker version first. An engine connection error belongs to setup, not app.py. With Docker Desktop running, choose Linux containers and enable Settings > Resources > WSL Integration for Ubuntu. Use docker ps -a --filter name=le-demo. inspect's exit code is 0 for normal completion. Do not reset Docker Desktop or remove other containers to repair a lab name collision.

## Troubleshooting

A missing named pipe or unavailable socket indicates an engine/context issue. Docker's internal docker-desktop WSL distribution is not your Ubuntu learning shell.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
