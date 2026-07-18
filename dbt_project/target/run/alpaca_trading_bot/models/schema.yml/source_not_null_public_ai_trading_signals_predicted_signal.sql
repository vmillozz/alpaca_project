
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select predicted_signal
from "alpaca_warehouse"."public"."ai_trading_signals"
where predicted_signal is null



  
  
      
    ) dbt_internal_test