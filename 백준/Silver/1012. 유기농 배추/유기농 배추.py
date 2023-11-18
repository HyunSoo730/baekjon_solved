import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    g[a][b] = 0 # 시작지점 방문처리
    dq = deque()
    dq.append((a,b))

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 1: # 좌표 내부이면서 방문 전
                g[nx][ny] = 0 # 방문처리
                dq.append((nx,ny))

T = int(input())
for _ in range(T):
    m,n,k = map(int, input().split())
    g = [[0] * m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, input().split())
        g[b][a] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                cnt += 1
                bfs(i,j)
    print(cnt)
