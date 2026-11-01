{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY Id) AS Id,
    Id AS ProductId,
    CategoryNameBr,
    CategoryNameEn,
    Weight,
    Length,
    Height,
    Width
FROM {{ ref('stg_products') }}