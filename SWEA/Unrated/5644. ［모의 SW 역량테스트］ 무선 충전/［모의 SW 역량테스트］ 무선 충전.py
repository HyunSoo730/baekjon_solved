

dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

def step1(): # ! 각 유저별 속해있는 배터리 찾기
    global userA, userB
    global checkA, checkB
    checkA = [False] * A
    checkB = [False] * A
    for i in range(A):
        x,y,c,p = battery[i]
        disA = abs(userA[0] - x) + abs(userA[1] - y)
        disB = abs(userB[0] - x) + abs(userB[1] - y)
        if disA <= c: # ! 해당 배터리에 속한다면
            checkA[i] = True
        if disB <= c:
            checkB[i] = True
    # ! 각 유저별 이용 가능한 배터리 계산 (이미 내림차순 정렬)

def step2(): # ! 현재 시간에 A,B 배터리 이용 최대 효율 찾기
    global userA, userB
    global checkA, checkB
    nowA, nowB = 0, 0  # ! 현재 A유저, B유저의 성능
    maxA, maxB = 0, 0  # ! 둘의 최고 성능 배터리 값
    indexA, indexB = -1, -1  # ! 현재 A유저, B유저의 이용하는 배터리 인덱스
    res = 0  # ! 최고 합
    for i in range(A):
        nowA = battery[i][3]  # ! 현재 배터리 성능
        nowB = battery[i][3]
        if checkA[i]:  # ! A유저는 i번째 배터리 이용 가능
            if maxA < nowA:
                maxA = nowA
                indexA = i  # ! 현재 인덱스가 최고 배터리로 갱신
            if i == indexB:
                res = max(res, (nowA + maxB) // 2)
            else:
                res = max(res, nowA + maxB)
        if checkB[i]:
            if maxB < nowB:
                maxB = nowB
                indexB = i
            if i == indexA: # ! 현재 인덱스 비교 !!
                res = max(res, (maxA + nowB) // 2)
            else:
                res = max(res, maxA + nowB)
    return res



def simulate():
    global checkA, checkB
    global res

    checkA = [False] * A
    checkB = [False] * A
    step1()
    res += step2()
    for time in range(M): # ! 0~M분까지 징행
        directionA = moveA[time]
        userA[0] += dx[directionA]
        userA[1] += dy[directionA]

        directionB = moveB[time]
        userB[0] += dx[directionB]
        userB[1] += dy[directionB]

        checkA = [False] * A
        checkB = [False] * A
        step1()
        now = step2()
        res += now


T = int(input())
for t in range(1,T+1):
    M,A = map(int, input().split()) # ! 이동시간, 배터리 개수
    moveA = list(map(int, input().split())) # ! 유저A의 움직임
    moveB = list(map(int, input().split())) # ! 유저B의 움직임
    battery = []
    for i in range(A): # ! 배터리 정보
        y,x,c,p = map(int, input().split())
        battery.append((x,y,c,p)) # ! 배터리 정보 저장
    battery.sort(key = lambda x : -x[3]) # ! 배터리 성능 순 내림차순
    userA = [1,1]
    userB = [10,10]
    checkA = [False] * A
    checkB = [False] * A
    res = 0
    simulate()
    print(f"#{t} {res}")