import sys
from collections import deque


T = int(input())


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 #시작 지점 방문 처리

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny] == 1: #방문 전
                    g[nx][ny] = 0
                    dq.append((nx,ny))



for _ in range(T):
    m,n,k = map(int, input().split()) #가로, 세로, 위치 개수
    g = [[0] * m for _ in range(n)]

    for _ in range(k):
        a,b = map(int, input().split())
        g[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1: #배추.
                BFS(i,j)
                cnt += 1

    print(cnt)
