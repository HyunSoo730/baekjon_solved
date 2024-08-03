import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# nxn 대나무숲.
# 상하좌우 이동하면서 대나무 먹음. 대나무 먹을 때의 조건.
# 현재 지역보다 대나무가 많이 있어야 이동 가능. -> 조건
# 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민
# -> 시작지점 랜덤

# n <= 500

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j]는 i,j에서 시작했을 떄의 최대 경로 수
dp = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isInner(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def DFS(x, y):  # (x,y)에서 시작했을 떄...
    if dp[x][y]:  # 값이 존재하면
        return dp[x][y]
    else:  # 값이 없다면 탐색 진행
        dp[x][y] = 1  # 한번도 시작안했으면 본인값부터 시작.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInner(nx, ny): continue  # 외부 좌표면 끝
            if g[nx][ny] > g[x][y]:  # 이동하려는 칸이 더 많으면 이동 가능
                dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)
        return dp[x][y]


# 시작지점 랜덤.
res = 0
for i in range(n):
    for j in range(n):
        res = max(res, DFS(i, j))

print(res)