# Help — Bind mounts, named volumes and persistent artifacts

## First hint

Container and volume lifecycles are distinct.

## Detailed approach

~~~bash
docker run --rm --mount "type=bind,src=$LE_COURSE_ROOT/data,dst=/data,readonly" python:3.12-slim python -c "from pathlib import Path; print(Path('/data/events.csv').read_text())"
~~~
Inspect source paths first. For the failed write, use a new name such as /data/read-only-test.txt; never target the real fixture. Record the container's nonzero status and permission/read-only error. Do not use global prune or delete unknown volumes.

## Troubleshooting

A missing bind source is a host-path problem. Without quotes, spaces can become extra CLI arguments. Mounting the wrong directory can hide required app files.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
