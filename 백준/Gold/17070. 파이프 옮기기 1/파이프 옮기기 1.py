import sys


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

# 끝점만 판단하면 돼
cnt = 0
endX, endY = n - 1, n - 1


def is_valid_move(x, y, d):
    if d == 0:  # 가로
        return y + 1 < n and g[x][y + 1] == 0
    elif d == 1:  # 세로
        return x + 1 < n and g[x + 1][y] == 0
    else:  # 대각선
        return x + 1 < n and y + 1 < n and (g[x][y+1] == 0 and g[x+1][y] == 0 and g[x+1][y+1] == 0)


dx = [0, 1, 1]
dy = [1, 0, 1]


def DFS(x, y, d):
    global cnt
    if (x, y) == (endX, endY):
        cnt += 1
    else:
        if d in [0, 2] and is_valid_move(x, y, 0):  # 현재 방향이 가로나 대각선일때만 가로로 이동 가능
            DFS(x, y + 1, 0)
        if d in [1, 2] and is_valid_move(x, y, 1):  # 현재 방향이 세로, 대각선일 때 세로로 이동 가능
            DFS(x + 1, y, 1)
        if is_valid_move(x, y, 2):  # 현재 어떤 방향이든 대각선 이동은 가능
            DFS(x + 1, y + 1, 2)

if g[endX][endY] == 1: print(0)
else:
    DFS(0,1,0)
    print(cnt)