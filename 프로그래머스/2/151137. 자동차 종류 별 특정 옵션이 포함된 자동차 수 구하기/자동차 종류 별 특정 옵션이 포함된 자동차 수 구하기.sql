# 대여중인 자동차 정보 CAR_RENTAL_COMPANY_CAR 테이블
# CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
# 자동차ID, 자동차 종류, 일일 대여 요굼, 옵션리스트

# 자동차 종류는 세단, SUV, 승합차, 트럭, 리무진이 있다.

# 해당 테이블에서 통풍 시트, 열선시트, 가죽시트 중 하나 이상의 옵션이 포함된 자동차가
# 자동차 종류 별로 몇대인지 출력
# 자동차 종류 기준 오름차순 정렬
# 1. 옵션 -> IN 으로 뽑아내기
# 2. 자동차 종류 별로 group by, count

SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%통풍시트%" 
    OR OPTIONS LIKE "%열선시트%"
    OR OPTIONS LIKE "%가죽시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC