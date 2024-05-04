import sys
from collections import deque


# 빙산. 2차원 맵, 각 칸은 높이, 0은 바다 0보다 크면 빙산
# 빙산의 각 칸은 상하좌우 0이 저장된 칸의 개수만큼 1년마다 줄어든다.
# 한 덩어리의 빙산이 주어질때 (모두 연결되어 있다는 뜻)
# 두 덩어리 이상으로 분리되는 최초의 시간 구하기 -> 연결성 : 플러드필이 2덩이 이상이 되는 순간 구하기
# 만일 전부 녹을 때까지 두 덩어리 이상으로 분리되지 않는다면 0 출력

n,m = map(int, input().split()) # 행, 열
g = [list(map(int, input().split())) for _ in range(n)]

# 1. 현재 빙산의 덩어리 판단
# -> 2덩어리 이상으로 나눠지면 끝
# 2. 아직 한 덩어리라면, 각 칸마다 인접한 0의 개수에 따라서 값 줄이기

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def BFS(startX,startY):
    global visited
    dq = deque()
    dq.append((startX,startY))
    visited[startX][startY] = True # 시작점 방문처리

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx,ny): continue
            if not visited[nx][ny] and g[nx][ny] > 0:
                visited[nx][ny] = True
                dq.append((nx,ny))
def cal_zero_cnt(x,y,check):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isInner(nx,ny) and g[nx][ny] == 0:
            cnt += 1
    check.append((x,y,cnt))

def 녹이기():
    check = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] > 0:
                cal_zero_cnt(i,j, check)
    while check:
        x,y,cnt = check.popleft()
        if g[x][y] > cnt:
            g[x][y] -= cnt
        else:
            g[x][y] = 0

def 보드출력(g):
    print("==============")
    for i in range(n):
        for j in range(m):
            print(g[i][j], end = " ")
        print()

res = 0
while True:
    # 현재 덩어리 판단
    # print(f"{res}번째 시도 후 현재 보드")
    # 보드출력(g)
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j] > 0:
                BFS(i,j)
                cnt += 1
    if cnt == 0: # 여기로 온다면 바로 나눠지는 것 없이 끝난다는 것
        res = 0
        break
    elif cnt > 1: # 두 덩어리 이상으로 나눠진다면
        break
    else: # cnt == 1일 때는 계속 진행
        res += 1
        녹이기()
print(res)