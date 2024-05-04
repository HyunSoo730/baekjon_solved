import sys
from collections import deque


# nxn 보드, 각 칸은 나라, 각칸의 값은 해당 나라에 살고 있는 사람 수
# 인접한 나라 사이에는 국경선이 존재, 인구 이동이 불가능할 때까지 진행. 인구 이동 며칠동안 발생하는지
# 인구이동. 두 나라의 인구 차이 L명이상, R명이하라면 두 나라가 국경선을 공유한다.
# 국경선이 모두 열리면 인구이동 시작.
# 플러드 필 -> 해당하는 애들 각칸은 총 인구수 / 칸 수 소수점 버림.

# 1. 전체를 돌면서 국경선 열려있는지 확인. -> 따로 관리 -> 1번, 2번 이런식으로
# -> 이건 BFS 한번이면 연결성 확인 가능
# 2. 모두 돌았으면 각 연결된 애들 총 합 구해서 연합 진행
# 3. 연결된 애들이 없을 때까지 반복

n,L,R = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def can_open(x,y,nx,ny): # 두 좌표 사이에 국경선 오픈 가능한지
    diff = abs(g[x][y] - g[nx][ny])
    if L<=diff<=R: return True # 국경선 공유
    return False

def BFS(startX,startY):
    global visited
    dq = deque()
    check = deque()
    check.append((startX,startY))
    dq.append((startX,startY))
    visited[startX][startY] = True
    sum_data = g[startX][startY] # 시작점 기준

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny): continue # 외부 좌표라면 탈출
            if not visited[nx][ny] and can_open(x,y,nx,ny):
                visited[nx][ny] = True
                check.append((nx,ny))
                dq.append((nx,ny))
                sum_data += g[nx][ny]
    if len(check) > 1: # 연합결성 가능 -> 시작점 제외 포함되어 있어야함.
        temp = int(sum_data / len(check))
        for x,y in check:
            g[x][y] = temp
        return True
    return False

res = 0
while True:
    cnt = 0 # 인구 이동 횟수
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if BFS(i,j):
                    flag = True # 인구 이동 가능
    if not flag:
        break
    res += 1
print(res)