---
tags: [decourse, docker, postgres]
module: 10
---

# Docker, PostgreSQL and Serving

> [!info] Learning goals
> After this note you can: explain images, containers, volumes, networks and healthchecks; read and write a Dockerfile and a Compose file; run and debug a local stack (Postgres + Metabase); connect between containers vs from the host; set up PostgreSQL schemas, roles and least-privilege grants for BI readers; and publish marts so dashboards never see broken tables.

## 1. Why containers

"It works on my machine" happens because machines differ: OS, library versions, Python, Java, system packages. A **container** packages an application with its runtime and dependencies into a portable unit that runs the same on your laptop, CI and a server. Docker is the most common tool; Compose runs several containers together.

| Term | Meaning |
|---|---|
| Image | Read-only template (filesystem + metadata), built from a Dockerfile; identified by tag (`postgres:16`) and digest (`sha256:…`) |
| Container | A running (or stopped) instance of an image, with its own writable layer |
| Volume | Storage that lives outside the container lifecycle — where database files must go |
| Bind mount | A host folder mounted into the container (`./dbt:/app/dbt`) — handy for code in dev |
| Network | Lets containers reach each other by service name |
| Healthcheck | A command Docker runs to decide whether the service is ready |
| Registry | Where images are stored and pulled from (Docker Hub, GHCR, Artifact Registry) |

Containers are not virtual machines: they share the host kernel and start in seconds. A container running on a laptop is not proof of production high availability, backups or access control.

## 2. Dockerfile

```dockerfile
FROM python:3.12-slim                      # pin a base image (a digest pins it fully)
WORKDIR /app
COPY pyproject.toml constraints.txt ./
RUN pip install --no-cache-dir -c constraints.txt -e .   # dependencies first: cached layer
COPY src/ src/                             # code last: changes often
RUN useradd --create-home app
USER app                                   # do not run as root
ENTRYPOINT ["python", "-m", "olist_platform"]
CMD ["run", "--offline"]
```

Each instruction creates a cached **layer**. Order from least to most frequently changed so rebuilds are fast. Use a `.dockerignore` to keep `data/`, `.venv`, `.git` and secrets out of the build context. Never bake secrets into an image: anyone with the image can read them.

## 3. Compose: a local stack

```yaml
# docker-compose.yml (excerpt)
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: olist
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}     # from .env, never committed
      POSTGRES_DB: olist
    ports: ["5432:5432"]                          # host:container
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U olist -d olist"]
      interval: 5s
      retries: 10
  metabase:
    image: metabase/metabase:v0.50.0
    ports: ["3000:3000"]
    depends_on:
      postgres: {condition: service_healthy}
volumes:
  pgdata:
```

Commands (from the repo, Docker installed):

```bash
docker compose config                      # validate and show the merged config
docker compose up -d postgres metabase     # start in the background
docker compose ps                          # status and health
docker compose logs --tail 50 postgres     # recent logs
docker compose exec postgres psql -U olist -d olist   # shell into the database
docker compose down                        # stop and remove containers (volumes kept)
```

`docker compose config` prints resolved environment values — do not share its output if it contains real secrets. `docker compose down -v` **deletes volumes**, i.e. your database; never use it casually.

### Networking: the classic confusion

- From your **host** (laptop), Postgres is `localhost:5432` (because of the port mapping).
- From **another container** (Metabase, Airflow), it is `postgres:5432` — the service name. Inside a container, `localhost` means that container itself.

## 4. PostgreSQL as the serving layer

DuckDB is excellent for single-process analytics, but a DuckDB file allows only one writing process, and a notebook plus a pipeline writing the same file will hit lock errors. A BI tool with many concurrent readers is better served by a client–server database like PostgreSQL, with users, roles and network access.

### Schemas

Organise by layer and purpose: `raw`, `staging`, `marts`, `audit`. Consumers get access only to `marts`.

### Roles and least privilege

```sql
-- Pattern: run as an admin after the marts schema exists. Passwords never go in files.
CREATE ROLE analyst_reader NOLOGIN;                       -- a group role
GRANT USAGE ON SCHEMA marts TO analyst_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA marts TO analyst_reader;
ALTER DEFAULT PRIVILEGES FOR ROLE pipeline_writer IN SCHEMA marts
    GRANT SELECT ON TABLES TO analyst_reader;             -- future tables created by the writer
CREATE ROLE metabase LOGIN IN ROLE analyst_reader;        -- password set separately
REVOKE ALL ON SCHEMA raw FROM PUBLIC;
```

