{{ config(schema='gold') }}

WITH session_activity AS (
    SELECT 
        session_id,
        user_id,
        MAX(CASE WHEN user_action = 'app_open' THEN 1 ELSE 0 END) as opened_app,
        MAX(CASE WHEN user_action = 'rate_calculated' THEN 1 ELSE 0 END) as calculated_rate,
        MAX(CASE WHEN user_action = 'transfer_initiated' THEN 1 ELSE 0 END) as initiated_transfer,
        MAX(CASE WHEN user_action = 'transfer_completed' THEN 1 ELSE 0 END) as completed_transfer
    FROM {{ ref('silver_ux_logs') }}
    GROUP BY session_id, user_id
)

SELECT 
    COUNT(session_id) as total_sessions,
    SUM(opened_app) as total_app_opens,
    SUM(calculated_rate) as total_rates_calculated,
    SUM(initiated_transfer) as total_transfers_initiated,
    SUM(completed_transfer) as total_transfers_completed,
    -- Calculate Drop-offs
    (SUM(opened_app) - SUM(calculated_rate)) as dropoff_after_open,
    (SUM(calculated_rate) - SUM(initiated_transfer)) as dropoff_after_rate,
    (SUM(initiated_transfer) - SUM(completed_transfer)) as dropoff_at_checkout
FROM session_activity