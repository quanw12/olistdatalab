"""Order-level seller metrics must not weight orders by their item count."""

import re
from decimal import Decimal

from olist_platform.config import PROJECT_DIR


def test_multi_item_order_gets_one_vote_in_seller_quality_rates(con):
    con.execute("CREATE TABLE dim_sellers(seller_id VARCHAR, state VARCHAR)")
    con.execute("INSERT INTO dim_sellers VALUES ('s1','SP')")
    con.execute("CREATE TABLE fct_order_items "
                "(seller_id VARCHAR, order_id VARCHAR, price DECIMAL(12,2))")
    con.execute("INSERT INTO fct_order_items VALUES "
                "('s1','o1',40), ('s1','o1',60), ('s1','o2',50)")
    con.execute("CREATE TABLE fct_orders(order_id VARCHAR, is_late BOOLEAN)")
    con.execute("INSERT INTO fct_orders VALUES ('o1',false), ('o2',true)")
    con.execute("CREATE TABLE stg_order_reviews(order_id VARCHAR, review_score INTEGER)")
    con.execute("INSERT INTO stg_order_reviews VALUES ('o1',5), ('o2',1)")

    model = (PROJECT_DIR / "dbt/models/marts/mart_seller_performance.sql").read_text()
    sql = re.sub(r"\{\{\s*ref\('([a-z_]+)'\)\s*\}\}", r"\1", model)
    # Revenue includes every item; review and late rates count each order once.
    assert con.execute(sql).fetchall() == [("s1", "SP", 2, Decimal("150.00"), 3.0, 0.5)]
