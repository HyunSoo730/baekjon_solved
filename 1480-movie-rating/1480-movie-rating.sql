# user의 이름
# 가장 많은 영화를 평점한 사용자의 이름
# 2020년 2월에 평균 평점이 가장 높은 영화 이름
(
select A.name as results
from users A 
inner join MovieRating B on A.user_id = B.user_id
group by A.user_id
order by count(A.user_id) desc, A.name
limit 1 
)
union all 
(
select A.title as results
from Movies A
inner join MovieRating B on A.movie_id = B.movie_id
where DATE_FORMAT(B.created_at, "%Y-%m") = '2020-02'
group by A.movie_id, A.title 
order by AVG(B.rating) desc, A.title asc
limit 1
)