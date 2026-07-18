
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select symbol
from "alpaca_warehouse"."public"."mart_trading_actions"
where symbol is null



  
  
      
    ) dbt_internal_test