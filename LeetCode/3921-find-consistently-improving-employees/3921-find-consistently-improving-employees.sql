# Write your MySQL query statement below


# 3개의 평가들 모두 상승해야함.
# 각 직원들의 가장 최근 3개 평가. review_date 기준으로.
# 지난 3개의 리뷰 중 최신 평점과 가장 이른 평점의 차이로 개선 점수를 계산
WITH tempA as (
    select A.employee_id, A.name
        ,B.review_date, B.rating
        ,ROW_NUMBER() OVER(
                partition by A.employee_id 
                order by B.review_date desc) as rn
    from employees A 
    inner join performance_reviews B on A.employee_id = B.employee_id
)
, tempB as (
    select * from (
        select tempA.*
            ,LEAD(rating, 1) OVER(partition by employee_id order by review_date desc) as lead_rating
        from tempA
        where rn <= 3
    ) as temp
    where rating > lead_rating or lead_rating is null -- 반드시 전 달보다는 커야한다. 그리고 rn = 3 인 경우는 null이어야지
)
, tempC as (
    select employee_id, name
        ,MAX(rating) - MIN(rating) as improvement_score
    from tempB
    group by employee_id, name
    having COUNT(*) = 3
)
select * from tempC
order by improvement_score desc, name;