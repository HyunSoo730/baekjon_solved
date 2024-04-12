import sys
from collections import deque


# nxn 보드 , m개의 물고기
# 아기 상어 처음 크기 2, 1초에 상하좌우 한칸, 자신보다 큰 물고기가 있는 곳은 갈 수 없고, 나머지 칸 이동 가능
# 아기상어 이동 정하기
# 더 이상 이동 못하면 끝 = 본인보다 크기가 큰 물고기들만 남은 경우
# 먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 물고기.
# 그런 물고기 여러개면 위쪽, 또 여러개면 왼쪽

# 먹을 때마다 맵을 갱신

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

size, eatCount = 0,1 # 인덱스 활용
shark = [2, 0]  # 샤크 크기, 샤크가 현재 먹은 물고기 수

startX, startY = 0, 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            startX, startY = i, j
            g[i][j] = 0
            break

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isInner(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


time = 0
def BFS():
    global time,startX,startY
    # 시작위치 갱신.

    while True:  # 먹을 수 있는 물고기가 없을 때까지 진행해야함.
        # 즉 매 순간 먹은 후에 갱신 후 계속 놀려야 함.
        dq = deque()
        dq.append((startX, startY,0)) # 현재 경로의 위치, 시간(거리)
        visited = [[False] * n for _ in range(n)]
        visited[startX][startY] = True

        # 먹을 수 있는 물고기 후보
        candidates = []
        while dq:
            x, y,t = dq.popleft()
            if 0 < g[x][y] < shark[size]: # 가능한 경우 . 후보자.
                candidates.append((x,y,t))
                continue # 후보자 추가 후 더 나가면 안됨.

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny):
                    continue
                if visited[nx][ny]:
                    continue
                if g[nx][ny] <= shark[size]: # 샤크 사이즈보다 작으면 방문은 가능
                    visited[nx][ny] = True
                    dq.append((nx,ny,t + 1)) # 방문 가능한 경우는 일단 다 넣고. 먹을 수 있는 경우에 판단

        if not candidates:
            break # 못먹는 경우 탈출

        candidates.sort(key = lambda x : (x[2], x[0], x[1])) # 거리 순으로 우선적. 그 후 x좌표 작은 거 그 후 y좌표 작은 거
        x,y,t, = candidates[0]
        time += t
        shark[eatCount] += 1
        g[x][y] = 0 # 먹은 처리 해주기

        if shark[eatCount] == shark[size]:
            shark[size] += 1
            shark[eatCount] = 0

        startX,startY = x,y # 샤크 위치 갱신

BFS()
print(time)