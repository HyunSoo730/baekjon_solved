# order_date = customer_pref_delivery_date -> immediate
# 다르면 scheduled

# 모든 손님의 즉시 주문 퍼센트 찾기 -> 소숫점 둘째자리에서 반올림
with tempA as (
    select DISTINCT customer_id
        ,FIRST_VALUE(order_date) over(partition by customer_id order by order_date asc) as first_order_date
        ,FIRST_VALUE(customer_pref_delivery_date) over(partition by customer_id order by order_date asc) as pref_date
    from Delivery
)
select ROUND(SUM(case when first_order_date = pref_date then 1 end ) / (select COUNT(*) from tempA) * 100, 2) as immediate_percentage
from tempA;