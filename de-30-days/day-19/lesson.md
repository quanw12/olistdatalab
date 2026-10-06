# Day 19 — Package the pipeline with Docker Compose


## A Dockerfile describes an image

A Dockerfile is a build recipe. FROM selects the base image; WORKDIR sets a container directory; COPY adds files; RUN executes during image build; CMD sets the default container command. Build-time and run-time are different.

A small unrelated example:

~~~dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY example_app/ example_app/
CMD ["python", "-m", "example_app", "--help"]
~~~

The JSON-array CMD form avoids shell interpretation. Copy dependencies before application code so changing code need not reinstall unchanged dependencies. Use python:3.13-slim for this course and record the resolved versions later.

A .dockerignore excludes .env, output/, __pycache__/, .venv*/ and other unnecessary files from the build context. Ignoring .env in Git alone does not prevent COPY from adding it to an image.

## Compose connects services

Compose is a YAML description of related containers. Indentation matters; use spaces. Our services are db and app. Inside app, localhost means app itself; PGHOST must be db and PGPORT5432. From Windows, the database is localhost5433.

Use the volume created on Day 18. Stop and remove only the old de30-pg container before Compose binds5433. This retains its external named volume:

~~~powershell
docker stop de30-pg
docker rm de30-pg
~~~

Do not remove de30_pg18. The Compose volume declaration names it explicitly:

~~~yaml
volumes:
  pgdata:
    external: true
    name: de30_pg18
~~~

Mount pgdata at /var/lib/postgresql in db, using postgres:18. Bind127.0.0.1:5433:5432. Pass db's initialization variables via env_file: .env.

## App environment and files

Add PGDATABASE=weather_course, PGUSER=de_student and PGPASSWORD to your ignored .env; PGPASSWORD must match the existing database user's password. Both POSTGRES_PASSWORD (initialization) and PGPASSWORD (client connection) are needed for different programs.

For app, use build: . and env_file: .env, override PGHOST=db/PGPORT=5432 in environment. Mount ../data to /data read-only and ./output to /app/output. Use the application command with /data/raw_batch.json, not a Windows path.

db's healthcheck can run pg_isready -U de_student -d weather_course. Use depends_on: db: condition: service_healthy for app. Startup health does not guarantee all later requests succeed; your application still handles failures. Read [startup order](https://docs.docker.com/compose/how-tos/startup-order/).

## Lifecycle commands

compose build creates the app image; up -d db starts the DB; run --rm app runs one batch; logs inspects output; down removes Compose containers/network while the external volume remains. Never add -v casually. A fresh installation still needs explicit database bootstrap; this course does not hide DDL inside every ingestion run.

Read: [Dockerfile reference](https://docs.docker.com/reference/dockerfile/), [Compose services](https://docs.docker.com/reference/compose-file/services/).
