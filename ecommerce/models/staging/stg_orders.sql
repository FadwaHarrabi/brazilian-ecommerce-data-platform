SELECT 
       order_id AS Id,
       customer_id AS CustomerId,
       order_status AS Status,
       order_purchase_timestamp AS PurchaseTimestamp,
       order_approved_at AS ApprovedAt,
       order_delivered_carrier_date AS DeliveredCarrierDate,
       order_delivered_customer_date AS DeliveredCustomerDate,
       order_estimated_delivery_date AS EstimatedDeliveryDate
FROM {{source('bronze','orders')}}