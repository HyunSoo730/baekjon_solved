import sys

from collections import deque

m,n = map(int, input().split()) #m가로 n세로
g = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dis = [[0] * m for _ in range(n)]

dq = deque()
flag = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 1: #익은 토마토.. 순서 생각 !
            dq.append((i,j))
        if g[i][j] == 0:
            flag = 1

if flag == 0:
    print(0)
    sys.exit(0)

def BFS():
    while dq:
        x,y = dq.popleft()
        g[x][y] = 1 #방문 처리. (시작점 때문에)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m: #경계선
                if g[nx][ny] == 0: #방문 전
                    g[nx][ny] = 1
                    dis[nx][ny] = dis[x][y] + 1
                    dq.append((nx,ny))


BFS()

flag = 0
res = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0: #모두 익지 못함
            print(-1)
            sys.exit(0)
        if res < dis[i][j]: 
            res = dis[i][j]
else:
    print(res)

