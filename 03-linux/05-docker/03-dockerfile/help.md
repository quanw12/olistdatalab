# Help — Build an image and control its command

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Separate image construction from each invocation.

</details>

<details>
<summary>Detailed approach</summary>

~~~bash
docker build -t le-pipeline:practice "$LE_COURSE_ROOT/project"
docker run --rm le-pipeline:practice --help
docker run --rm --mount "type=bind,src=$LE_COURSE_ROOT/data,dst=/data,readonly" --mount type=volume,src=le-storage,dst=/output le-pipeline:practice --input /data/events.csv --output /output
~~~
Write the recipe yourself using the required instructions. COPY app.py . refers to the context root, not the folder your terminal happens to be in. The output mount persists the app artifacts. For this isolated lab, default image-user behavior is acceptable; document that a production image should consider non-root identity and volume permissions.

</details>

<details>
<summary>Troubleshooting</summary>

An invalid /app/app.py path may mean COPY/context mismatch. Bash quoting inside JSON ENTRYPOINT is not automatic. Mounting /app can hide the copied code.

</details>
