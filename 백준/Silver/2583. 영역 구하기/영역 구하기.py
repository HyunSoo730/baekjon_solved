import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m,n,k = map(int, input().split()) #m 가로 n 세로 k 직사각형 개수
g = [[0] * n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(m-y2,m-y1):
        for j in range(x1,x2):
            g[i][j] = 1


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
    global cnt
    g[x][y] = 1 #방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<m and 0<=ny<n:
            if g[nx][ny] == 0:
                cnt += 1
                DFS(nx,ny)
res = []
for i in range(m):
    for j in range(n):
        if g[i][j] == 0: #구역.
            cnt = 1 
            DFS(i,j)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x, end = " ")

