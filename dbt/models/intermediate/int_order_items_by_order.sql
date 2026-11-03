-- Items summed to the order grain BEFORE joining to orders. Joining items and payments to
-- orders directly would repeat every payment once per item and inflate revenue.
select
    order_id,
    count(*)                         as item_count,
    sum(price)                       as items_price,
    sum(freight_value)               as items_freight,
    count(distinct seller_id)        as seller_count,
    arg_min(seller_id, order_item_id) as first_seller_id
from {{ ref('stg_order_items') }}
group by order_id
