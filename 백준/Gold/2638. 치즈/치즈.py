import sys
from collections import deque


n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
# 치즈 1, 빈칸 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isInner(x,y):
    return 0<=x<n and 0<=y<m

def isMelt(x,y): # 현재 위치의 치즈 녹일 수 있는가 ?
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isInner(nx,ny) and g[nx][ny] == 0:
            cnt += 1
    return cnt >= 2 # 2면 이상이면 녹이기 가능

def bfs(startX,startY):
    dq = deque()
    dq.append((startX,startY))
    visited = [[False] * m for _ in range(n)]
    visited[startX][startY] = True
    cheeze = deque()
    contact = [[0] * m for _ in range(n)]  # 접촉 횟수 용

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny) and not visited[nx][ny]:
                if g[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx,ny))
                elif g[nx][ny] == 1:
                    contact[nx][ny] += 1 # 접촉횟수 증가시킴

    # 2면 이상 접촉 치즈 녹이기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if contact[i][j] >=2:
                g[i][j] = 0
                cnt += 1
    return cnt
time = 0
while True:
    cnt = bfs(0,0) # 한바퀴 돌고...
    if cnt == 0:
        break
    time += 1
print(time)