import sys

from collections import deque

n,m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]
dis = [[0] * m for _ in range(n)] # 최단거리를 기록할 리스트
dis[0][0] = 1 # 시작지점부터 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]  # 방향 벡터 설정

def bfs(a,b): # 시작 위치 a,b
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 # 시작노드 방문 처리. 0,1로 나타내기에 g 내에서 그냥 방문처리 가능

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 1: # 좌표 내부이면서, 아직 방문 전
                g[nx][ny] = 0 #방문 처리 후
                dis[nx][ny] = dis[x][y] + 1 # 거리 갱신
                dq.append((nx,ny))

bfs(0,0)
print(dis[n-1][m-1])


