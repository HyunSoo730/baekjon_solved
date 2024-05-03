import sys
from collections import deque


# nxm 보드(맵), 0 : 빈칸(이동가능) 1 : 벽(이동불가)
# (1,1) -> (n,m) 이동. 최단 경로로 이동하기 -> 다익스트라.
# 시작하는 칸, 끝나는 칸 포함해서 센다.
# 이동하는 도중 한개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개까지 부수고 이동.
# 벽을 부순횟수 1과 부순횟수0은 다른 상태 -> 상태관리가 필요.

n,m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]
INF = int(1e9)
# dis[x][y][z]에서 (x,y)까지 도달하는 데 필요한 최단거리를 구하는데 z는 벽을 부순 횟수를 나타냄.
# z = 0 벽 안 부숨, z = 1 벽 부숨.
# 따라서 다른 상태. 각각의 상태에서 최단거리 계산해야 한다.
dis = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
startX,startY = 0,0
endX,endY = n-1,m-1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def BFS(startX,startY):
    global res
    dq = deque()
    dq.append((startX,startY,0,1)) # 시작 위치(x,y), 벽을 부순 횟수, 현재까지의 경로를 저장 (시작위치도 포함)

    while dq:
        x,y,cnt,distance = dq.popleft() # 현재 경로의 위치, 벽을 부순 횟수(부쉈는지 안 부쉈는지), 현재 경로의 길이
        if (x,y) == (endX,endY): # 도달
            res = min(res, distance)
            continue # 도착점 도달 시 더 할 필요 없음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny): continue
            if g[nx][ny] == 0: # 빈칸 -> 이동 가능
                if distance + 1 < dis[nx][ny][cnt]: # 현재 경로보다 작은 경우에만 갱신
                    dis[nx][ny][cnt] = distance + 1
                    dq.append((nx,ny,cnt,distance + 1))
            else: # 벽 -> 벽을 부술 수 있는지
                if cnt == 0 and distance + 1 < dis[nx][ny][1]:
                    dis[nx][ny][1] = distance + 1 # 벽을 부숴서 거리 갱신
                    dq.append((nx,ny,1,distance + 1)) # 벽 부순 것으로 갱신 후 현재 경로 진행.

res = INF
BFS(startX,startY)
if res == INF:
    print(-1)
else:
    print(res)