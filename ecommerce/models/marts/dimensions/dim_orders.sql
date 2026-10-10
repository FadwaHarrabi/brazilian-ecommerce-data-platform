SELECT 
       Id INT ALWAYS GENERATED AS IDENTITY PRIMARY KEY,
       Id AS OrderId,
       CustomerId,
       Status,
       PurchaseTimestamp,
       ApprovedAt,
       DeliveredCarrierDate,
       DeliveredCustomerDate,
       EstimatedDeliveryDate


FROM {{ref('stg_orders')}}