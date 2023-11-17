import sys

from collections import deque

n = int(input())
g = [list(map(int, input())) for _ in range(n)]

res = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    cnt = 1
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 # 방문처리

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and g[nx][ny] == 1: # 좌표 내부이면서 방문 전
                g[nx][ny] = 0 # 방문처리
                cnt += 1
                dq.append((nx,ny))
    return cnt

cnt = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1: # 아직 방문 전
            cnt += 1 # 연결 요소 개수 추가
            r = bfs(i,j)
            res.append(r)
res.sort()

print(cnt)
for c in res:
    print(c)
