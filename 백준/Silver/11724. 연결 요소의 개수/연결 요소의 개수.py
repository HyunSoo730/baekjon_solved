import sys

from collections import deque

n,m = map(int, input().split())
g = [[] for _ in range(n+1)] # 1번 인덱스부터 사용

for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ch = [0] * (n+1)
def dfs(v):
    ch[v] = 1  #방문처리

    for node in g[v]: # 현재 노드의 인접 노드들
        if ch[node] == 0: #방문 전
            ch[node] = 1 # 방문처리 후 들어감
            dfs(node)
cnt = 0
for i in range(1,n+1):
    if ch[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)