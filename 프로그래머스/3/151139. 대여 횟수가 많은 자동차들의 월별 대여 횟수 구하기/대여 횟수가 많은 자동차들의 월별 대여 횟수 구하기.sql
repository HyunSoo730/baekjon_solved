# 자동차 대여 기록 정보 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블
# HISTORY_ID, CAR_ID, START_DATE, END_DATE
# 자동차대여기록ID, 자동차ID, 대여시작일, 대여종료일

# 해당 테이블에서 대여 시작일 기준 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서
# 해당 기간 동안의 월별 자동차 ID 별 총 대여횟수 리스트 출력
# 월 기준 오름차순, 월이 같다면 자동차ID 기준 내림차순
# 특정 월 대여횟수 0이면 제외

# 1. 대여 시작일기준 2022-08 ~ 2022-10, 총 대여 횟수 5회 이상인 애들만 따로 테이블로 뽑아내기
# 2. GROUP BY를 월별, 자동차ID별 2번 , 대여횟수 확인

WITH CARS AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
)

SELECT 
    MONTH(START_DATE) AS MONTH, 
    CAR_ID, 
    COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID FROM CARS)
    AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH, CAR_ID
HAVING COUNT(*) > 0
ORDER BY MONTH ASC, CAR_ID DESC;