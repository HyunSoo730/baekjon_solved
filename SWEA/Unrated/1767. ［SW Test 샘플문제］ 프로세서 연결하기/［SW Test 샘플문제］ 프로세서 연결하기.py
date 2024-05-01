
# nxn 보드
# 각 칸은 셀이라고 부름. 각 칸은 1개의 코어 혹은 전선이 올 수 있다.
# 보드의 가장자리에는 전원이 흐른다
# 코어와 전원을 연결하는 전선은 직선으로만 설치가 가능, 상하좌우 , 교차 안된다
# 전원 연결 위해서 가장자리로 코어와 전선 연결해야함
# 가장자리 코어 전원 연결된 것으로 간주,
# 최대한 많은 코어에 전원을 연결했을 경우 ,전선 길이의 합 구하기
# 전선 길이의 합이 최소가 되는 전선 길이의 합 구하기

# 0 빈 셀, 1은 코어

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def DFS(L, cores,length,g): # 현재 몇번째 코어인지, 현재까지의 길이
    global max_cores, min_length
    if max_cores > cores + (core_cnt - L): # 최대로 연결된 코어수 > 현재 연결 코어수  + 남은 코어수
        return
    if L == core_cnt:  # 모두 확인 -> 최소값인지 계산
        if cores == max_cores:
            min_length = min(min_length, length)
        elif cores > max_cores:
            max_cores = cores
            min_length = length
    else: # 아니라면 현재 코어의 상하좌우 중 전원 연결 가능하다면 연결 후 넘기기
        # print(f"현재 코어 : {L}, 코어 위치 : {data[L][0], data[L][1]}")
        for i in range(4):
            # copy_g = [arr[:] for arr in g] # 배열 복사
            if can_draw(L, i, g): # 배열 복사가 아닌...
                # print(f"현재 {L}코어 방향{i}는 라인 그릴 수 있음")
                line_cnt = draw_line(L, i, g,1) # i방향으로 그리기 가능하면 그리기
                # 보드출력(copy_g)
                DFS(L+1, cores+1, length+line_cnt, g)
                draw_line(L,i,g,0)
            else:
                # print(f"현재 {L}코어 방향{i}는 라인 못그림")
                # 보드출력(copy_g)
                DFS(L+1, cores,length, g)
def can_draw(L, dir, g): # L번째 코어, dir방향으로 그리기 가능한지
    x,y = data[L] # 현재 코어의 위치
    while True:
        x += dx[dir]
        y += dy[dir]
        if not isInner(x,y):
            return True # 그을 수 있음
        if g[x][y] == 1: return False
def draw_line(L, dir, g, val):
    x,y = data[L] # 현재 코어의 dir 방향으로 긋기
    # print(f"현재 코어:{L}, 현재 코어 위치:{x,y} 그리는 방향 : {dir}")
    cnt = 0
    while True:
        x += dx[dir]
        y += dy[dir]
        if not isInner(x,y):
            return cnt
        g[x][y] = val
        cnt += 1
def 보드출력(g):
    print("=======현재 보드 출력========")
    for i in range(n):
        for j in range(n):
            print(g[i][j], end = " ")
        print()

T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    data = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            if g[i][j] == 1:
                data.append((i,j)) # 코어 위치 저장
    core_cnt = len(data)
    max_cores = 0
    min_length = int(1e9)
    DFS(0,0,0,g)
    print(f"#{t} {min_length}")