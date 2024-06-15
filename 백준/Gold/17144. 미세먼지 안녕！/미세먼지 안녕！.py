import sys

# nxm 보드
# 공기청정기는 항상 1열에 설치되어 있고, 두 행을 차지.
# 공기 청정기가 설치되지 않은 칸에는 미세먼지 존재. (각 칸의 값이 미세먼지 크기)

# 1-1. 미세먼지는 확산된다. 확산은 모든 칸에서 동시에 발생.
# 1-2. (r,c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 해당 방향으로 확산되지 않음.
# 1-3. 확산되는 양은 각 칸의 값 / 5, 소수점 버림.

# 2. 공기청정기 작동
# 위쪽 공기청정기는 반시계방향으로 순환, 아래쪽 공기청정기는 시계방향으로 순환.



dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def step1(x,y,g,temp):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny):
            continue
        if g[nx][ny] == -1: continue # 미세먼지
        cnt += 1

    val = int(g[x][y] / 5)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue
        if g[nx][ny] == -1: continue
        temp[nx][ny] += val
    temp[x][y] -= val * cnt



# step1. 확산
def 확산(g):
    temp = [arr[:] for arr in g]
    for x in range(n):
        for y in range(m):
            if g[x][y] > 0:
                step1(x,y,g,temp)
    return temp

# step2. 공기청정기
def 미세먼지순환(g):
    # 1. 위쪽 공기청정기
    x,y = 공기청정기[0][0], 공기청정기[0][1] # 위쪽 공기청정기 좌표
    tx,ty = x,y
    dir = 0 # 시작 방향
    L = 0
    while True:
        if (x,y) == (tx,ty) and L == 3: # 방향전환 + 시작위치 돌아옴
            break
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (0<=nx<=tx and 0<=ny<m):
            L += 1
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        g[x][y] = g[nx][ny]
        x,y = nx,ny # 위치 이동
    g[tx][ty] = 0
    g[tx][ty+1] = 0

    # 2. 아래쪽 공기청정기
    x,y = 공기청정기[1][0], 공기청정기[1][1]
    tx,ty = x,y
    dir = 2 # 시작 방향
    L = 0
    while True:
        if (x,y) == (tx,ty) and L == 3:
            break
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (tx<=nx<n and 0<=ny<m):
            L += 1
            dir = (dir + 3) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        g[x][y] = g[nx][ny]
        x,y = nx,ny # 위치 변경
    g[tx][ty] = 0
    g[tx][ty+1] = 0



n,m,T = map(int, input().split()) # T초 후의 미세먼지 양 구하기
g = [list(map(int, input().split())) for _ in range(n)]
공기청정기 = []

for i in range(n):
    if g[i][0] == -1: # 공기청정기
        공기청정기.append((i,0))

def 보드출력(g):
    print("======================")
    for x in range(n):
        for y in range(m):
            print(g[x][y], end = " ")
        print()

for i in range(T):
    # 1. 확산
    g = 확산(g)
    # 2. 순환
    미세먼지순환(g)
    # 보드출력(g)

res = 0
for i in range(n):
    for j in range(m):
        if g[i][j] > 0:
            res += g[i][j]
print(res)