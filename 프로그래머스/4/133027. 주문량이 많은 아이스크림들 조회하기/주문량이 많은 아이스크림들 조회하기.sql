# 아이스크림 가게 상반기 주문정보 담은 FIRST_HALF 테이블
# SHIPMENT_ID(출하번호), FLAVOR(아이스크림 맛), TOTAL_ORDER(상반기 아이스크림 총무준량)
# 7월의 아이스크림 주문 정보 담은 JULY 테이블
# SHIPMENT_ID(출하번호), FLAVOR(아이스크림 맛), TOTAL_ORDER(7월 아이스크림 총 주문량)

# 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 조회
SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN JULY J ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY SUM(F.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3;