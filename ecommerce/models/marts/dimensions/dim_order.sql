{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY Id) AS Id,
    Id AS OrderId,
    -- CustomerId,
    Status,
    PurchaseTimestamp,
    ApprovedAt,
    DeliveredCarrierDate,
    DeliveredCustomerDate,
    EstimatedDeliveryDate
FROM {{ref('stg_orders')}}