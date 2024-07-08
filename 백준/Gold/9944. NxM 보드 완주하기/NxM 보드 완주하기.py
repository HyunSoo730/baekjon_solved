import sys

from collections import deque

# nxn 보드, 각 칸은 빈칸 또는 장애물
# 보드 위에 공 하나 놓아야 함.
# 상하좌우 중 방향 하나 고른 후 그 방향으로 계속 이동시킨다
# 공은 장애물, 보드의 경계, 이미 공이 지나갔던 칸을 만나기 전까지 계속 이동
# 더이상 이동할 수 없을 때 끝난다. -> 모든 빈칸을 방문한 적이 있어야 함
# 모든 칸을 방문하기 위한 이동 횟수의 최솟값

# 시작위치는 어디든 상관없음
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

blank = "."
wall = "*"
def isInner(x, y):
    return 0 <= x < n and 0 <= y < m


def DFS(x, y, dir, now, change):
    global res
    if change >= res:
        return
    if now == cnt: # 현재 빈칸 모두 방문
        res = min(res,change)
    else: # 그게 아니라면 계속 이동
        nx = x + dx[dir]
        ny = y + dy[dir]
        if isInner(nx,ny) and g[nx][ny] == blank and not visited[nx][ny]: # 빈칸이면서 내부인 경우에 이동 가능
            visited[nx][ny] = True
            DFS(nx,ny,dir,now+1, change)
            visited[nx][ny] = False
        else: # 그 경우가 아니라면 방향 전환
            for i in range(1,4):
                dir = (dir + i) % 4
                nx = x + dx[dir]
                ny = y + dy[dir]
                if isInner(nx,ny) and g[nx][ny] == blank and not visited[nx][ny]:
                    visited[nx][ny] = True
                    DFS(nx,ny,dir,now+1,change+1)
                    visited[nx][ny] = False

case = 1
while True:
    try:
        n, m = map(int, input().split())
        g = [list(map(str,input())) for _ in range(n)]

        cnt = 0
        start_point = deque()
        for i in range(n):
            for j in range(m):
                if g[i][j] == ".":  # 시작점 가능
                    start_point.append((i, j))
                    cnt += 1 # 빈칸 개수
        res = int(1e9)

        for x,y in start_point:
            for dir in range(4):
                visited = [[False] * m for _ in range(n)]
                visited[x][y] = True
                DFS(x,y,dir,1,1)

        if cnt == 1:
            print(f"Case {case}: {0}")
        elif res == int(1e9):
            print(f"Case {case}: {-1}")
        else:
            print(f"Case {case}: {res}")
        case += 1
        # 여기서 문제를 해결하는 로직을 구현

        # 결과 출력

    except EOFError:
        break