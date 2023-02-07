import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]   #빈 리스트로 했어야함..! 무방향 노드들만 있는 상태니까! 
ch = [0] * (n+1)
## 그래프 전체 0으로 채워야 하는 것을 상하좌우 구분 있을 경우고 그 외에는 이런 식으로 빈 리스트에 추가하는 식으로 진행하자.
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

cnt = 0
def DFS(v):
    ch[v] = 1 #방문 표시
    for x in g[v]: #인접노드들
        if ch[x] == 0:
            DFS(x)
    
for i in range(1,n+1):
    if ch[i] == 0: #방문 전
        DFS(i)
        cnt += 1

print(cnt)


        
        
        
        
        
        