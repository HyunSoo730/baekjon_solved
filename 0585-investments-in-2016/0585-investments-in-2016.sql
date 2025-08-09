# tiv_2016 총합 구하기
# 조건1. tiv_2015가 같은 사람이 있는
# 조건2. (lat, lon)이 중복되지 않는

# 조건 충족 A and B
WITH tempA as (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) > 1
), tempB as (
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*) = 1
)
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance
where tiv_2015 in (select tiv_2015 from tempA) 
    and (lat, lon) in (select lat, lon from tempB)