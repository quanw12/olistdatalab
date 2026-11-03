select
    trim(seller_id)                    as seller_id,
    trim(seller_zip_code_prefix)       as zip_code_prefix,
    lower(trim(seller_city))           as city,
    upper(trim(seller_state))          as state
from {{ source('bronze', 'sellers') }}
