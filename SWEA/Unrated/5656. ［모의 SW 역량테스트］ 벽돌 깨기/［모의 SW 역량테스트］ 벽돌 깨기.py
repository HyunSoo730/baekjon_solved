from collections import deque

# 벽돌깨기
# 1. 조건
# 1-1. 구슬 n번 쏠 수 있음
# 1-1-1. 구슬은 좌우로 움직일 수 있고, 항상 맨 위에 있는 벽돌만 깬다.
# 1-1-2. 벽돌의 값만큼의 범위가 제거된다. 1은 본인만, 3이면 본인 포함 + 2길이의 상하좌우 제거
# 1-2. 벽돌 제거 시 벽돌은 연쇄 제거
# 1-3. 해당 구슬로 인해 제거할 수 있는 모든 벽돌 제거 후 벽돌을 아래로 내려야 함(중력작용)

# 2. 풀이
# 필요 기능 : 구슬은 좌우로 이동할 수 있다 -> 매 번 모든 열 중에 한 곳으로 떨어짐. 순서 의미 있고 중복 가능(같은 선택 가능) -> 중복 순열
# 벽돌 연쇄 제거 기능
# 벽돌 제거 후 중력작용을 통해 내려야 한다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<h and 0<=y<w:
        return True
    return False

def BFS(a,b,power,g):
    dq = deque()
    dq.append((a,b,power)) # 해당 좌표부터 벽돌 깨기 (범위 같이 받음)
    g[a][b] = 0 # 시작좌표 벽돌 깨고 시작

    while dq:
        x,y,p = dq.popleft()
        for d in range(1,p): # 1인 경우 그냥 끝내버리기 위해
            for i in range(4):
                nx = x + dx[i] * d
                ny = y + dy[i] * d
                if isInner(nx,ny) and g[nx][ny] > 0: # 벽돌 존재 -> 깨기
                    dq.append((nx,ny,g[nx][ny])) # 해당 좌표 깼으니 그 좌표에서 다시 깨기
                    g[nx][ny] = 0


def destroy(y, g): # y열에 폭탄 떨어뜨림
    for x in range(h):
        if g[x][y] > 0: # 처음으로 만나는 벽돌
            BFS(x,y,g[x][y], g)
            return

def recover(g):
    for y in range(w):
        temp = []
        for x in range(h):
            if g[x][y] > 0:
                temp.append(g[x][y]) 
        new_list = [0] * (h-len(temp)) + temp # 중력작용을 위한 작용. 위에서부터 0으로 채워야 하니까
        for i in range(h):
            g[i][y] = new_list[i] # 중력 작용
            
def DFS(L, g):
    global res
    if L == n: # n번 모두 떨어뜨림 -> 종료조건
        cnt = count_board(g)
        res = min(res, cnt)
        # print("최종 보드")
        # print_board(g)
        # print(f"최종 보드에 남은 개수 = {cnt}")

    else: # 아직 다 떨어뜨리지 않은 경우 떨어뜨려
        for i in range(w): # i번쨰 열에 떨어뜨림 -> 안되는 경우에는 백트랙킹 -> 원상복구해야함
            copy_g = [arr[:] for arr in g] # 배열 복사
            # print("현재 깨기 전")
            # print_board(copy_g)
            # print("깬 후 보드")
            destroy(i,copy_g) # 벽돌깨기
            # print_board(copy_g)
            # print("리커버리 후 보드")
            recover(copy_g) # 중력작용
            # print_board(copy_g)
            DFS(L+1, copy_g) # 백트랙킹 시 어차피 매번 배열 복사하므로 알아서 원상복구 됨
            # 이 문제는 전체 한 칸만 되돌리는게 아니라, 전체 보드를 되돌려야 하므로 배열 복사하는게 맞아.
            # 근데 다른 문제들 중에 딱 한 칸에 대해서만 원상복구를 해야하는 경우는 백트랙킹 시 그 선택에 대해서만 원상복구하면 돼

def count_board(g):
    cnt = 0
    for x in range(h):
        for y in range(w):
            if g[x][y] >0:
                cnt += 1
    return cnt

def print_board(g):
    print("현재 보드 출력")
    for x in g:
        print(*x)

T = int(input())
for t in range(1,T+1):
    n, w, h = map(int, input().split())  # n번 구슬 떨어뜨리는데, wxh 보드에
    g = [list(map(int, input().split())) for _ in range(h)]
    # step1 : 중복 순열 내에서 조작
    res = int(1e9)
    DFS(0, g)
    print(f"#{t} {res}")

