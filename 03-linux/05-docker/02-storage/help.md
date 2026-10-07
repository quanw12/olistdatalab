# Help — Bind mounts, named volumes and persistent artifacts

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Container and volume lifecycles are distinct.

</details>

<details>
<summary>Detailed approach</summary>

~~~bash
docker run --rm --mount "type=bind,src=$LE_COURSE_ROOT/data,dst=/data,readonly" python:3.12-slim python -c "from pathlib import Path; print(Path('/data/events.csv').read_text())"
~~~
Inspect source paths first. For the failed write, use a new name such as /data/read-only-test.txt; never target the real fixture. Record the container's nonzero status and permission/read-only error. Do not use global prune or delete unknown volumes.

</details>

<details>
<summary>Troubleshooting</summary>

A missing bind source is a host-path problem. Without quotes, spaces can become extra CLI arguments. Mounting the wrong directory can hide required app files.

</details>
