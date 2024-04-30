import sys
from collections import deque


# nxn 보드 0 빈칸, 1 벽(잘리지 않은 나무)
# 길이3 통나무 BBB 상하좌우, 회전을 통해 도착점으로 가야함
# 이동할 곳에 1이 없어야만 이동 가능
# 회전시에 통나무 포함되어 있는 3*3제외 1 없어야만 회전 가능
# 구하고자 : 최소의 움직임으로 이동 -> 다익스트라
n = int(input())
g = [list(map(str, input())) for _ in range(n)]

startX,startY = 0,0
endX,endY = 0,0
direction = 0 # 시작 방향 0 : 가로, 1 : 세로
end_dir = 0
def isIn(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
flag = False
for i in range(n):
    for j in range(n):
        if g[i][j] == "B": # 시작점 시작
            if isIn(i,j+1) and g[i][j+1] == "B": # 가로로 있는 상태
                startX,startY,direction = i,j+1,0
                g[i][j],g[i][j+1],g[i][j+2] = "0","0","0" # 시작점 모두 빈칸으로 만들기
            elif isIn(i+1,j) and g[i+1][j] == "B":
                startX,startY,direction =i+1,j,1
                g[i][j],g[i+1][j],g[i+2][j] = "0","0","0" # 시작점 모두 빈칸으로
            flag = True
            break
    if flag: break
flag = False
for i in range(n):
    for j in range(n):
        if g[i][j] == "E":
            if isIn(i,j+1) and g[i][j+1] == "E":
                endX,endY,end_dir = i,j+1,0
            elif isIn(i+1,j) and g[i+1][j]:
                endX,endY,end_dir =i+1,j,1
            flag = True
            break
    if flag: break
# print(f" 시작점 : {startX,startY} 도착점 : {endX,endY}")
# 시작점, 도착점 세팅끝
# (x,y)에 도착했을 때 그 상태가 어떤 상황에서 도착한지 알 수 없으므로!!
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y,dir): # 현재 중심 위치(x,y) 그리고 방향이 dir일때 존재 가능 ?
    if dir == 0: # 가로로 존재
        if not (0<=x<n and 1<=y<n-1):
            return False
        for i in (y-1,y,y+1):
            if g[x][i] == "1": # 벽 -> 이동 불가
                return False
    else: # 세로로 존재
        if not (1<=x<n-1 and 0<=y<n):
            return False
        for i in (x-1,x,x+1):
            if g[i][y] == "1":
                return False
    return True
def can_turn(x,y):
    cnt = 0
    if not (1 <= x < n - 1 and 1 <= y < n - 1): return False
    for i in (x-1,x,x+1):
        for j in (y-1,y,y+1):
            if g[i][j] == "1": return False
    return True
# def turn(x,y,dir):
#     # 중심좌표 (x,y) 기준 dir로회전 진행
#     for i in (x-1,x,x+1):
#         for j in (y-1,y,y+1):
#             g[i][j] = "0" # 일단 모두 초기화 후에
#     if dir == 0: # 가로로 진행
#         for i in (y-1,y,y+1):
#             g[x][i] = "1"
#     else:
#         for i in (x-1,x,x+1):
#             g[i][y] = "1"


def BFS(startX,startY,direction):
    global res
    dq = deque()
    dq.append((startX,startY,direction,0)) # 시작 위치, 시작 위치의 방향, 현재 경로횟수
    dis[startX][startY][direction] = 0 # 시작 위치에서의 시작방향. 값 0

    while dq:
        x,y,dir, cnt = dq.popleft() # 현재 경로의 현재 위치(중심좌표), 방향, 현재까지 이동 횟수
        # print(f"현재 확인할 경로 : 현재 중심 위치 : {(x,y)}, 현재 방향 : {dir}, 현재 경로까지의 이동 횟수 : {cnt}")
        if (x,y,dir) == (endX,endY,end_dir):
            # print("도착")
            res = min(res,cnt)
            continue
        for i in range(4): # 상하좌우 먼저 판단.
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny,dir): # 해당 좌표 이동 가능
                if cnt + 1 < dis[nx][ny][dir]: # 현재 통나무 방향(가로or세로)로 갔을 때의 최단거리보다 작은 경우
                    # print(f"{(nx,ny)} 도착 가능 거리 갱신 : {cnt+1}, 현재 방향 : {dir}")
                    dis[nx][ny][dir] = cnt + 1
                    dq.append((nx,ny,dir,cnt+1))
        # 회전
        if dir == 0: # 현재 가로로 존재 -> 세로로 회전
            if can_turn(x,y) and cnt + 1 < dis[x][y][1]: # 현재 중심좌표에서 회전 가능
                # print(f"{(x, y)} 도착 가능 거리 갱신 : {cnt + 1}, 현재 방향 : {1}")
                dis[x][y][1] = cnt + 1
                dq.append((x,y,1,cnt+1))
        else: # 현재 방향 1 -> 세로 -> 가로로 회전
            if can_turn(x,y) and cnt + 1 < dis[x][y][0]:
                # print(f"{(x,y)} 도착 가능, 거리 갱신 : {cnt+1}, 현재 방향 : {0 }")
                dis[x][y][0] = cnt + 1
                dq.append((x,y,0,cnt+1))

INF = int(1e9)
dis = [[[INF] * 2 for _ in range(n)] for _ in range(n)] # 가로,세로 상태가 2개이기에 3차원 배열로 해야한다.
res = int(1e9)
BFS(startX,startY,direction)
if res == INF:
    print(0)
else:
    print(res)