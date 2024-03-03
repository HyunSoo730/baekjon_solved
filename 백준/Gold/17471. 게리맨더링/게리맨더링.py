from collections import deque

n = int(input())
population = list(map(int, input().split())) # ! 각 지역 인구수
population.insert(0,0) # ! 1번 인덱스부터 사용


def isConnect(data): # ! 해당 지역에 있는 구역들 모두 연결되어 있는지 -> BFS
    dq = deque()
    start = data[0] # ! 시작점
    dq.append(start)
    visited = [False] * (n+1)
    visited[start] = True # ! 시작지점 방문처리
    check = set(data)
    while dq:
        now = dq.popleft()
        for node in g[now]:
            if not visited[node] and node in check: # ! 해당 구역에 속하면서 아직 방문 안했다면
                visited[node] = True
                dq.append(node)
    if sum(visited) == len(data): # ! 모두 방문 -> 모두 연결
        return True
    else: return False


def DFS(L, cntA, cntB):
    global res
    if L == n+1: # ! 1번 인덱스부터 사용하니까 n+1도달 (1~n 모두 확인)
        if cntA == 0 or cntB == 0:
            return
        if isConnect(dataA) and isConnect(dataB):
            sumA = 0
            sumB = 0
            for idx in dataA:
                sumA += population[idx]
            for idx in dataB:
                sumB += population[idx]
            res = min(res, abs(sumA - sumB))
    else:
        dataA.append(L) # ! 현재 구역(L) A구역에 추가
        DFS(L+1, cntA+1, cntB)
        dataA.pop()

        dataB.append(L) # ! 현재 구역(L_ B구역에 추가
        DFS(L+1, cntA, cntB+1)
        dataB.pop()


g = [[] for _ in range(n+1)]
for i in range(1,n+1):
    temp = list(map(int ,input().split()))
    for x in temp[1:]:
        g[i].append(x)

dataA = []
dataB = []
res = int(1e9)
DFS(1,0,0)
if res == int(1e9):
    print(-1)
else:
    print(res)