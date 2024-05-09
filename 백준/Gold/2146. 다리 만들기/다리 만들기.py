import sys
from collections import deque

# 여러 섬으로 이루어진 나라.
# 섬을 잇는 다리 만들겠다.
# 다리 하나만 만들고 가장 짧게.
# 다리 딱 하나만. -> 최단거리로 -> 다익스트라

# 1. 현재 좌표 기준 상하좌우 탐색. 근데 이동하는 좌표가 본인 섬 -> continue
# 2. 해당 섬 도착. 갱신

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def BFS(startX,startY, num): # 섬 번호 부여
    global visited
    dq = deque()
    dq.append((startX,startY))
    visited[startX][startY] = True
    g[startX][startY] = num
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny) and not visited[nx][ny]:
                if g[nx][ny] == 1:
                    visited[nx][ny] = True
                    g[nx][ny] = num
                    dq.append((nx,ny))
island_num = 1
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and g[i][j] == 1:
            BFS(i,j,island_num)
            island_num += 1

# 각 섬 별로 분류 완료
INF = int(1e9)
def 최단거리(startX,startY,num):
    global res
    dq = deque()
    dq.append((startX,startY,0)) # 현재 시작위치, 경로
    dis[startX][startY] = 0
    while dq:
        x,y,cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny):
                continue
            if g[nx][ny] == num: # 같은 섬
                continue
            if g[nx][ny] == 0:
                if cnt + 1 < dis[nx][ny]:
                    dis[nx][ny] = cnt + 1
                    dq.append((nx,ny,cnt + 1))
            elif g[nx][ny] > 0: # 다른 섬
                if cnt + 1 < dis[nx][ny]:
                    dis[nx][ny] = cnt + 1
                    res = min(res,cnt + 1)
res = INF
dis = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] > 0:
            최단거리(i,j,g[i][j])
print(res-1)