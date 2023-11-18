import sys
from collections import deque

m,n,k = map(int, input().split()) # 세로, 가로
g = [[0] * n for _ in range(m)]
for _ in range(k):
    a,b,c,d = map(int, input().split()) # n,m으로 주어짐; (가로, 세로)
    for i in range(b,d):
        for j in range(a,c):
            g[i][j] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0
res = []

def bfs(a,b):
    count = 1 # 시작지점 포함
    g[a][b] = 1 # 시작지점 방문 표시
    dq = deque()
    dq.append((a,b))

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y  +dy[i]
            if 0<=nx<m and 0<=ny<n and g[nx][ny] == 0: # 아직 방문 가능
                g[nx][ny] = 1
                count += 1
                dq.append((nx,ny))
    return count

for i in range(m):
    for j in range(n):
        if g[i][j] == 0:
            cnt += 1
            res.append(bfs(i,j))
print(cnt)
res.sort()
print(*res)