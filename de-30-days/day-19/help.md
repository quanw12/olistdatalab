# Day 19 — Package the pipeline with Docker Compose


1. Check that native fixture mode succeeds first. A Docker build cannot fix broken Python.
2. Write the Dockerfile with Python 3.13, /app workdir, requirements installation and package COPY. Add sql/ only if your application needs it. Do not COPY the entire repository by accident.
3. Add .dockerignore before building. Include .env, output/, caches and virtual environments.
4. In Compose, write db first, with image, env_file, ports, volume and healthcheck. Example healthcheck list: ["CMD", "pg_isready", "-U", "de_student", "-d", "weather_course"]; interval5s, timeout3s, retries10.
5. Add app with build, env_file, environment (PGHOST: db; PGPORT: "5432"), mounts and dependency health condition. Use a list command: python, -m, weather_pipeline, run, --mode, fixture, --input, /data/raw_batch.json, --output-dir, /app/output.
6. docker compose config --quiet checks syntax without printing expanded credentials. up -d db then logs db diagnoses startup. run --rm app uses the command you defined.
7. Missing input means the mount or container path is wrong. Connection refused means host/port/readiness; missing table means bootstrap, not a network problem.
8. The external volume must exist. For a truly new machine create it, start db and run your SQL through pgAdmin5433 before app. Do not claim Compose alone creates your schemas unless you implement and document an initialization method.
