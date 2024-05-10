# 동물 보호소에 들어온 동물의 정보 ANIMAL_INS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
# 동물 아이디,  생물 종,    보호 시작일,  보호 시작 시 상태,   이름,    성별 및 중성화 여부

# 동물 보호소에서 입양 보낸 동물 정보 ANIMAL_OUTS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
# 동물 아이디,  생물 종,     , 입양일,   이름,   성별 및 중성화 여부

# 중성화 수술을 거친 동물의 정보 알아내기
# 보호소에 들어올 당시에는 중성화되지 않았지만,  -> 거치지 않은 동물 : Intact
# 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름 조회   중성화된 : Spayed or Neutered
# 아이디 순으로 조회

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE "Intact%" AND
    (B.SEX_UPON_OUTCOME LIKE "Spayed%" or B.SEX_UPON_OUTCOME LIKE "Neutered%")
ORDER BY A.ANIMAL_ID
