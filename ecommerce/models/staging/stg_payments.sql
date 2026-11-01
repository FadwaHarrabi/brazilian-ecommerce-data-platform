SELECT 
    order_id AS OrderId,
    payment_sequential AS PaymentSequential,
    INITCAP(REPLACE(payment_type, '_', ' ')) AS PaymentType,
    payment_installments AS PaymentInstallments,
    payment_value AS PaymentValue
FROM {{source('bronze','payments')}}