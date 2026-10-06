# Help — Build an image and control its command

## First hint

Separate image construction from each invocation.

## Detailed approach

~~~bash
docker build -t le-pipeline:practice "$LE_COURSE_ROOT/project"
docker run --rm le-pipeline:practice --help
docker run --rm --mount "type=bind,src=$LE_COURSE_ROOT/data,dst=/data,readonly" --mount type=volume,src=le-storage,dst=/output le-pipeline:practice --input /data/events.csv --output /output
~~~
Write the recipe yourself using the required instructions. COPY app.py . refers to the context root, not the folder your terminal happens to be in. The output mount persists the app artifacts. For this isolated lab, default image-user behavior is acceptable; document that a production image should consider non-root identity and volume permissions.

## Troubleshooting

An invalid /app/app.py path may mean COPY/context mismatch. Bash quoting inside JSON ENTRYPOINT is not automatic. Mounting /app can hide the copied code.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
