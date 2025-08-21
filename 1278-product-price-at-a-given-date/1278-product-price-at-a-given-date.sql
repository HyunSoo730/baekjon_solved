# Products 테이블은 제품의 가격 변화 나타냄

# 모든 제품의 2019-08-16의 가격 찾기 : 처음 가격은 전부 10임
# 초기는 10으로 시작
# 16일 데이터가 없다면 그 사이 가격이 얼마인지 추측하면 됨
# 즉 16일자 데이터가 있다면 해당 데이터 사용
# 16일자 데이터가 없다면 그 이전 데이터 사용.
# - 그 이전 데이터 없다면 가격 10
select DISTINCT p1.product_id
    ,IFNULL(
        (select new_price
        from Products p2
        where p1.product_id = p2.product_id
        and p2.change_date <= DATE("2019-08-16")
        order by p2.change_date desc
        limit 1)
    ,10) as price
from Products p1