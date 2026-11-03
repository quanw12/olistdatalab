select
    order_id,
    count(*)                                         as payment_count,
    sum(payment_value)                               as payment_total,
    max(payment_installments)                        as max_installments,
    bool_or(payment_type = 'voucher')                as used_voucher,
    string_agg(distinct payment_type, ',' order by payment_type) as payment_types
from {{ ref('stg_order_payments') }}
group by order_id
