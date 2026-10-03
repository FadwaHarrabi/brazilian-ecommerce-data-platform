SELECT *
FROM {{ ref('stg_customer') }}
WHERE customer_id IS NOT NULL