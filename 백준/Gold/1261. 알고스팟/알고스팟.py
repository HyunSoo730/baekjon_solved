from collections import deque

# 미로 nxm 미로는 빈 방 또는 벽
# 이동은 상하좌우
# 벽 부수기 최소 몇개의 벽을 부숴야 하는지 (1,1) -> (n,m)으로 이동
m,n = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]

INF = int(1e9)
dis = [[INF] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def BFS(startX,startY):
    dq = deque()
    dq.append((startX,startY,0)) # 현재 위치, 벽 부순 횟수
    while dq:
        x,y,t = dq.popleft() # 현재 위치, 부순 횟수(거리라고 생각)
        if (x,y) == (n-1,m-1): # 도착점 도착
            if t < dis[x][y]: # 갱신 가능
                dis[x][y] = t
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny): continue
            if g[nx][ny] == 0: # 빈방 그냥 이동 가능
                if t < dis[nx][ny]: # 현재까지의 횟수가 기존 횟수보다 작으면
                    dis[nx][ny] = t
                    dq.append((nx,ny,t))
            elif g[nx][ny] == 1: # 벽 -> 부숴야
                if t + 1 < dis[nx][ny]: # 현재까지 벽 부순 횟수
                    dis[nx][ny] = t + 1
                    dq.append((nx,ny,t+1))

BFS(0,0)
print(dis[n-1][m-1])