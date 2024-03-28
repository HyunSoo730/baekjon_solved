import sys
from collections import deque


n,m = map(int, input().split()) # ! 보드 칸
g = [list(map(str,input())) for _ in range(n)]

nowX,nowY = 0,0
endX,endY = 0,0
water = deque()
blank = "." # 이동 가능
wall = "X"  # 돌
w = "*"
des = "D"
for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            nowX,nowY = i,j
        if g[i][j] == "D":
            endX,endY = i,j
        if g[i][j] == "*": # 물
            water.append((i,j)) # 물 위치 저장

INF = int(1e9)
time = INF # ! 최단 시간 저장.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

dis = [[INF] * m for _ in range(n)]

def BFS(a,b): # ! 시작 지점.
    dq = deque()
    dq.append((a,b,0)) # 현재 위치, 현재 경로에서의 최단 시간 저장

    while len(dq) != 0 or len(water) != 0: # 여기서 조건을 or로 줘야만 했다. 이유는 둘 중 하나라도 된다면 계속 반복 돌아야해!!!!!
        # step1 : 물 먼저 확장
        size = len(water)
        for _ in range(size):
            x,y = water.popleft() # 해당 물 좌표는 결국 한번 확인하고 다시 확인할 필요가 없다.
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isInner(nx,ny) and g[nx][ny] == blank: # 물이 확장하려는 좌표가 내부 좌표이면서 빈칸이라면
                    g[nx][ny] = w # 물로 채우기
                    water.append((nx,ny))
        # print("물 확장 후 보드 출력해보기 ")
        # printBoard()
        # step2 : 비버 이동 # 즉 비버 위치로부터 갱신
        size = len(dq)
        for _ in range(size):
            x,y,t = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isInner(nx,ny) and g[nx][ny] == blank: # ! 비버가 이동 가능한 경우
                    if t + 1 < dis[nx][ny]: # ! 최단거리 갱신 가능 하면 갱신
                        dis[nx][ny] = t+1
                        dq.append((nx,ny,t+1))
                elif isInner(nx,ny) and g[nx][ny] == des:
                    if t + 1 < dis[nx][ny]:
                        dis[nx][ny] = t + 1 # 여기서 뻗어나가면 안됨
        # print(f"비버 이동가능 좌표 갱신")
        # 갱신해야할 비버 좌표 지점 print(list(dq))
def printBoard():
    for i in range(n):
        for j in range(m):
            print(g[i][j], end = " ")
        print()

BFS(nowX, nowY)
if dis[endX][endY] == INF:
    print("KAKTUS")
else:
    print(dis[endX][endY])