-- Grain: one row per order (asserted by tests/assert_fct_orders_grain.sql).
-- Orders without items or payments keep NULL amounts, never 0, so they are not read as free.
with orders as (select * from {{ ref('stg_orders') }}),
customers as (select * from {{ ref('stg_customers') }}),
items as (select * from {{ ref('int_order_items_by_order') }}),
payments as (select * from {{ ref('int_order_payments_by_order') }}),
fx as (select * from {{ ref('int_fx_daily') }})

select
    o.order_id,
    o.customer_id,
    c.customer_unique_id,
    c.state                                   as customer_state,
    o.order_status,
    o.purchased_at_utc,
    o.purchase_date_local                     as order_date,
    o.approved_at_utc,
    o.carrier_pickup_at_utc,
    o.delivered_at_utc,
    o.estimated_delivery_date,
    date_diff('day', o.purchased_at_utc, o.delivered_at_utc)          as delivery_days,
    case when o.delivered_date_local is null then null
         else o.delivered_date_local > o.estimated_delivery_date end   as is_late,
    i.item_count,
    i.items_price,
    i.items_freight,
    i.seller_count,
    i.first_seller_id,
    p.payment_count,
    p.payment_total,
    p.payment_types,
    p.max_installments,
    p.used_voucher,
    fx.brl_usd,
    fx.brl_usd_rate_date,
    round(p.payment_total * fx.brl_usd, 2)    as payment_total_usd,
    fx.brl_vnd,
    fx.brl_vnd_rate_date,
    round(p.payment_total * fx.brl_vnd, 0)    as payment_total_vnd,
    i.order_id is null                        as has_no_items,
    p.order_id is null                        as has_no_payment
from orders o
left join customers c using (customer_id)
left join items i using (order_id)
left join payments p using (order_id)
left join fx on fx.day = o.purchase_date_local
