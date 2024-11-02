# 상품을 구매한 회원 비율 구하기

# 쇼핑몰 가입한 회원 정보를 담은 USER_INFO 테이블(회원ID, 성별(0,1), 나이, 가입일)
# 온라인 상품 판매 정보를 담은 ONLINE_SALE 테이블(온라인 상품판매ID, 회원ID, 상품ID, 판매량, 판매일)
# 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서 하나의 판매 데이터만 존재

# 두 테이블에서
# 2021년에 가입한 전체 회원들 중 
# 상품을 구매한 회원수와 상품을 구매한 회원의 비율(2021 가입한 회원 중 상품 구매 회원수 / 2021년 가입 전체 회원수)을
# 년, 월 별로 출력.
# 상품 구매한 회원의 비율은 소수점 둘째자리에서 반올림. 
# 년 기준 오름차순, 월 기준 오름차순

WITH TEMP AS (
    SELECT USER_ID, JOINED
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
    GROUP BY USER_ID
)
,TEMP2 AS (
    SELECT COUNT(DISTINCT A.USER_ID) AS CNT
    FROM USER_INFO A
    JOIN ONLINE_SALE B
    ON A.USER_ID = B.USER_ID
)
SELECT YEAR(B.SALES_DATE) AS YEAR
    ,MONTH(B.SALES_DATE) AS MONTH
    ,COUNT(DISTINCT A.USER_ID) AS PURCHASED_USERS
    ,ROUND(COUNT(DISTINCT A.USER_ID) / (SELECT COUNT(*) FROM TEMP), 1) AS PURCHASED_RATIO
FROM TEMP A
JOIN ONLINE_SALE B
ON A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH

