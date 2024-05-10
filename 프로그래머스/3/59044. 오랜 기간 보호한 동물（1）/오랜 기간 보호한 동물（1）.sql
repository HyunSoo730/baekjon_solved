# 동물 보호소에 들어온 동물 정보 ANIMAL_INS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
# 동물 아이디,  생물 종,  보호 시작일,    , 보호 시작 시 상태,   이름,   성별 및 중성화 여부

# 동물 보호소에서 입양 보낸 동물의 정보 ANIMAL_OUTS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
# 동물 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부

# 아직 입양을 못 간 동물 중 -> INS에는 있고, OUTS에는 없는. -> LEFT JOIN
# 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일.
# 결과 보호 시작일 순으로 조회

SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NOT NULL AND
    B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME ASC
LIMIT 3
