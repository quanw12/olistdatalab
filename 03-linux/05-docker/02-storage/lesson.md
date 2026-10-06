# Bind mounts, named volumes and persistent artifacts

## Concept and purpose

The container writable layer belongs to that container and is lost on removal. A bind mount exposes a host path. A named volume is managed by Docker and survives ordinary container removal. They serve different ownership/lifecycle needs.

Mount inputs read-only so a process cannot rewrite source fixtures through that mount. Quote host paths containing spaces. A mount hides existing image contents at its destination; do not assume both remain visible simultaneously.

Inspect volume ownership and explicit names before cleanup. docker volume rm removes stored data, so it is a deliberate destructive step for an empty disposable lab volume, not routine application shutdown. This course retains the volume while demonstrating persistence.

## Syntax example — Bash in Ubuntu

~~~bash
docker volume create le-storage
docker run --rm --mount type=volume,src=le-storage,dst=/store python:3.12-slim python -c "from pathlib import Path; Path('/store/note.txt').write_text('persistent', encoding='utf-8')"
docker run --rm --mount type=volume,src=le-storage,dst=/store python:3.12-slim python -c "from pathlib import Path; print(Path('/store/note.txt').read_text(encoding='utf-8'))"
~~~

## Trace the example

Two different disposable containers see the same volume-backed note. The volume remains after both containers disappear.

## Apply it to Data Engineering

Pipeline artifacts need a defined lifecycle independent of the container that produced them.

[Reference](https://docs.docker.com/engine/storage/volumes/). These explanations and exercises are original course material.
