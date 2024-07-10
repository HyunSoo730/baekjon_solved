import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isInner(x, y):
    return 0 <= x < n and 0 <= y < n


dp = [[0] * n for _ in range(n)]


# dp[x][y]는 (x,y)에서 시작했을 때 최댓값
def DFS(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1  # 만약 한번도 시작안했다면 해당 값으로 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue

        if g[nx][ny] > g[x][y]: # 이동 가능
            dp[x][y] = max(dp[x][y], DFS(nx,ny) + 1)

    return dp[x][y]

res = 0
for i in range(n):
    for j in range(n):
        res = max(res, DFS(i,j))

print(res)