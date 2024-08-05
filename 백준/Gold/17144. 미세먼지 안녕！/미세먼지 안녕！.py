import sys

# 공기 청정기는 항상 1번 열에 설치되어 있음 크기는 두 행 차지

# 1. 미세먼지 확산 -> 모든 칸에서 동시에 일어난다.
# 1-1. 현재 칸 기준 인접한 네 방향으로 확산
# 1-2. 인접한 방향에 공기청정기 or 벽. 확산 X (확산되는 양은 val / 5) 소수점 버림
# 1-3. 확산 후 남은 미세먼지 양은 val - (val/5) * 확산 칸

# 2 공기청정기 작동
# 2-1. 위쪽 공기청정기 바람 반시계 순환
# 2-2. 아래쪽 공기청정기 바람 시계방향 순환
# 2-3. 바람이 불면 미세먼지가 바람의 방향대로 모두 한칸씩 이동
# 2-4. 공기 청정기로 들어가면 끝

n,m,T = map(int,input().split())
g = [list(map(int, input().split())) for _ in range(n)]

air = [[0] * 2 for _ in range(2)]
idx = 0
for i in range(n):
    if g[i][0] == -1: # 공기청정기
        air[idx][0], air[idx][1] = i,0
        idx += 1
    if idx == 2:
        break

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def step1(x,y,g,temp): # 현재 칸의 값과 위치
    cnt = 0 # 확산 칸 개수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue
        if g[nx][ny] == -1: continue # 공기청정기
        cnt += 1
    val = int(g[x][y] / 5)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue
        if g[nx][ny] == -1: continue
        temp[nx][ny] += val
    temp[x][y] -= val * cnt




def 확산(g): # -> 모든 칸에서 동시에 발생
    temp = [arr[:] for arr in g] # 복사
    for i in range(n):
        for j in range(m):
            if g[i][j] > 0: # 확산 가능
                step1(i,j,g,temp)
    return temp

def 순환(g):
    # 위쪽 공기청정기, 아래쪽 공기청정기 나눠서 진행
    x,y = air[0][0], air[0][1] # 첫번째 공기 청정기
    endX,endY = x,y # 돌아왔을 때 종료조건 용
    # 위쪽 공기청정기 방향 바뀌는 순서 (위로 -> 오른쪽으로 -> 아래로 -> 왼쪽으로)
    dir = 0
    change = 0 # 방향전환 횟수
    while True:
        if (x,y) == (endX,endY) and change == 3: # 원위치 돌아옴
            break
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not(0<=nx<=endX and 0<=ny<m): # 방향 바꿔
            dir = (dir + 1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
            change += 1 # 방향전환 횟수 추가
        g[x][y] = g[nx][ny]
        x,y = nx,ny # 이동
    g[endX][endY] = 0
    g[endX][endY+1] = 0 # 마지막 부분 옮기고 끝냈어야 함.

    x,y = air[1][0], air[1][1] # 두번째 공기 청정기
    endX,endY = x,y
    # 아래쪽 공기 청정기 방향 바뀌는 순서 (아래 -> 오른쪽 -> 위 -> 왼쪽) # 반시계
    dir = 2
    change = 0
    while True:
        if (x,y) == (endX,endY) and change == 3:
            break
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (endX<=nx<n and 0<=ny<m): # 방향 바꿔
            dir = (dir + 3) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
            change += 1
        g[x][y] = g[nx][ny]
        x,y = nx,ny
    g[endX][endY] = 0
    g[endX][endY+1] = 0

    g[air[0][0]][air[0][1]] = -1
    g[air[1][0]][air[1][1]] = -1 # 다시 공기청정기 처리

for _ in range(T):
    # 1. 확산
    g = 확산(g)
    # 2. 순환
    순환(g)

cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] > 0:
            cnt += g[i][j]
print(cnt)