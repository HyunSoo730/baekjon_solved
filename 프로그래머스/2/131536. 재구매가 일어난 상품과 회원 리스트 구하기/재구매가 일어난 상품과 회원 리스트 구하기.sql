# 쇼핑몰의 온라인 상품 판매 정ㅈ보 담은 ONLINE_SALE 테이블

# 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여
# 재구매한 회원 ID와 재구매한 상품 ID 출력하기
# 회원 ID 기준 오름차순 정렬, 회원 ID 같다면 상품 ID 기준 내림차순 정렬 

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC