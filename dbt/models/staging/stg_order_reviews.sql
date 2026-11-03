select
    trim(review_id)                                   as review_id,
    trim(order_id)                                    as order_id,
    review_score::integer                             as review_score,
    nullif(trim(review_comment_title), '')            as comment_title,
    nullif(trim(review_comment_message), '')          as comment_message,
    {{ local_ts('review_creation_date') }}::date      as review_created_date,
    {{ to_utc('review_answer_timestamp') }}           as answered_at_utc
from {{ source('bronze', 'order_reviews') }}
