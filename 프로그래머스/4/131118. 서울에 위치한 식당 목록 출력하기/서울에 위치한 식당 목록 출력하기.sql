# 식당 정보 담은 REST_INFO 테이블
# 식당 리뷰 정보 담은 REST_REVIEW 테이블

# 두 테이블에서 서울에 위치한 -> LIKE 서울
# 식당들의 식당ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수 조회하기
# 리뷰 평균 점수는 소수점 세번째 자리에서 반올림
# 평균점수 내림차순, 즐겨찾기수 내림차순

SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, 
ROUND(AVG(B.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO A
JOIN REST_REVIEW B
ON A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE "서울%"
GROUP BY A.REST_ID
ORDER BY SCORE DESC, A.FAVORITES DESC
