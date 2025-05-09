# HR_DEPARTMENT : 회사의 부서 정보
# HR_EMPLOYEES : 회사의 사원 정보
# 부서별 평균 연봉 구하기
# 부서 ID, 영문 부서명, 평균 연봉을 조회 -> 윈도우 함수
# 평균 연봉은 소수점 첫째자리에서 반올림, 컬럼명은 AVG_SAL
# 결과는 부서별 평균 연봉 기준으로 내림차순

SELECT DISTINCT A.DEPT_ID
    ,A.DEPT_NAME_EN
    ,ROUND(AVG(B.SAL)) AS AVG_SAL
FROM HR_DEPARTMENT A 
INNER JOIN HR_EMPLOYEES B ON A.DEPT_ID = B.DEPT_ID
GROUP BY A.DEPT_ID, A.DEPT_NAME_EN
ORDER BY AVG_SAL DESC

