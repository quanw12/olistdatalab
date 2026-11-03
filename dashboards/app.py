"""Streamlit dashboard over the gold marts.

    pip install -e ".[dashboard]"
    streamlit run dashboards/app.py

Reads DuckDB read-only, so it can stay open while nothing is writing. For a shared BI tool use
`olist serve` + Metabase on Postgres instead (docker compose up -d postgres metabase).
"""

from __future__ import annotations

import duckdb
import plotly.express as px
import streamlit as st

from olist_platform.config import get_settings

st.set_page_config(page_title="Olist platform", layout="wide")


@st.cache_data(ttl=300)
def query(sql: str):
    with duckdb.connect(str(get_settings().duckdb_path), read_only=True) as con:
        return con.execute(sql).df()


st.title("Olist marketplace")
st.caption("Revenue here is payments (what customers paid), not item prices. "
           "See docs/data-contract.md.")

kpi = query("""
    SELECT count(*) AS orders,
           sum(payment_total) AS payments_brl,
           sum(payment_total_usd) AS payments_usd,
           avg(CASE WHEN is_late THEN 1.0 WHEN NOT is_late THEN 0.0 END) AS late_rate
    FROM marts.fct_orders
""").iloc[0]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Orders", f"{kpi.orders:,.0f}")
c2.metric("Payments (BRL)", f"{kpi.payments_brl:,.0f}")
c3.metric("Payments (USD)", f"{kpi.payments_usd:,.0f}")
c4.metric("Late deliveries", f"{kpi.late_rate:.1%}")

monthly = query("""
    SELECT date_trunc('month', order_date) AS month, sum(payments_brl) AS payments_brl,
           sum(orders) AS orders
    FROM marts.mart_daily_revenue GROUP BY 1 ORDER BY 1
""")
st.plotly_chart(px.bar(monthly, x="month", y="payments_brl", title="Payments per month (BRL)"),
                use_container_width=True)

left, right = st.columns(2)
late_by_state = query("""
    SELECT customer_state, count(*) AS orders,
           avg(CASE WHEN is_late THEN 1.0 ELSE 0.0 END) AS late_rate
    FROM marts.fct_orders WHERE is_late IS NOT NULL
    GROUP BY 1 HAVING count(*) >= 20 ORDER BY late_rate DESC
""")
left.plotly_chart(px.bar(late_by_state, x="customer_state", y="late_rate",
                         title="Late delivery rate by customer state"),
                  use_container_width=True)

try:
    topics = query("""
        WITH current_labels AS (
            SELECT l.* FROM ai.review_labels l
            JOIN staging.stg_order_reviews r USING (review_id, order_id)
            WHERE l.input_sha256 = sha256(r.comment_message)
            QUALIFY row_number() OVER (
                PARTITION BY review_id, order_id
                ORDER BY labeled_at DESC, model DESC, provider DESC, prompt_version DESC
            ) = 1
        )
        SELECT topic, sentiment, count(*) AS reviews FROM current_labels
        GROUP BY ALL ORDER BY reviews DESC
    """)
    right.plotly_chart(px.bar(topics, x="topic", y="reviews", color="sentiment",
                              title="Review topics (LLM labels)"),
                       use_container_width=True)
except (duckdb.CatalogException, duckdb.BinderException):
    right.info("Run `olist ai-label` to see review topics.")