- `GRANT … ON ALL TABLES` covers **existing** tables only. Default privileges apply to tables created later **by the named role**.
- `DROP` + `CREATE` during publish loses grants, indexes and dependent views; re-apply and test after every publish, or swap data inside existing tables.
- Test permissions **as the reader**: `SET ROLE analyst_reader; SELECT … FROM marts.fct_orders;` must work, `INSERT` and `SELECT … FROM raw.…` must fail.

### Publishing without breaking readers

Load into a staging table, validate, then swap within a transaction (`ALTER TABLE … RENAME` or `DELETE`/`INSERT` in one transaction). Each table is atomic, but a dashboard reading several tables can still see them from different publishes; use a batch id or publish them together ([[Transactions Indexes and EXPLAIN]]).

## 5. Persistence and backups

Data in a container's writable layer disappears when the container is removed; data in a volume survives. A volume is **not a backup**: it lives on the same disk. Back up with `pg_dump` (logical) or file-level/managed backups, and practise restoring — a backup you have never restored is a hope, not a backup ([[Observability and Recovery]]).

## 6. Debugging checklist

1. `docker compose ps` — is the container running and healthy?
2. `docker compose logs <service>` — the first error usually explains everything.
3. Port conflict? Another Postgres on 5432 (see [[Shell Linux and PowerShell]]).
4. Connection refused from another container? Use the service name, not `localhost`.
5. Permission denied on a mounted folder? The container user differs from the host owner.
6. Changed the Dockerfile but nothing changed? Rebuild: `docker compose up -d --build`.

## 7. Applying it to Olist

One Metabase dashboard is enough. Publish the real Olist marts to Postgres, check counts and money against DuckDB, and test the reader role. Stop and remove the container, start it again with the same volume, and confirm the data is still there (on a lab volume). Run `EXPLAIN ANALYZE` before and after adding an index for a dashboard query and keep the measurements even if the index does not help.

## 8. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| `localhost` inside a container | Connection refused | Use the service name |
| Database files without a volume | Data lost on removal | Named volume |
| `down -v` casually | Database deleted | Never on data you need |
| Secrets in Dockerfile/Compose | Leaked in image/repo | `.env` (ignored) or secret manager |
| `latest` tags | Unreproducible environments | Pin tags/digests |
| Grants only on existing tables | New tables invisible to BI | Default privileges + re-test after publish |
| Running as root | Larger blast radius | `USER` in Dockerfile |

## 9. Exercises

1. Start Postgres with Compose, create `marts.daily_revenue`, connect from the host with `psql` and from Metabase.
2. Create the reader role and prove: SELECT on marts works, INSERT fails, SELECT on raw fails. Then DROP/CREATE the table and test again.
3. Remove the container, recreate it with the same volume, and verify the data persisted. Take a `pg_dump`, drop the table and restore it.
4. Write a Dockerfile for your ingest lab and run the tests inside the container.

## 10. Review questions

> [!question]- Why can a notebook and a pipeline writing the same DuckDB file lock each other?
> DuckDB allows one process to open a database file for writing at a time; a second writer fails or waits.

> [!question]- Why does BI usually read from Postgres instead of a shared DuckDB file?
> Postgres is a server built for many concurrent clients over the network, with roles, grants and connection management.

> [!question]- Is a Docker volume a backup?
> No. It survives container removal but sits on the same disk; disk loss or `down -v` destroys it. Back up and test restores separately.

> [!question]- Why must permissions be re-tested after a publish?
> DROP/CREATE removes grants, indexes and dependent views, so a reader may lose access or a dashboard may break even though the data is correct.

Related: [[Transactions Indexes and EXPLAIN]], [[Security and Governance]], [[BI Metrics and Data Products]], [[Module 10 - Docker Postgres and BI]]. Sources: [Docker get started](https://docs.docker.com/get-started/), [Compose file reference](https://docs.docker.com/reference/compose-file/), [PostgreSQL privileges](https://www.postgresql.org/docs/current/ddl-priv.html).
