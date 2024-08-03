import sys

from collections import deque

# 말 움직임 8가지, 말은 장애물 뛰어넘을 수 있음
# 원숭이는 상하좌우만 가능, 또한 말처럼 총 k번만 이동 가능
# -> 상태가 있음 -> 상태가 있다는 것은 3차원..

k = int(input())
m, n = map(int, input().split())  # 가로, 세로
g = [list(map(int, input().split())) for _ in range(n)]

# 0인 빈칸, 1은 벽, 벽이 있는 곳으로 이동 불가
blank = 0
wall = 1

# (0,0) -> (n-1,m-1) 로 이동해야함 -> 최단거리

startX, startY = 0, 0
endX, endY = n - 1, m - 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
hx = [-2, -2, -1, 1, 2, 2, 1, -1]
hy = [-1, 1, 2, 2, 1, -1, -2, -2]


def isInner(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def BFS(startX, startY):
    global res
    dq = deque()
    dq.append((startX, startY, 0, 0))  # 시작점, 이동거리, 말로 움직인 횟수
    INF = int(1e9)
    # [n][m][k]
    dis = [[[INF] * (k+1) for _ in range(m)] for _ in range(n)]  # [n][m][k] 만듬
    dis[startX][startY][0] = 0  # 시작점 초기화

    while dq:
        x, y, d, cnt = dq.popleft()
        if (x,y) == (endX,endY):
            res = min(res,d)
            break
        # 먼저 원숭이 움직임
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx, ny): continue
            if g[nx][ny] == blank:  # 이동 가능
                if d + 1 < dis[nx][ny][cnt]:  # 갱신 가능
                    dis[nx][ny][cnt] = d + 1
                    dq.append((nx, ny, d + 1, cnt))
        # 말 움직임
        if cnt < k:  # 아직 말로 이동 가능
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if not isInner(nx, ny): continue
                if g[nx][ny] == blank:
                    if d + 1 < dis[nx][ny][cnt + 1]:
                        dis[nx][ny][cnt + 1] = d + 1
                        dq.append((nx,ny,d+1,cnt+1))


res = int(1e9)
BFS(startX,startY)
if res == int(1e9):
    print(-1)
else:
    print(res)