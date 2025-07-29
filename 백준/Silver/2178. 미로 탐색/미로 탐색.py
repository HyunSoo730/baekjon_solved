import sys
from collections import deque

# nxm 크기의 배열
# 1은 이동 가능, 0은 이동 불가.
# (1,1) -> (n,m)으로의 최소 칸 수 : 최단거리 -> BFS
# 조건
# 1. 인접 칸만 이동 가능

n,m = map(int, input().split())
g = [list(map(str, input())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dq = deque()

dis = [[0] * m for _ in range(n)]
dis[0][0] = 1 # 초기화

def isInner(x,y):
    return 0<=x<n and 0<=y<m

def bfs(a,b):
    dq.append((0,0)) # 시작점 설정

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny) and g[nx][ny] == "1": # 이동 가능
                g[nx][ny] = "0" # 방문 처리
                dq.append((nx,ny))
                dis[nx][ny] = dis[x][y] + 1
    return dis[n-1][m-1]

print(bfs(n,m))


