
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def findCores():
    global core
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                continue
            if g[i][j] == 1:
                core.append((i, j))  # 코어 좌표 저장


# def DFS(L, useCnt, length): # ! 현재 인덱스, 코어 사용 개수, 길이
#     if L == coreCnt: # 모든 경우 확인
#         pass
#     else:

def calCoreLength():
    global coreLength
    for i in range(coreCnt):
        for dir in range(4):
            x, y = core[i]  # ! 코어 위치
            nx, ny = x, y
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if isInner(nx, ny):
                    if g[nx][ny] == 1:  # 갈 수 없는 경우
                        coreLength[i][dir] = 0
                        break
                else:
                    coreLength[i][dir] = abs(core[i][0] - x) + abs(core[i][1] - y)
                    break
                x, y = nx, ny


def DFS(L, useCnt, length):
    global maxCore, minLength, coreCnt
    if L == coreCnt:
        if useCnt > maxCore:
            maxCore = useCnt
            minLength = length
        elif useCnt == maxCore:
            minLength = min(minLength, length)
    else:
        for i in range(4):  # ! 각 코어별 해당 방향 이동 가능한지 체크
            x, y = core[L]  # 현재 코어의 위치
            if canConnect(x, y, i):
                drawLine(x, y, i, 1)  # 해당 라인 체크 후
                DFS(L + 1, useCnt + 1, length + coreLength[L][i])  # ! 해당 방향 사용
                drawLine(x, y, i, 0)  # ! 백트랙킹 시 원상 복구
        DFS(L + 1, useCnt, length)  # ! 역시 해당 코어 사용 안하는 경우도 생각


def drawLine(x, y, dir, val):
    # ! 전선을 그리거나 지우는 용도
    while True:
        x += dx[dir]
        y += dy[dir]
        if isInner(x, y):
            g[x][y] = val
        else:
            break


def canConnect(x, y, dir):  # ! 해당 코어의 현재 위치에서 해당 방향으로 전선을 놓을 수 있는지 확인
    while True:
        x += dx[dir]
        y += dy[dir]
        if not isInner(x, y):
            return True
        if g[x][y] != 0:
            return False


def isInner(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    core = []
    findCores()
    coreCnt = len(core)  # ! 코어 개수
    coreLength = [[0] * 4 for _ in range(coreCnt)]  # !각 코어 별 4방 가능한 경우 길이 미리 계산
    calCoreLength()
    maxCore = 0
    minLength = int(1e9)
    DFS(0, 0, 0)
    print(f"#{t} {minLength}")
