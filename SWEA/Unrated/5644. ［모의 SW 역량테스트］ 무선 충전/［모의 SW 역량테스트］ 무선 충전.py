
# 최적의 배터리 선택.
# 충전범위 C 이하이면 해당 배터리 접속 가능.  (맨해튼 거리)
# 배터리 2개 이상에 속하면 둘 중 하나를 선택해 접속 가능
# 만약 한 배터리에 두 명의 사용자 접속 -> 접속한 사용자 수만큼 균등하게 분배
# 사용자는 총 2명. 초기위치(0초)부터 충전 가능. 동시에 같은 위치 이동 가능
# 시작부터 각 유저가 배터리에 속한지 확인해야함. 여러개 -> 경우의 수 모두 확인
# A는 (1,1) B는 (10,10)에서 출발

dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1] # 이동X, 상, 우, 하, 좌
def 최대충전량(userA,userB):
    # 두 유저가 속하는 배터리를 받아와서 최대 충전량 찾기
    res = 0
    if userA and userB: # 둘 다 소속이 되어 있음
        for i in userA:
            for j in userB:
                now = 배터리[i][3] + 배터리[j][3]
                if i == j:
                    now = now // 2
                if res < now:
                    res = now
    elif userA: # A만 존재
        for i in userA:
            now = 배터리[i][3]
            if res < now:
                res = now
    elif userB:
        for i in userB:
            now = 배터리[i][3]
            if res < now:
                res = now
    return res

def 소속확인(x1,y1,x2,y2): # 두 유저의 현재 위치 가져와서 진행
    # 유저 A,B 소속 확인
    userA = []
    userB = [] # 속하는 배터리 넣기 위해
    for i in range(A): # 배터리 개수만큼 돌면서
        tx,ty,c,power = 배터리[i] # 현재 배터리의 위치, 충전 범위, 충전량
        diffA = abs(x1-tx) + abs(y1-ty)
        if diffA <= c:
            userA.append(i) # 속하는 충전 배터리 넘버
        diffB = abs(x2-tx) + abs(y2-ty)
        if diffB <= c:
            userB.append(i)
    res = 최대충전량(userA,userB)
    return res


T = int(input())
for t in range(1,T+1):
    M,A = map(int, input().split()) # 총 이동 시간, 배터리 개수
    userA = list(map(int, input().split())) # A 이동 방향
    userB = list(map(int, input().split())) # B 이동 방향
    배터리 = []
    for _ in range(A):
        x,y,c,power = map(int, input().split()) # 각 배터리의 위치, 충전 범위, 충전량
        배터리.append((x,y,c,power))

    x1,y1 = 1,1
    x2,y2 = 10,10
    now = 소속확인(x1,y1,x2,y2)
    res = 0
    res += now
    for i in range(M):
        dir = userA[i]
        y1 += dx[dir]
        x1 += dy[dir]
        dir = userB[i]
        y2 += dx[dir]
        x2 += dy[dir]

        now = 소속확인(x1,y1,x2,y2)
        res += now
    # 좌표 반대로 생각했어야 함 !!!
    print(f"#{t} {res}")