# 각 부서 별 top 3 연봉자. 
# 근데 같아도 추가되어야 함.
WITH tempA as (
    select B.name as Department, A.name as Employee, A.salary
    ,DENSE_RANK() OVER(partition by A.departmentId order by A.salary desc) as rn
    from Employee A
    inner join Department B on A.departmentId = B.id
)
select Department, Employee, Salary
from tempA
where rn <= 3
order by Salary desc, Department;