from collections import deque


def step1(): # ! 계단 입구까지 이동거리 계산
    global dis, data
    dis = [0] * len(person)
    data = []
    for i in range(len(person)):
        idx = select[i] # ! i번째 사람이 선택한 계단의 인덱스
        px,py = person[i][0], person[i][1] # ! 사람의 위치
        sx,sy, length = stairs[idx]
        distance = abs(px-sx) + abs(py-sy)
        dis[i] = distance
        data.append((idx, distance, length)) # ! 어떤 계단을 이용하는지, 해당 계단까지 거리, 해당 계단 길이


def step2():
    global minDis
    time = 0  # 현재 시간
    finish_count = 0  # 계단을 내려간 사람 수
    on_stairs = [deque() for _ in range(2)]  # 각 계단을 내려가고 있는 사람들
    waiting = [[] for _ in range(2)]  # 각 계단에 대기 중인 사람들

    while finish_count < len(person):
        # 계단을 내려가고 있는 사람 처리
        for i in range(2):
            if on_stairs[i]:
                updated = deque()
                for p_time in on_stairs[i]:
                    if time - p_time < stairs[i][2]:  # 아직 내려가는 중인 경우
                        updated.append(p_time)
                    else:
                        finish_count += 1  # 계단을 내려갔으므로 카운트 증가
                on_stairs[i] = updated

        # 대기 중인 사람 계단으로 이동
        for i in range(2):
            while waiting[i] and len(on_stairs[i]) < 3:  # 계단에 여유가 있고, 대기자가 있는 경우
                p_idx = waiting[i].pop(0)
                if dis[p_idx] <= time:  # 계단에 도착한 경우
                    on_stairs[i].append(time)  # 계단 내려가기 시작 시간 기록

        # 각 사람별로 대기열에 추가
        for i, (idx, distance, length) in enumerate(data):
            if distance == time:  # 계단에 도착한 경우
                waiting[idx].append(i)  # 해당 계단의 대기열에 추가

        time += 1  # 시간 증가

    minDis = min(minDis, time)  # 모든 사람이 내려간 시간 중 최소값 업데이트


def DFS(L):
    global minDis
    if L == len(person): # ! 모두 확인
        # ! 모든 사람이 계단을 선택했으니 이제 각 계단별 이동거리 진행
        # print("select : ", end = " ")
        step1()
        step2()

    else:
        select[L] = 0
        DFS(L+1)
        select[L] = 1
        DFS(L+1)

T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    person = []
    stairs = [] # ! 계단은 무조건 2개
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1: # ! 사람인 경우
                person.append((i,j))
            elif g[i][j] > 1: # ! 계단인 경우
                stairs.append((i,j,g[i][j]))
    select = [0] * len(person) # ! 각 사람별 선택한 계단의 인덱스
    dis = [0] * len(person) # ! 각 사람별 이동 시간 저장할 리스트
    data = []
    minDis = int(1e9)
    DFS(0)
    print(f"#{t} {minDis-1}")