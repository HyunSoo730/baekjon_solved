# Write your MySQL query statement below

# 재귀적으로 풀어야함...
WITH RECURSIVE tempA as (   -- 첫번째 재귀로 level을 파악
    select employee_id, employee_name, manager_id, 1 as 'level', salary
    from Employees
    where manager_id is null -- 우선 가장 위에 CEO LEVEL 1인 애를 만들어 두고...

    union all

    select B.employee_id, B.employee_name, B.manager_id, A.level + 1, B.salary
    from tempA A
    inner join Employees B on A.employee_id = B.manager_id
)
, tempB as (        -- team_size, budget 구하기 : 각 매니저 별로 부하를 찾아야함 !!!
    select manager_id, employee_id
    from Employees 
    where manager_id is not null -- 이번에는 Base Case는 매니저가 있는 애들 전부 뽑아내 놓고 진행.

    union all

    select E.manager_id, B.employee_id      -- 본인위의 위 매니저로..!
    from tempB B 
    inner join Employees E on B.manager_id = E.employee_id
    where E.manager_id is not null
)
, tempC as (        -- team_size 구하기
    select manager_id as employee_id, COUNT(*) as cnt
    from tempB
    group by manager_id
)
, tempD as (    -- budget은 본인 급여 + 본인 부하의 모든 급여.. -> tempB 활용
    select B.manager_id
        ,sum(E.salary) as subordinate_budget    -- 본인 부하들의 급여 합
    from tempB B 
    inner join Employees E on B.employee_id = E.employee_id
    group by B.manager_id
)
select A.employee_id, A.employee_name, A.level
    ,IFNULL(C.cnt, 0) as team_size
    ,A.salary + IFNULL(D.subordinate_budget, 0) as budget
from tempA A
left join tempC C on A.employee_id = C.employee_id
left join tempD D on A.employee_id = D.manager_id
order by level asc, budget desc, employee_name asc;