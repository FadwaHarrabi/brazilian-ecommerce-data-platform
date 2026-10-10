SELECT 
     O.CustomerId AS IdCustomer

FROM {{ref('stg_orders')}} O
LEFT JOIN {{ref('stg_customer')}} C
ON O.CustomerId=C.Id
LEFT JOIN {{ref('')}}