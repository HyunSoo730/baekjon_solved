import sys
from collections import deque

# 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어짐
# 공기의 관점에서 생각의 전환 !!
# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간,
# 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수


n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 0은 공기, 1은 치즈
air = 0
cheeze = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def BFS(startX,startY):
    dq = deque()
    dq.append((startX,startY))
    visited = [[False] * m for _ in range(n)]
    visited[startX][startY] = True
    cnt = 0 # 치즈 개수
    melt = deque()
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny): continue
            if visited[nx][ny]: continue
            if g[nx][ny] == air:
                visited[nx][ny] = True
                dq.append((nx,ny))
            elif g[nx][ny] == cheeze:
                visited[nx][ny] = True
                melt.append((nx,ny))
                cnt += 1

    while melt:
        x,y = melt.popleft()
        g[x][y] = air # 공기화
    return cnt




last_cnt = 0
time = 0
while True:

    cnt = BFS(0,0)
    if cnt == 0: # 끝
         break
    time += 1
    last_cnt = cnt

print(time)
print(last_cnt)