# Help — Compose for a batch job and report viewer

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Startup ordering and ongoing publication consistency are different properties.

</details>

<details>
<summary>Detailed approach</summary>

Compose uses spaces for indentation. The dependency shape is:
~~~yaml
depends_on:
  batch:
    condition: service_completed_successfully
~~~
That belongs under web. batch's command should be a YAML argument list so values remain separate. run --rm batch creates a new batch invocation; it does not reset the named artifacts volume. Keep all commands on the same -p le-capstone project and file path. Record config output carefully; no secret variables are needed here.

Build your file around this structure; fill the service settings from the assignment:

~~~yaml
services:
  batch:
    build: .
    # Add this service's command and volumes here.
  web:
    image: python:3.12-slim
    # Add command, volumes, ports, and depends_on here.
volumes:
  artifacts:
~~~

`volumes` at the bottom declares a named volume. A service's volumes is a list of mounts; for example `- artifacts:/output` goes beneath batch's volumes, while web's mount adds `:ro`. An argument list uses syntax such as `command: ["--input", "/data/events.csv", "--output", "/output"]`. Ports is a list, with the mapping quoted as `- "127.0.0.1:8765:8000"`. Use two spaces per nesting level and no tabs.

After the lesson's config/up/ps/logs commands, inspect the report and rehearse the lifecycle:

~~~bash
curl --fail --max-time 5 http://127.0.0.1:8765/manifest.json
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" run --rm batch
curl --fail --max-time 5 http://127.0.0.1:8765/report.json
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" down
docker volume inspect le-capstone_artifacts
docker compose -p le-capstone -f "$LE_COURSE_ROOT/project/compose.yaml" up -d
~~~

Check the new batch's exit status and viewer response again; merely seeing the volume exist does not prove a successful rerun.

</details>

<details>
<summary>Troubleshooting</summary>

A successful one-shot batch showing Exited(0) is expected. web must bind 0.0.0.0 inside the container. If batch fails, inspect its logs before replacing depends_on with an arbitrary sleep.

</details>
