"""Whole batch on the synthetic sample: ingest -> fx -> dbt build -> gold. Needs dbt-duckdb."""

import importlib.util

import duckdb
import pytest

from olist_platform.fx import load_fx
from olist_platform.ingest import ingest_all
from olist_platform.runlog import connect
from olist_platform.transform import export_gold, run_dbt

pytestmark = pytest.mark.skipif(importlib.util.find_spec("dbt") is None,
                                reason="dbt-duckdb not installed")


@pytest.fixture(scope="module")
def warehouse(tmp_path_factory):
    from olist_platform.contracts import load_contract
    from olist_platform.sample import generate

    root = tmp_path_factory.mktemp("e2e")
    landing, lake, db = root / "landing" / "olist", root / "lake", root / "olist.duckdb"
    generate(landing, n_orders=1500, seed=1)
    with connect(db) as con:
        ingest_all(con, load_contract(), landing, lake, run_id="e2e")
        load_fx(con, landing, run_id="e2e", offline=True)
    run_dbt(db, "build")  # raises if any model or dbt test fails
    with connect(db) as con:
        export_gold(con, lake)
    return db, lake


def test_fact_has_one_row_per_order(warehouse):
    db, _ = warehouse
    with duckdb.connect(str(db), read_only=True) as con:
        orders = con.execute("SELECT count(*) FROM bronze.orders").fetchone()[0]
        facts, unique = con.execute(
            "SELECT count(*), count(DISTINCT order_id) FROM marts.fct_orders").fetchone()
    assert orders == facts == unique == 1500


def test_payments_are_not_inflated_by_items(warehouse):
    db, _ = warehouse
    with duckdb.connect(str(db), read_only=True) as con:
        source = con.execute("SELECT sum(payment_value::DECIMAL(12,2)) "
                             "FROM bronze.order_payments").fetchone()[0]
        fact = con.execute("SELECT sum(payment_total) FROM marts.fct_orders").fetchone()[0]
    assert abs(source - fact) < 0.01


def test_every_order_gets_a_rate_within_the_gap(warehouse):
    db, _ = warehouse
    with duckdb.connect(str(db), read_only=True) as con:
        missing, carried = con.execute(
            "SELECT count(*) FILTER (WHERE brl_vnd IS NULL), "
            "count(*) FILTER (WHERE brl_vnd_rate_date < order_date) FROM marts.fct_orders"
        ).fetchone()
    assert missing == 0
    assert carried > 0  # the offline VND gap is filled from an earlier day, and says so


def test_unavailable_orders_keep_null_amounts(warehouse):
    db, _ = warehouse
    with duckdb.connect(str(db), read_only=True) as con:
        rows = con.execute(
            "SELECT count(*), count(items_price) FROM marts.fct_orders WHERE has_no_items"
        ).fetchone()
    assert rows[0] > 0 and rows[1] == 0


DAILY_TOTALS = "SELECT sum(orders), sum(payments_brl), count(*) FROM marts.mart_daily_revenue"


def test_incremental_rerun_matches_full_build(warehouse):
    db, _ = warehouse
    with duckdb.connect(str(db), read_only=True) as con:
        before = con.execute(DAILY_TOTALS).fetchone()
    run_dbt(db, "run")  # second run takes the incremental path
    with duckdb.connect(str(db), read_only=True) as con:
        after = con.execute(DAILY_TOTALS).fetchone()
    assert before == after


def test_gold_parquet_is_published(warehouse):
    _, lake = warehouse
    assert (lake / "gold" / "fct_orders.parquet").exists()
    assert (lake / "gold" / "mart_daily_revenue.parquet").exists()
