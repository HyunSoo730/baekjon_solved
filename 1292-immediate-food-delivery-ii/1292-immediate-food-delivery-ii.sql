# order_date = customer_pref_delivery_date -> immediate
# 다르면 scheduled

# 모든 손님의 즉시 주문 퍼센트 찾기 -> 소숫점 둘째자리에서 반올림
# 가장 첫 주문을 ROW_NUMBER로 찾았어도 됐겠다.
WITH tempA as (
    select customer_id
        ,order_date, customer_pref_delivery_date as pref_date
        ,ROW_NUMBER() OVER(partition by customer_id order by order_date asc) as rn
    from Delivery 
)
select ROUND(COUNT(case when order_date = pref_date then 1 end) / COUNT(*) * 100, 2) as immediate_percentage
from tempA
where rn = 1;
