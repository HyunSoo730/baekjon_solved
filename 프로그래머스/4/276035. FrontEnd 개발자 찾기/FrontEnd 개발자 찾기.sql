# SKILLCODES : 개발자들이 사용하는 프로그래밍 언어에 대한 정보를 담은 테이블
# DEVELOPERS : 개발자들의 프로그래밍 스킬 정보를 담은 테이블

# DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보 조회.
# ID, 이메일, 이름, 성 조회, 결과는 ID 기준 오름차순 정렬

# 먼저 SKILLCODES 테이블에서 Front End 카테고리에 해당하는 스킬들의 코드 값 찾기
# 그 다음 DEVELOPERS 테이블에서 해당 Front End 스킬 코드를 가진 개발자 찾기
# --> 비트 연산 사용해서 코드 값이 일치하는지 확인
# --> 조인 조건을 컬럼이 같은 것으로 판별하는 일반적인 문제가 아니라 ! 비트 연산을 섞어주면 됐음. 

SELECT DISTINCT B.ID, B.EMAIL, B.FIRST_NAME, B.LAST_NAME
FROM SKILLCODES A
INNER JOIN DEVELOPERS B ON (A.CODE & B.SKILL_CODE) = A.CODE
WHERE CATEGORY = 'Front End'
ORDER BY B.ID ASC