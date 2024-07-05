import sys
from collections import deque

# 가장자리에는 치즈가 놓여있지 않으며, 치즈에는 하나 이상의 구멍이 있을 수 있다.
# 가장 자리 따라가면서 녹아야 함.
# 좌표 확장 개념 도입

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
# -> 중요한 것은 반대로 생각할 수 있어야 함. 공기에서 탐색을 시작한다는 생각!
startX,startY = 0,0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    return 0<=x<n and 0<=y<m

def BFS(startX,startY):
    dq = deque()
    dq.append((startX,startY))
    melt = deque()
    visited = [[False] * m for _ in range(n)]
    visited[startX][startY] = True
    cnt = 0 # 녹인 치즈
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y +dy [i]
            if not isInner(nx,ny): continue
            if not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = True
                dq.append((nx,ny))
            elif not visited[nx][ny] and g[nx][ny] == 1:
                visited[nx][ny] = True
                melt.append((nx,ny))

    while melt:
        x,y = melt.popleft()
        g[x][y] = 0
        cnt += 1
    return cnt

time = 0
prev_cnt = 0
while True:
    cnt = BFS(0, 0)
    if cnt == 0:
        break
    prev_cnt = cnt
    time += 1

print(time)
print(prev_cnt)