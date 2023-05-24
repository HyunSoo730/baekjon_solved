import sys


n = int(input()) # <= 100
m = int(input()) #간선

g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ch = [0] * (n+1)
cnt = 0
def DFS(v):
    global cnt
    ch[v] = 1

    for node in g[v]:
        if ch[node] == 0:
            ch[node] = 1
            cnt += 1
            DFS(node)

DFS(1)
print(cnt)
