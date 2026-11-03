-- Grain: one row per person (customer_unique_id), not per customer_id.
select
    customer_unique_id,
    arg_max(customer_state, purchased_at_utc)  as latest_state,
    min(order_date)                            as first_order_date,
    max(order_date)                            as last_order_date,
    count(*)                                   as order_count,
    sum(payment_total)                         as lifetime_payments
from {{ ref('fct_orders') }}
group by customer_unique_id
