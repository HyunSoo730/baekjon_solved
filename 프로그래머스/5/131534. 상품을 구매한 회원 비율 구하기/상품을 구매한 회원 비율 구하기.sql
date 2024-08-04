# 쇼핑몰에 가입한 회원 정보 담은 USER_INFO 테이블
# 온라인 상품 판매 정보를 담은 ONLINE_SALE 테이블

# 두 테이블에서 2021년에 가입한 전체 회원들 중
# 상품을 구매한 회원수와 상품을 구매한 회원의 비율
# -> 2021년에 가입한 회원 중 상품을 구매한 회원 수 / 2021년에 가입한 전체 회원 수)
# 이 값을 년, 월 별로 출력 -> 상품을 구매한 회원의 비율은 소수점 둘째자리에서 반올림
# 년 기준 오름차순, 월 기준 오름차순

WITH TEMP AS (  # 2021년에 가입한 user만 추출
    SELECT USER_ID
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
    GROUP BY USER_ID
)

SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH,
        COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS,
        ROUND(COUNT(DISTINCT A.USER_ID) / (SELECT COUNT(*) FROM TEMP),1) AS PURCHASED_RATIO
FROM USER_INFO A
JOIN ONLINE_SALE B
ON A.USER_ID = B.USER_ID
WHERE A.USER_ID IN (
    SELECT USER_ID FROM TEMP
)
GROUP BY YEAR, MONTH
ORDER BY YEAR ASC, MONTH ASC