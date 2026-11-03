select rate_date, base, quote, rate
from {{ source('bronze', 'fx_rates') }}
