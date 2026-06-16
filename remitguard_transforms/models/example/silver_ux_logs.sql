{{ config(schema='silver') }}

SELECT
    CAST(user_id AS VARCHAR(50)) AS user_id,
    CAST(session_id AS VARCHAR(50)) AS session_id,
    LOWER(device_type) AS device_type,
    LOWER(action) AS user_action,
    CAST(timestamp AS DATETIME) AS action_at
FROM {{ source('azure_staging', 'raw_ux_logs') }}