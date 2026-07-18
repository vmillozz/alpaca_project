
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

with all_values as (

    select
        predicted_signal as value_field,
        count(*) as n_records

    from "alpaca_warehouse"."public"."ai_trading_signals"
    group by predicted_signal

)

select *
from all_values
where value_field not in (
    '0','1'
)



  
  
      
    ) dbt_internal_test