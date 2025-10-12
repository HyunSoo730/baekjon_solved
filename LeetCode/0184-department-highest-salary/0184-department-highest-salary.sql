
# 각 부서의 가장 높은 임금은 받는 사람들 찾기
WITH tempA as (
    select A.id, A.name as Employee, A.salary, B.name as Department
        ,RANK() OVER(partition by A.departmentId order by A.salary desc) as rn
    from Employee A
    inner join Department B on A.departmentId = B.id
)
select Department, Employee, salary as Salary
from tempA
where rn = 1
