-- customer_id is per order; customer_unique_id identifies the person.
select
    trim(customer_id)                  as customer_id,
    trim(customer_unique_id)           as customer_unique_id,
    trim(customer_zip_code_prefix)     as zip_code_prefix,
    lower(trim(customer_city))         as city,
    upper(trim(customer_state))        as state
from {{ source('bronze', 'customers') }}
