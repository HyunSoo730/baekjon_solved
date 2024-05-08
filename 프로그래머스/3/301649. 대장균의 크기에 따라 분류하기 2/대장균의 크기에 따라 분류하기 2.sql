# 대장균 정보 담은 ECOLI_DATA 테이블
# ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
# 대장균ID, 부모ID, 개체 크기,       분화되어 나온 날짜,    개체의 형질
# 최초의 대장균 개체는 NULL
# 대장균 크기 내림차순 정렬했을 때 상위 25, 50, 75, 100 나눠서 출력해야함
# 대장균 개체ID, 분류된 이름 출력
# ID에 대해 오름차순 정렬.

# WITH로 필요한 데이터 뽑아내자
# 1. 대장균 개체의 크기를 내림차순으로 정렬한 것을 행번호와 함께 따로 저장하는 테이블 하나 만들기
# 해당 데이터에서는 전체 데이터 개수도 알아야 퍼센트를 알 수 있음
WITH TEMP AS (
    SELECT ID, SIZE_OF_COLONY, ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) RN 
    FROM ECOLI_DATA
    ORDER BY SIZE_OF_COLONY DESC
)
# SELECT * FROM TEMP

SELECT ID, (
    CASE 
    WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.25 THEN "CRITICAL"
    WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.50 THEN "HIGH"
    WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.75 THEN "MEDIUM"
    ELSE "LOW"
    END
) AS COLONY_NAME
FROM TEMP
ORDER BY ID