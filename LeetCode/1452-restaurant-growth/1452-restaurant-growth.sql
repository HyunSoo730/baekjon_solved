# 얼마나 손님들이 7일간 제출하는지
# 7일부터 포함시키면 될듯
WITH tempA as(
    select visited_on, sum(amount) as total_amount
        ,ROW_NUMBER() OVER(order by visited_on) as rn
    from Customer
    group by visited_on
)
select visited_on
    ,(
        select sum(total_amount)
        from tempA
        where visited_on between DATE_SUB(A.visited_on, INTERVAL 6 DAY) and A.visited_on
    ) as amount
    ,ROUND((
        select avg(total_amount)
        from tempA
        where visited_on between DATE_SUB(A.visited_on, INTERVAL 6 DAY) AND A.visited_on
    ),2) as average_amount
from tempA A
where visited_on >= (
    select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    from Customer
)