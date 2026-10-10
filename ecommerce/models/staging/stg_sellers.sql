SELECT 
    seller_id AS Id,
    seller_zip_code_prefix AS ZipCode

FROM {{source('bronze','sellers')}}