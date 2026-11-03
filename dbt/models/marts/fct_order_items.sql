-- Grain: one row per item line. Use for product / seller / category revenue.
select
    i.order_id,
    i.order_item_id,
    i.product_id,
    i.seller_id,
    o.customer_unique_id,
    o.order_date,
    o.order_status,
    p.category,
    i.price,
    i.freight_value
from {{ ref('stg_order_items') }} i
join {{ ref('fct_orders') }} o using (order_id)
left join {{ ref('stg_products') }} p using (product_id)
