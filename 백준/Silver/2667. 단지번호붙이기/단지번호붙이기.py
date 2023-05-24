import sys
from collections import deque


# 상하좌우 연결요소 구하기 문제

n = int(input())
g = [list(map(int, input())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 #시작 지점 방문 처리
    cnt = 1

    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n: #경계선 안
                if g[nx][ny] == 1:
                    g[nx][ny] = 0 #방문 처리
                    cnt += 1
                    dq.append((nx,ny))
    return cnt

res = []
total_cnt = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1: #집
            total_cnt += 1
            res.append(BFS(i,j))

res.sort()
print(total_cnt)
for x in res:
    print(x)
