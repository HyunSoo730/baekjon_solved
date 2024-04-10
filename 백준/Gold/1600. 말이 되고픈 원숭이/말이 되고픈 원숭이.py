import sys
from collections import deque


# 말 : 이동방향 8가지, 말로 움직이면 장애물 뛰어넘을 수 있다.
# 원숭이는 k번만 말처럼 이동 가능 그 외는 4방 탐색.
# (0,0) -> (h-1,w-1)  최소횟수로 이동 -> 최단거리 : 다익스트라
# 보드의 각 칸, 0은 이동가능 1은 장애물(벽)

k = int(input())  # 말처럼 이동가능 횟수
m,n = map(int, input().split())  # 보드 크기
g = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dis = [[[INF] * (k + 1) for _ in range(m)] for _ in range(n)]  # 최단거리 기록
# k+1로 한 것은 k번까지 가능하기 때문

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1] # 말처럼 이동
def isInner(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

startX,startY = 0,0
endX,endY = n-1,m-1 # 도착점

def BFS(a, b):
    global res
    dq = deque()
    dq.append((a, b, 0, 0))  # 시작좌표, 현재 경로의 거리, 말처럼 이동한 횟수 기억

    while dq:
        x, y, t, cnt = dq.popleft()  # 현재 위치, 현재 경로의 길이, 말처럼 이동한 횟수
        if (x,y) == (endX, endY): # 도착점 도달
            res = min(res, t) # 최단거리 갱신
            continue # 도착점 도달하고는 더이상 하면 안됨.
        # 현재 위치에서 기본 이동, 말처럼이동 다 따져보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx, ny):  # 내부 좌표 아니면 안돼
                continue
            if g[nx][ny] == 0:  # 이동가능
                if t + 1 < dis[nx][ny][cnt]:  # 현재 말로 이동한 횟수에서의 최단거리보다 작다면
                    dis[nx][ny][cnt] = t + 1
                    dq.append((nx, ny, t + 1, cnt))
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            if not isInner(nx,ny):
                continue # 내부 좌표 아니면 다시
            if g[nx][ny] == 0: # 말처럼 뛰었을 때 이동가능. 근데 횟수가 남아있는지 확인
                if cnt < k: # 말처럼 이동 가능
                    if t + 1 < dis[nx][ny][cnt + 1]: # 말처럼 이동 + 1의 보드에서 최단거리 갱신 가능
                        dis[nx][ny][cnt + 1] = t + 1
                        dq.append((nx,ny,t + 1 , cnt + 1))


res = int(1e9)
BFS(startX, startY)
if res == INF:
    print(-1)
else:
    print(res)