import heapq
from collections import deque
# nxn 보드, 최대한 빠른 시간 내에 내려가기
# 보드에 사람, 계단 입구 존재
# 이동 완료 시간은 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료하는 시간.
# 게단 입구까지 이동시간 + 계단 내려가는 시간

# 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우!
# -> 완탐. 전부 다 해보기. 백트랙킹

# 1 : 사람, 2이상 계단의 입구. 해당 값은 계단의 길이 의미
# 계단의 입구는 반드시 2개, 서로 위치가 겹치지 않음

def DFS(L):
    global 최종결과
    if L == len(사람): # 모두 어떤 계단갈 지 선택완료
        # 각 계단 별로 확인
        dataA = []
        dataB = []
        for idx in range(len(사람)):
            if selected[idx] == 0: # idx번째 사람은 첫번째 계단을 선택한
                diff = abs(사람[idx][0] - 계단[0][0]) + abs(사람[idx][1] - 계단[0][1]) # 계단까지 걸리는 시간
                heapq.heappush(dataA,diff)
            else:
                diff = abs(사람[idx][0] - 계단[1][0]) + abs(사람[idx][1] - 계단[1][1])  # 계단까지 걸리는 시간
                heapq.heappush(dataB, diff)
        # 각 사람별 계단에 도착한 시간을 작은 순서로 덱에 저장
        resA = deque()
        resB = deque()
        while dataA:  # 첫번째 계단.
            도착시간 = heapq.heappop(dataA)
            if len(resA) < 3: # 최대 인원 안넘으면 그냥 가능
                resA.append(도착시간)
            else: # 계단 오르는 인원이 3명이면 시간을 확인 후 진행
                data = resA.popleft()
                if data + 계단[0][2] < 도착시간: # 가장 먼저 계단을 이용한 사람의 종료시간과 새로 도착한 사람의 도착 시간 중 큰 값을 추가
                    resA.append(도착시간)
                else: # 대기시간 포함해서 넣기
                    resA.append(data + 계단[0][2]) # 종료시간은 계단의 길이를 더하면 돼
        while dataB: # 두번째 계단
            도착시간 = heapq.heappop(dataB)
            if len(resB) < 3:
                resB.append(도착시간)
            else: # 계단 오르는 인원이 3명이면 가장 먼저 계단을 이용한 사람의 종료시간과 현재 새로 온 사람의 시작 시간을 비교
                data = resB.popleft()
                if data + 계단[1][2] < 도착시간:
                    resB.append(도착시간)
                else:
                    resB.append(data + 계단[1][2]) # 이 종료시간부터 새로온 사람이 계단을 이용할 수 이씅므로
        # 두 계단 모두 확인 후에 각 계단 별로 마지막 사람의 종료시간을 계산하고, 그 중 최댓값 계산 (대기시간 1분 추가로 넣는 거 잊지말기)
        rA = rB = 0
        if len(resA) > 0:
            rA = resA.pop() + 계단[0][2] + 1 # 가장 늦게 계단 도착한 사람의 도착 시간 + 계단 길이 + 1(대기시간)
        if len(resB) > 0:
            rB = resB.pop() + 계단[1][2] + 1
        result = max(rA,rB) # 최종결과는 두 계단에서 가장 마지막에 내려온 사람의 최종 시간.
        최종결과 = min(최종결과, result)
    else:
        selected[L] = 0 # L번째 사람 첫번째 계단 선택
        DFS(L+1)
        selected[L] = 1 # L번째 사람 두번째 계단 선택
        DFS(L+1)


T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    계단 = [] # 계단 입구는 2개
    사람 = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                사람.append((i,j))
            if g[i][j] >= 2: # 계단 입구
                계단.append((i,j,g[i][j])) # 계단 좌표, 계단 길이
    # 각 계단은 동시에 최대 3명만 올라가 있을 수 있따.
    # 1. 각 사람들이 어떤 계단을 갈 지 선택
    selected = [0] * len(사람)
    최종결과 = int(1e9)
    DFS(0)
    print(f"#{t} {최종결과}")