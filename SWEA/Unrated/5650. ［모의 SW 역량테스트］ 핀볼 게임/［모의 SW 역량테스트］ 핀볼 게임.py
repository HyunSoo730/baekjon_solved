from collections import defaultdict

# 핀볼 게임
# nxn,  5가지 블록, 웜홀, 블랙홀
# 핀볼 상하좌우 중 한 방향으로 움직임
# 블록 만나면 방향 변경. 경우에 따라서 변경하기

# 블록 1~5까지 웜홀 6~10 웜홀은 반드시 쌍으로 존재. 블랙홀 -1
# 시작점으로 다시 돌아오거나 블랙홀 만나면 끝
# 출발위치 , 진행방향 임의 선정 가능.

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def 방향변경(num, dir):
    if num == 1: # 부딪힌 블록이 1번
        if dir == 2: dir = 1
        elif dir == 3: dir = 0
        else: dir = (dir + 2) % 4 # 반대
    elif num == 2: # 부딪힌 블록이 2번
        if dir == 0: dir = 1
        elif dir == 3: dir = 2
        else: dir = (dir + 2) % 4
    elif num == 3: # 부딪힌 블록이 3번
        if dir == 0: dir = 3
        elif dir == 1: dir = 2
        else: dir = (dir + 2) % 4
    elif num == 4:
        if dir == 1: dir = 0
        elif dir == 2: dir = 3
        else: dir = (dir + 2) % 4
    else:
        dir = (dir + 2) % 4
    return dir

def 웜홀만남(num, x,y): # 만난 웜홀 번호, 현재 위치
    if 웜홀[num][0][0] == x and 웜홀[num][0][1] == y:
        return 웜홀[num][1][0], 웜홀[num][1][1] # 반대 구멍 반환
    else:
        return 웜홀[num][0][0], 웜홀[num][0][1]

def 핀볼게임(startX,startY,k): # 시작위치, 시작 방향
    cnt = 0 # 점수 기록
    x,y = startX,startY
    while True:
        # 1. 현재 이동해야 하는 방향으로 이동
        x += dx[k]
        y += dy[k]
        if not isInner(x,y): # 내부 좌표 아니라면 -> 벽에 부딪힘
            x -= dx[k]
            y -= dy[k]
            k = (k+2) % 4 # 방향 변경
            cnt += 1
        if g[x][y] == -1: # 블랙홀 만남
            return cnt
        if (x,y) == (startX,startY): # 시작위치로 돌아옴
            return cnt
        if 1 <= g[x][y] <= 5: # 블록에 부딪힘
            k = 방향변경(g[x][y], k) # 현재 부딪힌 블록과 현재 방향
            cnt += 1
            continue
        if 6<=g[x][y]<=10: # 웜홀 만남
            x,y = 웜홀만남(g[x][y], x,y) # 반대 웜홀로 이동
            continue



T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    # 웜홀 따로 기록.
    웜홀 = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if g[i][j] >= 6: # 웜홀인 경우
                웜홀[g[i][j]].append((i,j)) # 해당 핀볼 넘버에 좌표 추가
    max_cnt = 0
    for x in range(n):
        for y in range(n):
            if g[x][y] == 0: # 시작위치 가능
                for k in range(4): # 시작위치에서 4방향 모두 가능
                    cnt = 핀볼게임(x,y,k)
                    max_cnt = max(max_cnt, cnt)

    print(f"#{t} {max_cnt}")