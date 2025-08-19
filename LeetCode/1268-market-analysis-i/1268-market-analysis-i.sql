# Orders 테이블에 user 정보, item 정보 모두 포함
# 각각의 유저에 대해서 join_date, 2019년에 구매한 수
# -> buyer_id로 묶어서
WITH tempA as (
    select DISTINCT A.user_id as buyer_id, A.join_date
        ,count(B.order_date) over(partition by B.buyer_id) as orders_in_2019
    from Users A
    left join Orders B on A.user_id = B.buyer_id
    and YEAR(B.order_date) = 2019
)
select * from tempA
order by buyer_id asc;