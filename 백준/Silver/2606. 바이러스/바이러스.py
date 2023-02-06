import sys

n = int(input()) #노드 수
m = int(input()) #간선 수
g = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1 # 무방향 그래프
    
ch = [0] * (n+1)
ch[1] = 1 #시작 노드 방문 표시 1번 노드부터 시작하니까
cnt = 0
def DFS(v):
    global cnt
    for i in range(1,n+1):
        if g[v][i] == 1 and ch[i] == 0: #연결되어 있고 방문 전
            cnt += 1
            ch[i] = 1
            DFS(i)

DFS(1)
print(cnt)
        
    
    
    
    