from collections import deque


# 출발지(S) 도착지(G)까지 가기 위한 빠른 시간.
# 출발지에서 도착지까지 가는 경로 중 복구 기간이 가장 짧은 경로에 대한 총 복구 시간 구하기
# 최단거리.

# 조건
# 깊이1 -> 복구에 드는 시간 1
# 시작점(0,0) 도착점(n-1, n-1), 각 칸마다 파여진 도로의 깊이. 현재 위치한 칸의 도로를 복구해야만 다른 곳으로 이동 가능

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def BFS(a,b):
    global dis
    dq = deque()
    dq.append((a,b,0)) # 현재 경로의 좌표, 시간을 함께 기록

    while dq:
        x,y,t = dq.popleft() # 현재 좌표, 현재 경로의 걸린 시간
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny): # 이동 가능
                if t + g[nx][ny] < dis[nx][ny]:
                    if nx == endX and ny == endY:
                        dis[nx][ny] = t + g[nx][ny]
                    else:
                        dis[nx][ny] = t + g[nx][ny]
                        dq.append((nx,ny,t + g[nx][ny]))




T = int(input())
for t in range(1,T+1):
    n = int(input()) # 보드 크기
    g = [list(map(int, input())) for _ in range(n)]

    startX,startY = 0,0
    endX,endY = n-1,n-1
    INF = int(1e9)
    dis = [[INF] * n for _ in range(n)]
    dis[startX][startY] = 0 # 시작점 초기화
    BFS(startX,startY)
    print(f"#{t} {dis[endX][endY]}")