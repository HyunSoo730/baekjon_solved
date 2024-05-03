import sys
from collections import deque, defaultdict


n,m = map(int, input().split())
g = defaultdict(list)
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split()) # a->b
    g[a].append(b)
    indegree[b] += 1
# print(indegree)

dq = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        dq.append(i)
# print(dq)
res = []
while dq:
    now = dq.popleft()
    res.append(now)
    for node in g[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            dq.append(node)
print(*res)