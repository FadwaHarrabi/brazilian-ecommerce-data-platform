SELECT 
    Id INT ALWAYS GENERATED AS IDENTITY PRIMARY KEY,
    Id AS ProductId,
    CategoryNameBr,
    CategoryNameEn,
    Weight,
    Length,
    Height,
    Width
FROM {{ref('stg_products')}}