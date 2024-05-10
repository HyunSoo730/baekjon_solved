# 중고 거래 게시판 정보 USED_GOODS_BOARD 테이블
# BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS
# 게시글 ID,   작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일,      거래 상태, 조회수

# 중고 거래 게시판 사용자 정보 USED_GOODS_USER 테이블
# USER_ID, NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO
# 회원 ID, 닉네임,    시 ,     도로명 주소,     상세 주소,        전화 번호

# 완료된 중고 거래의 총 금액이 70만원 이상인 사람의 -> STATUS가 DONE이면 거래 완료.
# 회원ID, 닉네임, 총거래금액 조회
# 총거래금액 기준 오름차순 정렬

SELECT B.USER_ID, B.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD A
JOIN USED_GOODS_USER B
ON A.WRITER_ID = B.USER_ID
WHERE A.STATUS = "DONE"
GROUP BY B.USER_ID, B.NICKNAME
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC