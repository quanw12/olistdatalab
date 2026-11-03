{{
  config(
    materialized='incremental',
    unique_key='order_date',
    incremental_strategy='delete+insert'
  )
}}
-- Grain: one row per Sao Paulo business day. Incremental: each run recomputes only the last
-- incremental_lookback_days days already in the table plus anything newer, so late status
-- changes within that window are picked up. Older updates, deletes and emptied days
-- need explicit backfill/full-refresh; see learning module 19. This is not general CDC.
select
    order_date,
    count(*)                                              as orders,
    count(*) filter (where order_status = 'delivered')    as delivered_orders,
    count(*) filter (where order_status = 'canceled')     as canceled_orders,
    sum(items_price)                                      as items_revenue_brl,
    sum(payment_total)                                    as payments_brl,
    sum(payment_total_usd)                                as payments_usd,
    avg(case when is_late then 1.0 when not is_late then 0.0 end) as late_delivery_rate
from {{ ref('fct_orders') }}
{% if is_incremental() %}
where order_date >= (
    select max(order_date) - {{ var('incremental_lookback_days') }} from {{ this }}
)
{% endif %}
group by order_date
