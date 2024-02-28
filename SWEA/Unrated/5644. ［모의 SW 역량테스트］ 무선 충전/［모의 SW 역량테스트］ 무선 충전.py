from collections import deque, defaultdict


stay,up, right, down, left = 0,1,2,3,4
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]


T = int(input()) # ! 테스트 케이스

def isAccess(user):
    global access
    access = [False] * A
    for i in range(A):
        dis = abs(user[0] - battery[i][0]) + abs(user[1] - battery[i][1])
        if dis <= battery[i][2]: # ! 충전량 이하라면
            access[i] = True

def calMaxPerformance():
    # 현재 userA, userB 좌표 기준 최대값 찾기
    nowA, nowB = 0,0
    maxA, maxB = 0,0
    indexA, indexB = -1,-1
    res = 0
    for i in range(A):
        if accessA[i]:
            nowA = battery[i][3]
            if maxA < nowA:
                indexA = i
                maxA = nowA
            if i != indexB:
                res = max(res, nowA + maxB)
            else:
                res = max(res, (nowA + maxB) // 2)
        if accessB[i]:
            nowB = battery[i][3]
            if maxB < nowB:
                maxB = nowB
                indexB = i
            if indexA != i:
                res = max(res, maxA + nowB)
            else:
                res = max(res, (maxA + nowB) // 2)
    return res



def move(user, direction):
    user[0] += dx[direction]
    user[1] += dy[direction]

def maxPerformance():
    global accessA, accessB
    isAccess(userA)
    accessA = access[:]  # 복사 : 할당할 때는 global 필요 !
    isAccess(userB)
    accessB = access[:]
    # print("가능한 경우 : ")
    # print(f"A : {accessA[:]}")
    # print(f"B : {accessB[:]}")
    res = calMaxPerformance()
    return res

for t in range(1,T+1):
    M, A = map(int ,input().split())  # ! 이동시간, 배터리 개수
    moveA = list(map(int, input().split()))
    moveB = list(map(int, input().split()))
    moveA.insert(0,0)
    moveB.insert(0,0)
    # userA, userB 의 이동 정보
    battery = []
    for _ in range(A):
        y, x, c, p = map(int, input().split())  # ! 각 배터리의 정보  좌표를 내가 생각하고 싶은 대로 변환
        battery.append((x,y,c,p))  # ! 배터리 좌표 (x,y) , 충전범위 c, 퍼포먼스 p

    battery.sort(key = lambda x : x[3], reverse = True) # ! 배터리 충전량 내림차순 정렬

    # * 이제 각 경우마다 계산 진행

    # ! 먼저 매 순간 어떤 배터리에 포함되어 있는지 확인 후 이동 진행
    accessA = [False] * A
    accessB = [False] * A
    access = [False] * A
    userA = [1,1]
    userB = [10,10]

    maxVal = 0

    # ! 0초일 때 먼저 한번 진행
    res = maxPerformance()
    maxVal += res
    # print(f"0초 : max : {res}")
    for time in range(1,M+1): # M초까지 진행
        # * 1. 이동 진행
        direction = moveA[time]  # ! 현재 시간 A가 이동할 방향
        move(userA, direction)
        direction = moveB[time]  # ! 현재 시간 b가 이동할 방향
        move(userB, direction)
        # * 2. 충전량 맥스 구하기
        res = maxPerformance()
        maxVal += res
        # print(f"time : {time}, max : {res}")
        # ! 이제 구했다면 다음 위치로 이동 진행
    print(f"#{t} {maxVal}")

    # ! 마지막 시간 한번 더 계산 진행