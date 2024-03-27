import sys
from collections import deque


g = [list(map(int, input())) for _ in range(9)]
# ! 9x9 스도쿠

# ! 좋은 방향 : 일단 0인 좌표를 미리 넣어둔다
dq = deque()
for i in range(9):
    for j in range(9):
        if g[i][j] == 0:
            dq.append((i,j)) # ! 해당 좌표 넣어둠

x,y = dq[0] # ! 시작 좌표
def check_row(x,y,val):
    # ! 해당 행 검사 -> 행 고정, 열 변수
    for i in range(9):
        if g[x][i] == val: # ! 이미 존재
            return False
    else:
        return True
def check_col(x,y,val):
    # ! 해당 열 검사 -> 열 고정, 행 변수
    for i in range(9):
        if g[i][y] == val: # ! 이미 존재
            return False
    else:
        return True

def check(x,y,val): # ! 현재 좌표가 속한 미니 박스 확인
    dx = (x // 3) * 3
    dy = (y // 3) * 3
    for i in range(dx,dx+3):
        for j in range(dy,dy+3):
            if g[i][j] == val:
                return False
    return True

flag = True
def DFS(L):
    global flag
    if not flag: return
    if L == len(dq):
        flag = False
    else:
        x,y = dq[L]
        for i in range(10):
            if check(x,y,i) and check_row(x,y,i) and check_col(x,y,i):
                g[x][y] = i
                DFS(L+1)
                if not flag: return # ! 다 돌았으면 원상복구 안함.
                g[x][y] = 0


DFS(0)
for i in range(9):
    for j in range(9):
        print(g[i][j], end = "")
    print()