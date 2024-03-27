import sys


n,m = map(int, input().split())
nowX,nowY, direction, = map(int, input().split()) # ! 현재 로봇 좌표, 방향
g = [list(map(int, input().split())) for _ in range(n)]
# ! (0,0) -> (n-1,m-1) 로 이동하기

up, right, down, left = 0,1,2,3

# ! 청소하지 않은 칸 : 0 벽 : 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

def DFS(x,y):
    global cnt, direction
    global nowX, nowY

    # ! step1
    if g[x][y] == 0:
        g[x][y] = 2 # ! 방 청소 처리
        cnt += 1
    flag = False
    d = direction
    for i in range(4): # ! 시계방향으로 돌면서 확인
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
            flag = True
            break

    # ! d에 대해서 실행.
    if flag:
        direction = d
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
            DFS(nx,ny)
        else:
            DFS(x,y)
    else: # ! 이동 불가능 -> 여기서는 그냥 빈칸도 이동 가능
        nx = x - dx[direction]
        ny = y - dy[direction]
        if 0<=nx<n and 0<=ny<m and g[nx][ny] != 1:
            DFS(nx,ny) # ! 후진
        else:
             return # ! 후진 안되면 끝.

DFS(nowX, nowY)
print(cnt)