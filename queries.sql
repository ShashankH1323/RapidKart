-- Define the core funnel steps based on the product flow
WITH funnel_events AS (
    SELECT 
        user_id,
        session_id,
        event_name,
        timestamp,
        CASE 
            WHEN event_name = 'view_cart' THEN 1
            WHEN event_name = 'enter_checkout' THEN 2
            WHEN event_name = 'select_payment' THEN 3
            WHEN event_name = 'purchase_complete' THEN 4
            ELSE NULL 
        END as step_level
    FROM event_stream
    WHERE event_name IN ('view_cart', 'enter_checkout', 'select_payment', 'purchase_complete')
      AND timestamp >= '2026-06-01'
),

-- Find the maximum step reached per user in a session
max_funnel_step AS (
    SELECT 
        user_id,
        session_id,
        MAX(step_level) as max_step
    FROM funnel_events
    GROUP BY user_id, session_id
)

-- Aggregate to see where the drop-offs occur
SELECT 
    max_step,
    COUNT(DISTINCT session_id) as session_count
FROM max_funnel_step
GROUP BY max_step
ORDER BY max_step;
