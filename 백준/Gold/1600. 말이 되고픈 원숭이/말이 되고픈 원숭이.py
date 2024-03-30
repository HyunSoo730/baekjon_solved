import sys
from collections import deque


k = int(input())  # k번 말처럼 점프 가능
w, h = map(int, input().split())  # 가로, 세로
g = [list(map(int, input().split())) for _ in range(h)]
endX, endY = h - 1, w - 1
INF = int(1e9)
# 기본 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 말처럼 이동
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]


def isInner(x, y):
    if 0 <= x < h and 0 <= y < w:
        return True
    return False


dis = [[[INF] * w for _ in range(h)] for _ in range(k + 1)]  # 뛴 횟수를 표현하려면 3차원 배열 필요.
# 그런데 아예 안 뛴경우가 0 k번까지 가능하다고 했으니 k 즉 k+1개만큼으로 표시할 수 있다.

res = int(1e9)


def BFS(a, b):
    global res
    dq = deque()
    dq.append((a, b, 0, 0))  # 현재 좌표, 현재 경로의 길이, 현재 말처럼 뛴 횟수

    while dq:
        x, y, d, cnt = dq.popleft()  # 현재 좌표, 현재까지의 이동거리 확인
        if x == endX and y == endY:
            if d < res:
                # print(f"현재 좌표 : {x,y} 말처럼 뛰기 횟수: {cnt} 값 : {d}")
                res = d
                continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx, ny) and g[nx][ny] == 0:  # 이동 가능
                if d + 1 < dis[cnt][nx][ny]:
                    dis[cnt][nx][ny] = d + 1
                    dq.append((nx, ny, d + 1, cnt))
        for i in range(8):  # 말처럼 이동
            nx = x + hx[i]
            ny = y + hy[i]
            if isInner(nx, ny) and g[nx][ny] == 0:  # 이동 가능
                if cnt < k:
                    if d + 1 < dis[cnt + 1][nx][ny]:
                        dis[cnt + 1][nx][ny] = d + 1
                        dq.append((nx, ny, d + 1, cnt + 1))


BFS(0, 0)

if res == INF:
    print(-1)
else:
    print(res)