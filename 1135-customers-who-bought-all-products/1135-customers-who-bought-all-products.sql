# 모든 제품을 산 손님 찾기

select customer_id
from Customer
group by customer_id
having COUNT(DISTINCT product_key) = (select COUNT(*) FROM Product)