import sys
input = sys.stdin.readline
from collections import deque

#상하좌우 위아래 6방향
# 최소 일수

m,n,h = map(int, input().split()) #가로, 세로, 높이
#r가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토의 정보.
#3차원 리스트?
g = []
for _ in range(h):
    data = [list(map(int, input().split())) for _ in range(n)]
    g.append(data)
    #2차원 리스트 h개 쌓이게끔
flag = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 0:
                flag = 1
if flag == 0:
    print(0)
    sys.exit(0)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1] #총 6방향

#1은 익은 토마토
dq = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 1: #익은 토마토
                dq.append((i,j,k))


dis = []
for _ in range(h):
    data = [[0] * m for _ in range(n)]
    dis.append(data)
    
def BFS():

    while dq:
        z,x,y = dq.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h: #경계선
                if g[nz][nx][ny] == 0: #아직 방문 안함
                    g[nz][nx][ny] = 1 #방문처리
                    dis[nz][nx][ny] = dis[z][x][y] + 1
                    dq.append((nz,nx,ny))

BFS()
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 0: #모두 익지 못함
                print(-1)
                sys.exit(0)
            if dis[i][j][k] > res:
                res = dis[i][j][k]
    
print(res)







