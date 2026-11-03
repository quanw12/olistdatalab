# 10 · Docker, PostgreSQL and BI

> **Theory notes:** [[Docker PostgreSQL and Serving]] · [[Transactions Indexes and EXPLAIN]] · [[BI Metrics and Data Products]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]. Videos are optional: use the diagnostic test to decide what to watch.

**Weeks:** 17–18 · **Prerequisites:** 02, 03, 09

## Goal
Run any service reproducibly with Docker Compose, serve marts from PostgreSQL to many readers,
and build a dashboard people can use (Metabase / Power BI / Streamlit).

## 1. Watch
| Video | What to watch | Length |
|---|---|---|
| [Docker Crash Course for Absolute Beginners — TechWorld with Nana](https://www.youtube.com/watch?v=pg19Z8LL06w) | All | 1 h 08 |
| [Ultimate Docker Compose Tutorial — TechWorld with Nana](https://www.youtube.com/watch?v=SXwC9fSwct8) | All | 1 h 03 |
| [Docker for Data Engineering: Postgres, Compose — DataTalksClub](https://www.youtube.com/watch?v=lP8xXebHmuE) | All — the data-engineering angle | 2 h 11 |
| [Learn PostgreSQL — freeCodeCamp](https://www.youtube.com/watch?v=qw--VYLpxG4) | Skim; focus on constraints, indexes | 4 h 20 |
| [Metabase tutorial in under 40 min — Actiondesk](https://www.youtube.com/watch?v=LJ0l2HZ8Lp8) | All | 39 min |
| [Power BI for Data Analytics — Luke Barousse](https://www.youtube.com/watch?v=FwjaHCVNBWA) | First 2 h (connect, model, visuals) | 8 h |
| [Streamlit Mini Course — Tech With Tim](https://www.youtube.com/watch?v=o8p7uQCGD0U) | First 45 min | 1 h 36 |

## 2. Read
- [Docker: get started](https://docs.docker.com/get-started/) · [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [PostgreSQL: indexes](https://www.postgresql.org/docs/current/indexes.html) · [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- [DuckDB postgres extension](https://duckdb.org/docs/stable/core_extensions/postgres)
- [Metabase docs](https://www.metabase.com/docs/latest/) · [Streamlit docs](https://docs.streamlit.io/)

## 3. Syntax sheet
```bash
docker compose up -d postgres            # start one service in the background
docker compose ps                        # what runs, health
docker compose logs -f postgres          # follow logs
docker compose exec postgres psql -U olist -d olist   # a shell inside
docker compose down                      # stop (keeps volumes); add -v to delete data
```
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -e .
ENTRYPOINT ["olist"]
```
```sql
-- PostgreSQL
CREATE INDEX ON marts.fct_orders (order_date);
EXPLAIN ANALYZE SELECT ... ;            -- real plan + timing
```

## 4. Practice
Run `postgres:16` with a volume, create a table, stop and remove the container, start a new one
on the same volume — is the data still there? Then without the volume.

## 5. Apply to the project
1. Read `docker-compose.yml`: for each service write one line on ports, volumes, healthcheck.
2. `docker compose up -d postgres metabase`, `pip install -e ".[postgres]"`, `olist serve`.
   Query `marts.fct_orders` from DBeaver.
3. Metabase (http://localhost:3000): dashboard with payments per month, late-delivery rate by
   state, top 10 sellers. Screenshot → `docs/img/`.
4. Indexes: pick the slowest dashboard query, `EXPLAIN ANALYZE` before and after an index.
5. Write a `Dockerfile` for the pipeline CLI and a compose service `pipeline` that runs `olist run`.
   Hint: the data folder must be a volume; the DuckDB path comes from an env var.
6. Optional: same dashboard in **Power BI Desktop** (Get Data → PostgreSQL), or add **Superset** to compose.
7. Optional: extend `dashboards/app.py` (Streamlit) with a seller drill-down page.

## 6. Self-check
- Image vs container vs volume?
- Why serve from Postgres instead of letting BI read the DuckDB file?
- How does `olist serve` avoid showing a half-loaded table?

## Done when
- [ ] Dashboard screenshot committed, pipeline image runs `olist run`
- [ ] One index with before/after timing in your notes

## Product-focused requirements

Pick one dashboard (Metabase or Power BI); a second dashboard or a Streamlit drill-down is an extension. Mandatory: a transaction with rollback, observing a lock with two lab sessions, and EXPLAIN before/after an index. Create a reader role, check that SELECT works and that INSERT and raw access are denied; re-check after a publish, because DROP/CREATE can lose grants and indexes. Per-table atomicity is not atomicity of the whole dataset.
