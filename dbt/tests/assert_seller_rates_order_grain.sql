-- Compare seller rates against a source-grain oracle: one vote per seller/order,
-- independent of how many item lines that seller sold on the order.
with seller_order_keys as (
    select distinct seller_id, order_id from {{ ref('fct_order_items') }}
), review_per_order as (
    select order_id, avg(review_score) as score
    from {{ ref('stg_order_reviews') }} group by order_id
), expected as (
    select k.seller_id,
           avg(case when o.is_late then 1.0 when not o.is_late then 0.0 end) as late_rate,
           avg(r.score) as review_score
    from seller_order_keys k
    join {{ ref('fct_orders') }} o using (order_id)
    left join review_per_order r using (order_id)
    group by k.seller_id
)
select m.seller_id
from {{ ref('mart_seller_performance') }} m
join expected e using (seller_id)
where abs(m.late_delivery_rate - e.late_rate) > 0.000000001
   or (m.late_delivery_rate is null) <> (e.late_rate is null)
   or abs(m.avg_review_score - e.review_score) > 0.000000001
   or (m.avg_review_score is null) <> (e.review_score is null)
