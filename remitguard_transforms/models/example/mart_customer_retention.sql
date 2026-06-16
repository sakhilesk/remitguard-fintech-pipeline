{{ config(schema='gold') }}

WITH last_customer_transfer AS (
    SELECT
        sender_id,
        MAX(transaction_at) AS last_transfer_date,
        COUNT(transaction_id) AS total_lifetime_transactions,
        SUM(CASE WHEN transaction_status = 'Success' THEN amount_zar ELSE 0 END) AS total_value_sent_zar
    FROM {{ ref('silver_transactions') }}
    GROUP BY sender_id
)

SELECT
    sender_id,
    last_transfer_date,
    total_lifetime_transactions,
    total_value_sent_zar,
    DATEDIFF(day, last_transfer_date, GETDATE()) AS days_since_last_transfer,
    -- Flag churn risk based on typical remittance behavior (monthly sending cycles)
    CASE 
        WHEN DATEDIFF(day, last_transfer_date, GETDATE()) > 30 THEN 'High Churn Risk'
        WHEN DATEDIFF(day, last_transfer_date, GETDATE()) BETWEEN 15 AND 30 THEN 'Medium Risk'
        ELSE 'Active / Safe'
    END AS customer_retention_status
FROM last_customer_transfer