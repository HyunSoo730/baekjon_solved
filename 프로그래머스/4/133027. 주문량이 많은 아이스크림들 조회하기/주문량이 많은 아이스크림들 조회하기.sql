# 아이스크림 가게의 상반기 주문 정보 FIRST_HALF 테이블
# 7월의 아이스크림 주문 정보 JULY 테이블 

# 두 테이블에서 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 조회

WITH TEMP AS (
    SELECT *
    FROM FIRST_HALF A
    UNION
    SELECT * 
    FROM JULY B
)

SELECT FLAVOR
FROM TEMP
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3