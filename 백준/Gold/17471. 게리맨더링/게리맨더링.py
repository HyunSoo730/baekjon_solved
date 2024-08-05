import sys
from collections import defaultdict
from collections import deque

# n개의 구역
# 1~n까지 번호
# 각 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다.
# 선거구는 적어도 구역을 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 함.
# 인접하면 같은 구역

# 두 선거구에 포함된 인구수의 차이 최소

n = int(input())
인구수 = [0] + list(map(int, input().split())) # 1번부터 n번 구역까지 인구수 1번 인덱스부터 사용
g = defaultdict(list)
for now in range(1,n+1):
    temp = list(map(int, input().split()))
    for idx in temp[1:]:
        g[now].append(idx)

# 1. 1~n번 일단 두 구역으로 나누기
sectionA = 0
sectionB = 1
selected = [0] * (n+1) # 각 구역이 선택한 지역구를 저장하기 위해
def DFS(L, cntA, cntB):
    global res
    if L == n+1: # 모두 확인 종료조건
        if cntA == 0 or cntB == 0: # 모두 선택하지 않음
            return
        # 선택 완료했으면 각 지역구 사람들 연결되어 있는지 확인
        secA = []
        secB = []
        for i in range(1,n+1):
            if selected[i] == sectionA:
                secA.append(i) # i번쨰 사람은 sectionA
            else:
                secB.append(i) #

        # 두 지역 모두 연결되어 있는지 확인
        if BFS(secA) and BFS(secB): # 가능
            # 두 인구수 차이 구하기
            sumA = 0
            sumB = 0
            for i in range(1,n+1):
                if selected[i] == sectionA:
                    sumA += 인구수[i]
                else:
                    sumB += 인구수[i]
            res = min(res, abs(sumA-sumB))

    else: # 현재 어느 구역 선택할지 정해야함
        selected[L] = sectionA
        DFS(L+1, cntA + 1, cntB)

        selected[L] = sectionB
        DFS(L+1, cntA, cntB+1)

def BFS(sec): #
    visited = [False] * (n+1)
    start = sec[0]
    visited[start] = True # 시작점 방문처리
    dq = deque()
    dq.append(start)
    check = set(sec)

    while dq:
        now = dq.popleft()
        for node in g[now]: # now와 인접한 노드들 확인
            if not visited[node] and node in check: # 같은 지역구
                visited[node] = True
                dq.append(node)
    if sum(visited) == len(sec): # 모두 포함됨
        return True
    else:
        return False

res = int(1e9)
DFS(1,0,0)

if res == int(1e9):
    print(-1)
else:
    print(res)