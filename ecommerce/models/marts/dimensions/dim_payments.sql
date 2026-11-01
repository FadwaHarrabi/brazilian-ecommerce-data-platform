{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (
        ORDER BY PaymentSequential, OrderId
    ) AS Id,
    OrderId,
    PaymentSequential,
    PaymentType,
    PaymentInstallments,
    PaymentValue
FROM {{ ref('stg_payments') }}