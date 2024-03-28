import sys
from collections import deque


n,m,k = map(int, input().split()) # ! nxm k번 벽 부수기 가능

g = [list(map(int, input())) for _ in range(n)]
INF = int(1e9)
dis = [[[INF] * m for _ in range(n)] for _ in range(k+1)] # ! k번까지 열쇠를 부술 수 있으므로

# for x in g:
#     print(x)
# ! 안쪽에서부터 채우는거야.
# ! (0,0) -> (n-1,m-1) 로 이동. 벽 부수면서 진행

dx = [-1,0,1,0]
dy = [0,1,0,-1]

startX,startY = 0,0
endX,endY = n-1,m-1
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def BFS(a,b):
    if a == endX and b == endY: # ! 시작점 도착점 동일
        dis[0][a][b] = 1
        return
    dq = deque()
    dq.append((a,b,1,0)) # ! 현재 좌표, 경로의 최단거리, 벽을 부순 횟수

    while dq:
        x,y,d,cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny) and (nx == endX and ny == endY): # ! 도착점 도달
                if d + 1 < dis[cnt][nx][ny]:
                    dis[cnt][nx][ny] = d + 1 # ! 도착점은 갱신만 진행.
            elif isInner(nx,ny) and g[nx][ny] == 0: # ! 이동 가능
                if d + 1 < dis[cnt][nx][ny]:
                    dis[cnt][nx][ny] = d+1
                    dq.append((nx,ny,d+1,cnt))
            elif isInner(nx,ny) and g[nx][ny] == 1: # 이동 불가능 -> 벽 부수기
                if cnt < k: # ! 아직 벽 부수기 가능
                    if d + 1 < dis[cnt+1][nx][ny]:
                        dis[cnt+1][nx][ny] = d + 1
                        dq.append((nx,ny,d+1,cnt+1))

BFS(startX,startY)
# ! BFS가 끝나면 벽 부순 횟수 별로 이제 최단 경로가 나오니까 그 중 최소값을 찾으면 된다.
res = INF
for i in range(k+1):
    res = min(res, dis[i][endX][endY])
if res == INF:
    print(-1)
else:
    print(res)