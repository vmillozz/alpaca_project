
    
    

with all_values as (

    select
        trading_action as value_field,
        count(*) as n_records

    from "alpaca_warehouse"."public"."mart_trading_actions"
    group by trading_action

)

select *
from all_values
where value_field not in (
    'BUY - AI Prevede Rialzo','HOLD / SELL - AI Prevede Ribasso'
)


