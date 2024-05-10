# 고객 정보 MEMBER_PROFILE 테이블
# MEMBER_ID, MEMBER_NAME, TLNO, GENDER, DATE_OF_BIRTH
# 회원ID,    회원 이름,    회원 연락처, 성별,  생년월일

# 리뷰 정보 REST_VIEW 테이블
# REVIEW_ID, REST_ID, MEMBER_ID, REVIEW_SCORE, REVIEW_TEXT, REVIEW_DATE
# 리뷰ID,    식당ID,  회원 ID,     점수,          리뷰 텍스트,     리뷰 작성일

# 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL
# 회원 이름, 리뷰 텍스트, 리뷰 작성일 출력. 리뷰 작성일 오름차순, 리뷰 텍스트 오름차순

# 1. 리뷰 가장 많이 작성한 회원 찾기
WITH MAX_REVIEWER AS (
    SELECT MEMBER_ID, COUNT(*) AS REVIEW_COUNT
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY REVIEW_COUNT DESC
    LIMIT 1
)
SELECT 
    MP.MEMBER_NAME, 
    RR.REVIEW_TEXT, 
    DATE_FORMAT(RR.REVIEW_DATE, "%Y-%m-%d")
FROM 
    MAX_REVIEWER MR
    JOIN REST_REVIEW RR ON MR.MEMBER_ID = RR.MEMBER_ID
    JOIN MEMBER_PROFILE MP ON RR.MEMBER_ID = MP.MEMBER_ID
ORDER BY 
    RR.REVIEW_DATE ASC, 
    RR.REVIEW_TEXT ASC;










