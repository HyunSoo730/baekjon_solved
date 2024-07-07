#아이템들은 업그레이드가 가능하다.
# ITEM_A -> ITEM_B와 같이 업그레이드가 가능할 때
# ITEM_A를 ITEM_B의 PARENT 아이템, PARENT 아이템이 없는 아이템을 ROOT 아이템이라고 한다.
# ITEM_A -> ITEM_B -> ITEM_C와 같이 업그레이드가 가능한 아이템이 있다면
# ITEM_C의 PARENT : ITEM_B
# ITEM_B의 PARENT : ITEM_A
# ROOT : ITEM_A

# 아이템 정보 담은 ITEM_INFO 테이블
# 아이템 관계 나타낸 ITEM_TREE 테이블

# 희귀도(A.RARITY)가 RARE인 아이템들의
# 모든 다음 업그레이드 아이템의 아이템아이디, 아이템명, 아이템 희귀도 출력
# 아이템 ID 기준 내림차순
# B,C -> A     D,E -> B

SELECT B.ITEM_ID, (
    SELECT ITEM_NAME
    FROM ITEM_INFO T
    WHERE B.ITEM_ID = T.ITEM_ID
) AS ITEM_NAME
, (
    SELECT T.RARITY
    FROM ITEM_INFO T
    WHERE B.ITEM_ID = T.ITEM_ID
) AS RARITY
FROM ITEM_INFO A
JOIN ITEM_TREE B
ON A.ITEM_ID = B.PARENT_ITEM_ID
WHERE A.RARITY = "RARE"
ORDER BY B.ITEM_ID DESC


