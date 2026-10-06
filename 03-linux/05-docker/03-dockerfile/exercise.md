# LE18 assignment

Complete project/Dockerfile and project/.dockerignore. Use python:3.12-slim, WORKDIR /app, COPY only app.py, create /output, ENTRYPOINT ["python", "/app/app.py"] and CMD ["--help"]. No pip dependencies or credentials are needed. Exclude output/, .env, .venv*/, __pycache__/, tests and workflow drafts from the context. Build le-pipeline:practice with project/ as context. Run --help, then mount data read-only and le-storage at /output to process the fixture. Record the image ID and output counts. Explain the lab image's default user and which production hardening would come later.

## Deliverables

Dockerfile, .dockerignore, notes.md and actual build/run evidence. These project files start as prompts.

## Reflection

What is the difference between RUN and the container's ENTRYPOINT?

Keep your final implementation separate from teaching examples. Record commands, exit codes and observations; a screenshot alone should not replace an explanation.
