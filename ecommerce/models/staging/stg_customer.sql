
SELECT 
      customer_id AS Id,
      Customer_unique_id AS CustomerCode,
      customer_zip_code_prefix AS ZipCode
      
FROM {{source('bronze','customer')}}
