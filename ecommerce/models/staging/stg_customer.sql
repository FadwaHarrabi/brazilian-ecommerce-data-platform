{{config(materialized='table')}}
SELECT *
FROM public.customer
WHERE customer_id IS NOT NULL