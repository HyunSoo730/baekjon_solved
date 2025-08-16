# managerId에 최소 5개.. -> 그룹핑
WITH tempA as (
    select managerId
    from Employee
    group by managerId
    having count(managerId) >= 5
)
select A.name
from Employee A 
inner join tempA B on A.id = B.managerId