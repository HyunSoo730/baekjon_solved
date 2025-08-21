# Products 테이블은 제품의 가격 변화 나타냄

# 모든 제품의 2019-08-16의 가격 찾기 : 처음 가격은 전부 10임
# 초기는 10으로 시작
# 16일 데이터가 없다면 그 사이 가격이 얼마인지 추측하면 됨
# 즉 16일자 데이터가 있다면 해당 데이터 사용
# 16일자 데이터가 없다면 그 이전 데이터 사용.
# - 그 이전 데이터 없다면 가격 10
with tempA as (
    select product_id, 
        RANK() OVER(partition by product_id order by change_date desc) as rn,
        new_price
    from Products
    where change_date <= DATE("2019-08-16")
)
select product_id, new_price as price
from tempA 
where rn = 1
union
select product_id, 10
from Products 
where product_id not in (select product_id from tempA)