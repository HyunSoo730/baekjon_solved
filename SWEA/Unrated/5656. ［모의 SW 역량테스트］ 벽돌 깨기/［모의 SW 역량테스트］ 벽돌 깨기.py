from collections import deque


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def isInner(x,y):
    if 0<=x<h and 0<=y<w:
        return True
    return False
def BFS(x,y,power,board): # ! 해당 보드의 x,y에서부터 폭탄 터지기 시작
    board[x][y] = 0 # ! 시작좌표 역시 0으로 만들고 진행
    dq = deque()
    dq.append((x,y,power))
    while dq:
        x,y,level = dq.popleft() # ! 폭탄이 터질 좌표 + 폭탄 범위
        for d in range(1,level): # level가 1이면 본인 자리만 터지는게 맞으므로 이렇게 표현
            for i in range(4):
                nx = x + dx[i] * d
                ny = y + dy[i] * d
                if isInner(nx,ny) and board[nx][ny] > 0: # ! 벽돌이 존재하는 곳이라면
                    dq.append((nx,ny,board[nx][ny]))
                    board[nx][ny] = 0

def print_board(board):
    for x in range(h):
        for y in range(w):
            print(board[x][y], end = " ")
        print()

def reboard(board):
    for y in range(w):
        temp = []
        for x in range(h):
            if board[x][y] > 0:
                temp.append(board[x][y])
        new_list = [0] * (h-len(temp)) + temp
        for i in range(h):
            board[i][y] = new_list[i]
    # print("보드 중력 적용 후 출력")
    # print_board(board)

def DFS(L,board): # ! 해당
    global res
    if L == n: # ! 모든 폭탄을 다 떨어트린 경우
        # ! 남은 개수 구하기
        cnt = 0
        for x in range(h):
            for y in range(w):
                if board[x][y] > 0:
                    cnt += 1
        res = min(res, cnt)
    else:
        for y in range(w):
            g = [arr[:] for arr in board] # ! 배열 복사 후 진행
            # print_board(g)
            a,b = 0,0
            flag = False
            for x in range(h): # ! 행 순차적으로 탐색하면서 처음으로 만나는 벽돌 좌표 구하기
                if g[x][y] > 0: # ! 벽돌 발견
                    flag = True
                    a,b = x,y
                    break
            # 폭탄 투하
            if flag:
                BFS(a,b,g[a][b], g) # ! 해당 보드에 폭탄 투하
            # ! 폭탄 투하가 끝나면 보드를 원상복구 시키고 넘기기
            reboard(g)
            DFS(L+1,g)


T = int(input())
for t in range(1,T+1):
    n,w,h = map(int, input().split()) # ! n개의 벽돌 떨어뜨리기, wxh 크기 배열
    board = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    res = int(1e9)
    DFS(0,board)

    print(f"#{t} {res}")

