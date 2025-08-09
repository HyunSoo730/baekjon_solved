# 홀수 아이디와 짝수 아이디 자리 교환
# 최대값보다 이하인지 판단해야함.
#### 문제 
select id, CASE
    WHEN id % 2 = 1 AND id < (select MAX(id) from Seat) THEN LEAD(student, 1) OVER(order by id)
    WHEN id % 2 = 0 THEN LAG(student, 1) OVER(order by id) 
    ELSE student
    END AS student
from Seat