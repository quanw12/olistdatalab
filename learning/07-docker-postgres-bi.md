# 07 · Docker, PostgreSQL and BI

**Time:** week 9 · **Stack:** Docker, Docker Compose, PostgreSQL, Metabase, Superset, Power BI, Streamlit, Linux CLI

## Why
Analysts and dashboards need a database that many people can query at once. Containers make the
whole stack reproducible on any machine.

## Learn
- Image vs container vs volume; ports; healthchecks; `docker compose logs -f`
- Linux basics inside containers: `docker exec -it <c> bash`, `ps`, `env`, `cat`, `grep`
- PostgreSQL: roles, schemas, indexes, `EXPLAIN ANALYZE`
- Why build in DuckDB and serve from Postgres (single writer vs many readers)

## Read in this repo
- `docker-compose.yml`, `src/olist_platform/serve.py` (atomic swap via `__new` table + rename), `dashboards/app.py`.

## Build
1. `docker compose up -d postgres metabase`, `pip install -e ".[postgres]"`, `olist serve`.
   Connect DBeaver to Postgres and query `marts.fct_orders`.
2. Metabase (http://localhost:3000): build a dashboard with revenue per month, late rate per
   state, top sellers. Screenshot for the README.
3. Add indexes on `marts.fct_orders(order_date)` and `(customer_unique_id)` after publishing;
   show `EXPLAIN ANALYZE` before/after for one dashboard query.
4. Same dashboard in **Power BI Desktop** (connect to Postgres) or **Superset** (add it to compose).
5. `streamlit run dashboards/app.py` — add a seller drill-down page.
6. Containerise the pipeline itself: a `Dockerfile` for the `olist` CLI and a compose service
   `pipeline` that runs `olist run`.

## Break it
- `docker compose down -v` deletes the volume. What is lost, what can you rebuild, how fast?
- Open a Metabase question while `olist serve` runs. Does it ever see a half-loaded table?

## Interview questions
- Container vs virtual machine?
- Why not let the BI tool read the DuckDB file directly?
- How do you speed up a slow dashboard query?

## Done when
- [ ] Postgres + Metabase dashboard working, screenshot in README
- [ ] Pipeline image builds and runs
