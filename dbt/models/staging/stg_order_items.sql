select
    trim(order_id)                          as order_id,
    order_item_id::integer                  as order_item_id,
    trim(product_id)                        as product_id,
    trim(seller_id)                         as seller_id,
    {{ to_utc('shipping_limit_date') }}     as shipping_limit_at_utc,
    price::decimal(12, 2)                   as price,
    freight_value::decimal(12, 2)           as freight_value
from {{ source('bronze', 'order_items') }}
