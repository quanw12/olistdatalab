-- Grain: one row per seller.
with reviews as (
    select order_id, avg(review_score) as review_score
    from {{ ref('stg_order_reviews') }}
    group by order_id
),
seller_orders as (
    -- One row per seller/order before averaging order-level measures. Otherwise
    -- a seller's order with more items gets more weight in review/late rates.
    select seller_id, order_id, sum(price) as items_revenue_brl
    from {{ ref('fct_order_items') }}
    group by seller_id, order_id
)

select
    s.seller_id,
    s.state                                       as seller_state,
    count(distinct i.order_id)                    as orders,
    sum(i.items_revenue_brl)                      as items_revenue_brl,
    avg(r.review_score)                           as avg_review_score,
    avg(case when o.is_late then 1.0 when not o.is_late then 0.0 end) as late_delivery_rate
from {{ ref('dim_sellers') }} s
join seller_orders i using (seller_id)
join {{ ref('fct_orders') }} o using (order_id)
left join reviews r using (order_id)
group by s.seller_id, s.state
