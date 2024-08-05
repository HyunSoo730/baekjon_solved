# 동물 보호소에 들어온 동물의 정보 담은 ANIMAL_INS
# 동물 보호소에서 입양 보낸 동물의 정보 담은 ANIMAL_OUTS

# 두 테이블에서
# 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의
# 아이디, 생물 종, 이름 조회
# 중성화 거치지 않은 동물 : Intact
# 중성화 거친 동물 Spayed or Neutered

WITH TEMP AS (
    SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
    FROM ANIMAL_INS A
    JOIN ANIMAL_OUTS B
    ON A.ANIMAL_ID = B.ANIMAL_ID
    WHERE B.SEX_UPON_OUTCOME NOT LIKE "Intact%"
    AND A.SEX_UPON_INTAKE LIKE "Intact%"
)

SELECT *
FROM TEMP
ORDER BY ANIMAL_ID ASC