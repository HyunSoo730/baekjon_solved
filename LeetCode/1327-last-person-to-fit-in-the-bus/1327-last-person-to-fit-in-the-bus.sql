# 버스에 기다리는 사람
# turn이 버스에 탑승하는 사람의 순서를 결정
# weight는 그 사람의 무게
# 최대 1000 kg

# 마지막 사람 찾기 무게를 초과하지 않는 마지막 사람 찾기

WITH tempA as (
    select person_id
        ,person_name
        ,weight
        ,sum(weight) over(order by turn) as total_sum
        ,turn
    from Queue
)
select person_name
from tempA
where total_sum <= 1000
order by turn desc
limit 1;