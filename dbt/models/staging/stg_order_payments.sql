select
    trim(order_id)                     as order_id,
    payment_sequential::integer        as payment_sequential,
    lower(trim(payment_type))          as payment_type,
    payment_installments::integer      as payment_installments,
    payment_value::decimal(12, 2)      as payment_value
from {{ source('bronze', 'order_payments') }}
