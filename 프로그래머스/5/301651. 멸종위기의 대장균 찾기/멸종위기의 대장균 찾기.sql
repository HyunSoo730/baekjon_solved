# WITH RECURSIVE 활용.
/*
기저 케이스 실행 -> generation_tree 테이블 생성 (1세대 데이터)
재귀 1단계 -> 새로 추가된 1세대 데이터만 활용해서 1세대 찾기
재귀 2단계 -> 새로 추가된 2세대 데이터만 활용해서 3세대 찾기
...

-> 더 이상 새로운 데이터 없으면 종료
*/
WITH RECURSIVE generation_tree as (
    -- 기저 : 1세대만 딱 1번 찾기
    SELECT ID, PARENT_ID, 1 as GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT A.ID, A.PARENT_ID, B.GENERATION + 1 AS GENERATION 
    FROM ECOLI_DATA A
    INNER JOIN generation_tree B ON A.PARENT_ID = B.ID
)
SELECT COUNT(*) AS COUNT, GENERATION
FROM generation_tree
where ID NOT IN (
    SELECT DISTINCT PARENT_ID FROM generation_tree 
    WHERE PARENT_ID IS NOT NULL
)
GROUP BY GENERATION 
ORDER BY GENERATION
