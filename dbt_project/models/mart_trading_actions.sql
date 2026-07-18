{{ config(materialized='table') }}

SELECT 
    timestamp,
    symbol,
    close as current_price,
    predicted_signal,
    CASE 
        WHEN predicted_signal = 1 THEN 'BUY - AI Prevede Rialzo'
        WHEN predicted_signal = 0 THEN 'HOLD / SELL - AI Prevede Ribasso'
    END as trading_action
FROM {{ source('public', 'ai_trading_signals') }}
ORDER BY timestamp DESC