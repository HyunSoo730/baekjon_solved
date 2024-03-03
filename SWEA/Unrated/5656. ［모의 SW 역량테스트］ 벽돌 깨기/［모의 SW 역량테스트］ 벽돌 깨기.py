from collections import deque


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def destroy(x,y,g):
    # ! 해당 행 , 열 기준으로 폭파 시작
    dq = deque()
    dq.append((x,y, g[x][y]))
    g[x][y] = 0 # ! 폭파 처리
    while dq:
        x,y,power = dq.popleft() # ! 폭파해야할 위치, 범위
        for d in range(1,power):
            for i in range(4):
                nx = x + dx[i] * d
                ny = y + dy[i] * d
                if 0<=nx<h and 0<=ny<w and g[nx][ny] > 0: # ! 좌표 내부이면서 폭탄인 경우
                    dq.append((nx,ny, g[nx][ny])) # ! 연쇄 작용 진행
                    g[nx][ny] = 0

def step1(y, g): # ! 해당 열 폭파
    for x in range(h):
        if g[x][y] >= 1: # ! 폭탄이라면
            destroy(x,y,g)
            break

def step2(g): # ! 벽돌 제거한 상태에서 빈칸 메우기 -> 아래와 같이 해도 되고 deque를 사용해서 해도 되고.
    # ! 어찌됐든, 남아있는 것들을 먼저 채우고 빈칸을 채우는 개념을 사용했어야 했음.
    for y in range(w):
        temp = []
        for x in range(h):
            if g[x][y] > 0:
                temp.append(g[x][y])
        temp = [0] * (h-len(temp)) + temp # ! 남은 공간은 0으로 채움
        for x in range(h):
            g[x][y] = temp[x]

def step3(g): # ! 해당 벽돌의 남은 벽돌 개수
    cnt = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] >= 1:
                cnt += 1
    return cnt

def DFS(L, g):
    global minCnt
    if L == n: # !n번 모두 떨어뜨림
        cnt = step3(g) # ! 남은 블록 개수
        minCnt = min(minCnt, cnt)
    else: # ! 떨어뜨릴 위치 선택
        # * 먼저 맵 복사
        for i in range(w): # ! 0~w-1까지
            temp = [arr[:] for arr in g] # ! 현재 맵 복사 후 폭파 진행 (각 열에 대해 폭파를 시도할 때마다 원본 맵의 상태를 유지한 채로 새로운 시도를 해야함)
            step1(i, temp) # ! 해당 열 폭파 진행
            step2(temp)
            DFS(L+1, temp) # ! 다음  폭발로 이동

def printArray(g):
    for x in g:
        print(x)


T = int(input())
for t in range(1,T+1):
    n,w,h = map(int, input().split()) # ! 구슬 떨어뜨리는 횟수, 너비, 높이
    g = [list(map(int, input().split())) for _ in range(h)]
    # ! 1. 떨어뜨리는 위치 선택
    minCnt = int(1e9)
    DFS(0, g)

    print(f"#{t} {minCnt}")