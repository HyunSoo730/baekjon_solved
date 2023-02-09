import sys
from collections import deque

n,m,v = map(int, input().split()) #노드, 간선
g = [[] for _ in range(n+1)] #1번부터 사용

for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,n+1):
    g[i].sort()

ch = [0] * (n+1)
resA = []
resA.append(v)
def DFS(v):
    for x in g[v]: #인접 노드
        if ch[x] == 0: #방문 전
            ch[x] = 1
            resA.append(x)
            DFS(x)
    
ch[v] = 1 
DFS(v)    
for x in resA:
    print(x, end = " " )
    

ch = [0] * (n+1)
resB = []
resB.append(v)
ch[v] = 1
dq = deque()
dq.append(v)
def BFS(v):
    while dq:
        now = dq.popleft()
        
        for x in g[now]:
            if ch[x] == 0:
                ch[x] = 1
                resB.append(x)
                dq.append(x)

print()
BFS(v)
for x in resB:
    print(x, end = " ")
    