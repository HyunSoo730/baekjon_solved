from collections import defaultdict, deque

# 핀볼 게임
# nxn 보드, 정사각형 블록, 4가지 삼각형 블록, 웜홀, 블랙홀 존재
# 핀볼은 상하좌우로 이동
# 1. 핀볼이 블록을 만났을 때
# 블록의 수평면이나 수직면 만나면 방향 반대로 진행, 경사면 만나면 직각으로 진행 방향 꺾어서 진행
# 2. 핀볼이 벽을 만날 경우 반대 방향으로 돌아온다.
# 3. 핀볼이 웜홀을 만났을 때 -> 다른 반대편 웜홀로 빠져 나오게 되며, 진행방향은 그대로 유지
# 4. 핀볼이 블랙홀 만났을 때, 게임 끝
# 블랙홀 : -1, 빈공간 : 0, 1~5 블록, 6~10 웜홀
# 종료조건 : 핀볼이 출발위치로 돌아오거나, 블랙홀에 빠질 때 끝. 점수는 벽이나 블록에 부딪힌 횟수
# 얻을 수 있는 점수의 최댓값 구하기

# 1. 빈공간에서 게임 시작. 진행 방향 임의로 선정 가능.
# 2. 시작위치 및 진행 방향 선정했다면 해당 방향으로 이동
# 3. 이동하면서, 블록, 웜홀, 블랙홀 만날 때를 각각 생각하면서 카운트 진행

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def 핀볼게임(startX,startY,dir):
    x,y,d = startX,startY,dir
    cnt = 0 # 현재 시작위치 및 시작방향에서의 점수
    while True:
        x += dx[d]
        y += dy[d]
        if not isInner(x,y): # 벽 부딪힌 경우
            d = (d+2)%4 # 방향 전환
            cnt += 1
            continue
            # 벽 부딪히고 바로 돌아가면 안돼 이후 과정을 수행해야만 함.
        if (x, y) == (startX, startY) or g[x][y] == -1:  # 시작위치 or 블랙홀 -> 종료조건 검사는 중간에 해야하는가 ?
            return cnt
        if 1<=g[x][y]<=5: # 블록 만난 경우
            d = 블록만남(d, g[x][y])
            cnt += 1
        elif 6<=g[x][y]<=10: # 웜홀 만난 경우 -> 방향은 유지.
            holeA = 웜홀[g[x][y]][0]
            holeB = 웜홀[g[x][y]][1]
            if (x,y) == (holeA[0],holeA[1]): # 반대방향으로 나가야함
                x = holeB[0]
                y = holeB[1]
            else:
                x = holeA[0]
                y = holeA[1]



def 블록만남(dir,block_num): # 현재 진행방향에 따라서 블록 처리
    if block_num == 1:
        if dir == 0: dir = 2
        elif dir == 1: dir = 3
        elif dir == 2: dir = 1
        elif dir == 3: dir = 0
    elif block_num == 2:
        if dir == 0: dir = 1
        elif dir == 1: dir = 3
        elif dir == 2: dir = 0
        elif dir == 3: dir = 2
    elif block_num == 3:
        if dir == 0: dir = 3
        elif dir == 1: dir = 2
        elif dir == 2: dir = 0
        elif dir == 3: dir = 1
    elif block_num == 4:
        if dir == 0: dir = 2
        elif dir == 1: dir = 0
        elif dir == 2: dir = 3
        elif dir == 3: dir = 1
    elif block_num == 5:
        dir = (dir + 2) % 4
    return dir

# def 블록만남(direction, num): # 현재 블록번호와, 현재 방향
#     if num == 1:
#         if direction == 2: direction = 1
#         elif direction == 3: direction = 0
#         else: direction = (direction + 2) % 4
#     elif num == 2:
#         if direction == 0: direction = 1
#         elif direction == 3: direction = 2
#         else: direction = (direction + 2) % 4
#     elif num == 3:
#         if direction == 0: direction = 3
#         elif direction == 1: direction = 2
#         else: direction = (direction + 2) % 4
#     elif num == 4:
#         if direction == 1: direction = 0
#         elif direction == 2: direction = 3
#         else: direction = (direction + 2) % 4
#     else:
#         direction = (direction + 2) % 4
#     return direction

T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    웜홀 = defaultdict(list)
    시작위치 = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0: # 시작위치 가능
                시작위치.append((i,j))
            if 6<=g[i][j]<=10: # 웜홀
                웜홀[g[i][j]].append((i,j)) # key를 웜홀 번호로 해서 저장
    res = 0
    for x,y in 시작위치:
        for dir in range(4):
            cnt = 핀볼게임(x,y,dir)
            res = max(res, cnt)
    print(f"#{t} {res}")