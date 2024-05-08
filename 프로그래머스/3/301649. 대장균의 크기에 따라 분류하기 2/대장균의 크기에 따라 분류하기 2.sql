# 대장균 정보 담은 ECOLI_DATA 테이블
# ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
# 대장균ID, 부모ID, 개체 크기,       분화되어 나온 날짜,    개체의 형질
# 최초의 대장균 개체는 NULL
# 대장균 크기 내림차순 정렬했을 때 상위 25, 50, 75, 100 나눠서 출력해야함
# 대장균 개체ID, 분류된 이름 출력
# ID에 대해 오름차순 정렬.

SELECT ID, COLONY_NAME
FROM (
  SELECT ID,
         CASE 
           WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.25 THEN 'CRITICAL'
           WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.50 THEN 'HIGH'
           WHEN RN <= (SELECT COUNT(*) FROM ECOLI_DATA) * 0.75 THEN 'MEDIUM'
           ELSE 'LOW'
         END AS COLONY_NAME
  FROM (
    SELECT ID, SIZE_OF_COLONY, ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) AS RN
    FROM ECOLI_DATA
  ) t
) u
ORDER BY ID;