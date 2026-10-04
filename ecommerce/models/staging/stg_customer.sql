
SELECT *
FROM {{source('bronze','customer')}}
WHERE customer_id IS NOT NULL