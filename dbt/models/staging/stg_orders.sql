-- One row per order. Timestamps: *_at_utc for durations and ordering, *_date_local for the
-- business calendar (an order placed at 22:00 in Sao Paulo belongs to that Sao Paulo day).
select
    trim(order_id)                                   as order_id,
    trim(customer_id)                                as customer_id,
    lower(trim(order_status))                        as order_status,
    {{ to_utc('order_purchase_timestamp') }}         as purchased_at_utc,
    {{ to_utc('order_approved_at') }}                as approved_at_utc,
    {{ to_utc('order_delivered_carrier_date') }}     as carrier_pickup_at_utc,
    {{ to_utc('order_delivered_customer_date') }}    as delivered_at_utc,
    {{ local_ts('order_purchase_timestamp') }}::date as purchase_date_local,
    {{ local_ts('order_delivered_customer_date') }}::date as delivered_date_local,
    {{ local_ts('order_estimated_delivery_date') }}::date as estimated_delivery_date
from {{ source('bronze', 'orders') }}
