import sys
# sys.stdin = open("input.text", "rt")
from collections import deque

n,m = map(int, input().split())
#최단거리
g = [list(map(int, input())) for _ in range(n)]

#1로만 이동
dis = [[0] * m for _ in range(n)]
dis[0][0] = 1 #시작위치는 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 #방문처리

    while dq:
        x,y = dq.popleft()
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny] == 1: #방문 전
                    g[nx][ny] = 0 #방문처리
                    dis[nx][ny] = dis[x][y] + 1
                    dq.append((nx,ny))

    
BFS(0,0)


print(dis[n-1][m-1])