#동물 보호소에 들어온 동물의 정보 테이블 ANIMAL_INS
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
# 동물 아이디, 생물 종,      보호 시작일,  보호 시작 시 상태,  이름,   성별 및 중성화 여부

# 동물 보호소에서 입양 보낸 동물의 정보 담은 테이블 ANIMAL_OUTS
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
# 동물아이디, 생물 종,        입양일,    이름,   성별 및 중성화 여부

# 입양 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이믈.  ID순으로 조회
# -> 한쪽 데이터 없음 : LEFT JOIN을 통해 추출

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.ANIMAL_ID ASC