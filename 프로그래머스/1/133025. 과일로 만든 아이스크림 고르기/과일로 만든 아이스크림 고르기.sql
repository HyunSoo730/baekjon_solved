# 아이스크림 가게 상반기 주문 정보 FIRST_HALF 테이블
# 아이스크림 성분에 대한 정보 ICECREAM_INFO 테이블

# 상반기 아이스크림 총 주문량이 3000보다 높으면서 -> 조건
# 아이스크림의 주 성분이 과일인 아이스크림의 맛을 -> 조건
# 총 주문량이 큰 순서대로 -> 정렬

SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER > 3000 AND B.INGREDIENT_TYPE = "fruit_based"
ORDER BY A.TOTAL_ORDER DESC