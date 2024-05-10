# 동물 보호소에 들어온 동물 정보 ANIMAL_INS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
# 동물 아이디,   생물 종,     보호 시작일,  보호 시작 시 상태,   이름,   성별 및 중성화 여부

# 동물 보호소에서 입양 보낸 동물 정보 ANIMAL_OUTS 테이블
# ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME
# 동물 아이디,   생물 종,     입양일 ,    이름,   성별 및 중성화 여부

# 입양일 잘못 입력. 
# 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름 조회.
# 보호시작일이 빠른 순 -> 오름차순

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME ASC
