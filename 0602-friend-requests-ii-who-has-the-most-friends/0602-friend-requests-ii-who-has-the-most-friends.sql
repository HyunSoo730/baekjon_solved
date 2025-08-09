WITH tempA as (
    select requester_id as idA, accepter_id as idB
    from RequestAccepted

    union 

    select accepter_id as idA, requester_id as idB
    from RequestAccepted
), tempB as (
    select idA as id, count(*) as num
    from tempA
    group by idA
)
select id, num 
from tempB
order by num desc
limit 1