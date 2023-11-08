import sys
from collections import deque


n,m = map(int, input().split())
g = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int ,input().split())
    g[a].append(b) # a -> b 필수
    indegree[b] += 1 # 순서 존재하기에 진출차수 증가
# 기본 세팅
res = [0] * (n+1)
def toplogy_sort():
    dq = deque()
    for v in range(1,n+1):
        if indegree[v] == 0:
            dq.append((v,1))   # 삽입할 때 순번과 함께 !
    while dq:
        now,cnt = dq.popleft()
        res[now] = cnt

        for v in g[now]:
            indegree[v] -= 1
            if indegree[v] == 0:
                dq.append((v,cnt+1)) # 해당 다음 순번으로 넣어줘야함.

    print(*res[1:])

toplogy_sort()
