# 종합병원에 등록된 환자정보 담음 PATIENT 테이블

# 테이블에서 12세 이하인 여자환자의
# 환자이름, 환자번호, 성별코드, 나이, 전화번호 조회
# 전화번호가 없는 경우 : NONE로 출력
# 나이 내림차순 정렬, 환자이름 오름차순

SELECT PT_NAME,PT_NO, GEND_CD, AGE, 
(
    CASE WHEN TLNO IS NULL THEN "NONE"
    WHEN TLNO IS NOT NULL THEN TLNO
    END
) AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = "W"
ORDER BY AGE DESC, PT_NAME
