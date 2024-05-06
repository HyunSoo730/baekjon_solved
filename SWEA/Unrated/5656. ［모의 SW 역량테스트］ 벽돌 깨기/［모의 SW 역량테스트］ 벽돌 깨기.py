from collections import deque


# 벽돌 깨기
# 구슬 n번 쏠 수 있음. 구슬은 좌우로만 움직일 수 있고, 항상 맨 위에 있는 벽돌만 깬다.
# 각 칸의 값은 벽돌의 크기, 벽돌 크기 - 1만큼 상하좌우 제거
# 벽돌은 연쇄적으로 터진다.
# 벽돌 제거 후 중력작용
# 벽돌 깨기 이후에 남은 벽돌의 개수를 구하는데, 최소로 남게끔 구하기

# 1. 벽돌 떨어뜨릴 위치 정하기 (중복 순열) -> 어디든지 가능 , 순서 중요
# 2. 떨어뜨릴 위치 정하면 벽돌 떨어뜨리기
# 3. 연쇄 작용으로 벽돌 제거
# 4. 가능한 모든 벽돌 제거 후 중력 작용. (아래로 떨어뜨려야함)
# 총 n번 반복하기

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def BFS(startX,startY,power, g):
    dq = deque()
    dq.append((startX,startY,power)) # 현재 퍼져야 할 크기 함께 저장
    g[startX][startY] = 0 # 시작점 꺤걸로 시작.
    while dq:
        x,y,p = dq.popleft()
        for i in range(4):
            for d in range(p): # p-1만큼 퍼져나가야 하므로
                nx = x + dx[i] * d
                ny = y + dy[i] * d
                if not isInner(nx,ny): continue
                if g[nx][ny] > 0: # 벽돌 깨야함
                    dq.append((nx,ny,g[nx][ny]))
                    g[nx][ny] = 0

def 벽돌깨기(y,g): # 현재 보드의 y번쨰 열에서 구슬 떨어뜨림
    for x in range(n):
        if g[x][y] > 0: # 벽돌 깨기 시작
            BFS(x,y,g[x][y], g)
            break

def 벽돌떨어뜨리기(L,g):
    global res
    if L == count: # 모두 떨어뜨림 -> 카운트 해야함
        cnt = 남은벽돌개수(g)
        res = min(res, cnt)
    else: # 아직이라면 떨어뜨리기
        for y in range(m): # 열 만큼 돌아야함
            copy_g = [arr[:] for arr in g] # 배열 복사 -> 영향을 끼치기 때문에 배열 복사하면서 진행
            # print("벽돌 깨기 전 보드")
            # 보드출력(copy_g)
            벽돌깨기(y,copy_g)
            # print("벽돌 꺠고난 후 보드")
            # 보드출력(copy_g)
            중력작용(copy_g)
            # print("중력작용 후 보드")
            # 보드출력(copy_g)
            벽돌떨어뜨리기(L+1, copy_g)
def 중력작용(g):
    for y in range(m):
        temp = []
        for x in range(n):
            if g[x][y] > 0:
                temp.append(g[x][y])
        new_list = [0] * (n-len(temp)) + temp # 중력작용 적용 후
        for i in range(n):
            g[i][y] = new_list[i]
def 남은벽돌개수(g):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] > 0:
                cnt += 1
    return cnt
def 보드출력(g):
    print("=========현재 보드 상황=============")
    for i in range(n):
        for j in range(m):
            print(g[i][j], end = " ")
        print()

T = int(input())
for t in range(1,T+1):
    count, m,n = map(int, input().split()) # count만큼 벽돌 떨어뜨리기, 가로,세로
    g = [list(map(int, input().split())) for _ in range(n)]
    res = int(1e9)
    벽돌떨어뜨리기(0,g)
    print(f"#{t} {res}")