import sys

from collections import deque

n = int(input())
v,w = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ch = [0] * (n+1)
res = -1
def DFS(v, cnt):
    global res
    if v == w:
        res = cnt
    ch[v] = 1
    for node in g[v]:
        if ch[node] == 0:
            DFS(node, cnt + 1)

DFS(v,0)
if res == -1:
    print(-1)
else:
    print(res)