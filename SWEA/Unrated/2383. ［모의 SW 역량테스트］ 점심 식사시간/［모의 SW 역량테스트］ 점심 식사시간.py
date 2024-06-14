import heapq
from collections import deque


# nxn 보드, 보드에는 사람, 계단 입구 존재
# 이동 완료 시간 : 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간
# 아래층으로 이동하는 시간 : 계단입구까지 이동 시간 + 계단 내려가는 시간
# 1. 계단 입구까지 시간 : 사람 위치 - 계단입구 위치
# 2. 계단 내려가는 시간 : 1분 대기시간 + 계단은 최대 3명만 이용. 이미 3명 이용 시 그 중 한 명 계단 완전히 내려갈 때까지 대기
# 구하고자 : 모든 사람들이 계단을 내려가 이동 완료하는 시간의 최소 시간

# 1. 각 사람별 어느 계단으로 갈 지 선택 (DFS) (계단의 입구는 반드시 2개)
# 2. 도착한 순서대로 계산 진행.

def 이동시간계산(selected):
    # 각 사람 별로 시간 계산
    timeA = [] # 계단A를 사용하는 사람들의 시간 계산
    timeB = []
    for i in range(len(selected)): # 각 사람별 시간 계산
        x,y = 사람[i] # i번째 사람의 위치
        if selected[i] == 0: # i번쨰 사람이 첫번째 계단 선택
            tx,ty,level = 계단[0] # 첫번째 계단의 위치, 해당 계단 내려가는 시간
            time = abs(x-tx) + abs(y-ty) # 계단 입구까지의 시간
            heapq.heappush(timeA, time)
        else: # i번째 사람이 두번째 계단 선택
            tx,ty,level = 계단[1] # 두번째 계단의 위치, 해당 계단 내려가는 시간
            time = abs(x-tx) + abs(y-ty)
            heapq.heappush(timeB, time)

    resA = deque()
    resB = deque()
    while timeA: # 이제 도착 순서대로 삽입
        time = heapq.heappop(timeA)
        if len(resA) < 3:
            resA.append(time)
        else: # 비교
            first = resA.popleft()
            if first + 계단[0][2] < time: # 이후에 도착하면 그냥 삽입
                resA.append(time)
            else:
                resA.append(first + 계단[0][2])

    while timeB:
        time = heapq.heappop(timeB)
        if len(resB) < 3:
            resB.append(time)
        else:
            first = resB.popleft()
            if first + 계단[1][2] < time:
                resB.append(time)
            else:
                resB.append(first + 계단[1][2])

    res = 0
    if resA:
        res = max(res, resA[-1] + 계단[0][2] + 1)  #  1분은 대기시간
    if resB:
        res = max(res, resB[-1] + 계단[1][2] + 1)
    return res


def DFS(L):
    global min_time
    if L == len(사람): # 모든 사람 선택 완료
        # 모든 사람이 어떤 계단으로 갈 지 선택했으니 이제 각 계단 별로 확인 진행
        time = 이동시간계산(selected)
        min_time = min(min_time, time)
    else: # 각 사람 이제 계단 선택해야 함.
        selected[L] = 0 # L번째 사람 첫번째 계단으로 가겠다.
        DFS(L+1)
        selected[L] = 1 # L번째 사람 두번째 계단으로 가겠다.
        DFS(L+1)


T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    계단 = []
    사람 = []
    for i in range(n):
        for j in range(n):
            if g[i][j] >= 2: # 계단
                계단.append((i,j,g[i][j])) # 계단 위치 추가
            elif g[i][j] == 1: # 사람
                사람.append((i,j)) # 사람 위치 추가
    # step1. 각 사람 어느 계단 선택할 지 선택.
    selected = [0] * len(사람)
    min_time = int(1e9)
    DFS(0)

    print(f"#{t} {min_time}")