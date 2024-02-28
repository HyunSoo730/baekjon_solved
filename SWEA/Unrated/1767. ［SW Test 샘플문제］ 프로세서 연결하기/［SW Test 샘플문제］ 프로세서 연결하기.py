
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  # ! 위, 오른쪽, 아래, 왼쪽
up, right, down, left = 0, 1, 2, 3


def isInner(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def calDis(core):
    # ! 방향은 위, 오른쪽, 아래, 왼쪽 순으로 길이 저장된다.
    global coreLength
    for i in range(len(core)):
        for dir in range(4):
            x, y = core[i][0], core[i][1]  # ! 방향 바꿀 때마다 초기화 해줘야함
            while (True):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if isInner(nx, ny):
                    if g[nx][ny] == 1:  # 갈 수 없는 경우
                        coreLength[i].append(0)
                        break
                else:
                    # print(f"기존 좌표 : ({core[i][0]}, {core[i][1]}) 구한 좌표 : ({x}, {y}) 길이 : {abs(core[i][0] - x) + abs(core[i][1] - y)}")
                    coreLength[i].append(abs(core[i][0] - x) + abs(core[i][1] - y))
                    break
                x, y = nx, ny  # 다시 갱신


def findCores():
    global core
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    continue
                else:
                    core.append((i, j))


def canConnect(x,y,dir):
    # ! 전선을 연결할 수 있는지 확인하는 함수
    nx,ny = x,y
    while True:
        nx += dx[dir]
        ny += dy[dir]
        if not isInner(nx,ny): # 경계를 벗어나면 연결 가능
            return True
        if g[nx][ny] != 0: # 다른 코어나 전선 만나면 연결 불가능
            return False

def drawLine(x,y,dir, val):
    # ! 전선을 그리거나 지우는 함수 (val : 1 -> 그리기, val : 0 -> 지우기)
    nx,ny = x,y
    while True:
        nx += dx[dir]
        ny += dy[dir]
        if not isInner(nx,ny):
            break
        g[nx][ny] = val

def DFS(L, useCnt, length):
    global maxCore, minLength
    if L == cnt:  # ! 모든 코어 확인한 경우
        if useCnt > maxCore: # ! 사용한 코어 개수 : useCnt
            maxCore = useCnt
            minLength = length
        elif useCnt == maxCore: # 같은 코어 수를 연결했지만 더 짧은 경우
            minLength = min(minLength, length)

    else: # 아니라면 현재 코어 4방향 모두 확인
        for dir in range(4):
            x,y = core[L] # 현재 코어의 좌표 꺼내서
            if canConnect(x,y,dir): # 현재 방향으로 전선을 연결할 수 있는 경우
                drawLine(x,y,dir, 1)
                DFS(L+1, useCnt + 1, length + coreLength[L][dir])
                drawLine(x,y,dir, 0)
        DFS(L+1, useCnt, length) # 현재 코어를 연결하지 않고 다음 코어로 이동


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    core = []
    # ! 먼저 가장 자리 코어 제외 저장
    findCores()
    cnt = len(core)  # 저장된 코어 개수
    coreLength = [[] for _ in range(len(core))]
    calDis(core) # ! 각 코어에서 4방향으로의 최소 길이 계산

    maxCore = 0
    minLength = int(1e9)
    # print(f"현재 n : {n}")
    # print (core)
    # print(coreLength)
    DFS(0,0,0)

    print(f"#{t} {minLength}")
