# Write your MySQL query statement below

# 각각의 product_id에 대해,  첫 해, 가격까지 구하라 ? 

WITH tempA as (
    select product_id, quantity, price, year
        ,RANK() OVER(partition by product_id order by year asc) as rn
    from Sales
)
select product_id, year as first_year, quantity, price
from tempA
where rn = 1