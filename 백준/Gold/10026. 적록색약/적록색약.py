import sys
from collections import deque

n = int(input())
g = [list(input()) for _ in range(n)]

cnt = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def BFS(a,b, color):
    ch[a][b] = 1
    dq = deque()
    dq.append((a,b))

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if ch[nx][ny] == 0 and color == g[nx][ny]: #방문 전, 같은 컬러
                    ch[nx][ny] = 1
                    dq.append((nx,ny))


cntA = 0
ch = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] == "R" and ch[i][j] == 0: #아직 방문 전
            BFS(i,j, "R")
            cntA += 1
        elif g[i][j] == "G" and ch[i][j] == 0:
            BFS(i,j,"G")
            cntA += 1
        elif g[i][j] == "B" and ch[i][j] == 0:
            BFS(i,j,"B")
            cntA += 1

# 이제 적록색맹
for i in range(n):
    for j in range(n):
        if g[i][j] == "R":
            g[i][j] = "G"


ch = [[0] * n for _ in range(n)]
cntB = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == "G" and ch[i][j] == 0:
            BFS(i,j,"G")
            cntB += 1
        elif g[i][j] == "B" and ch[i][j] == 0:
            BFS(i,j,"B")
            cntB += 1
print(cntA, cntB)