{{ config(schema='silver') }}

WITH ranked_transactions AS (
    SELECT
        CAST(transaction_id AS VARCHAR(50)) AS transaction_id,
        CAST(sender_id AS VARCHAR(50)) AS sender_id,
        UPPER(source_country) AS source_country,
        UPPER(destination_country) AS destination_country,
        CAST(amount_zar AS DECIMAL(18, 2)) AS amount_zar,
        CAST(exchange_rate AS DECIMAL(18, 4)) AS exchange_rate,
        CAST(status AS VARCHAR(20)) AS transaction_status,
        CAST(timestamp AS DATETIME) AS transaction_at,
        -- Row number orders duplicates by timestamp and tags the newest one as 1
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id 
            ORDER BY timestamp DESC
        ) as row_num
    FROM {{ source('azure_staging', 'raw_transactions') }}
    WHERE transaction_id IS NOT NULL
)

SELECT
    transaction_id,
    sender_id,
    source_country,
    destination_country,
    amount_zar,
    exchange_rate,
    transaction_status,
    transaction_at
FROM ranked_transactions
-- Only keep the unique/latest record
WHERE row_num = 1