import sys
from collections import deque

n,m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

res = int(1e9) # 최소 비용
def bfs(v): # 현재 노드와 현재 레벨
    res = 0 # 최종 케빈 베이컨의 수 저장을 위한 변수
    visited[v] = 1 # 현재 노드 방문 처리
    dq = deque()
    dq.append((v,0)) # (현재노드, 레벨) 이렇게 넣어줄꺼야.

    while dq:
        now, level = dq.popleft()
        for node in g[now]: # 현재 노드의 인접노드들 확인
            if visited[node] == 0:# 아직 방문 전이라면
                visited[node] = 1 # 방문처리 후
                res += level
                dq.append((node, level+1)) # 레벨 차수 증가시키고 삽입 진행
    return res
max_res = int(1e9)
idx = -1
for i in range(1,n+1):
    visited = [0] * (n+1)
    r = bfs(i)
    if r < max_res:
        idx = i
        max_res = r
print(idx)
