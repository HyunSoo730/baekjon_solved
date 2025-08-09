# 조건1,2의 반대로 해서 진행
WITH tempA as (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) <= 1
), tempB as (
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*) > 1
), tempC as (
    select * from Insurance
)
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance i
where NOT EXISTS (
    select 1 from tempA a
    where a.tiv_2015 = i.tiv_2015
)
and NOT EXISTS (
    select 1 from tempB b
    where b.lat = i.lat and b.lon = i.lon
)