import sys
from collections import deque


dx = [-1,0,1,0]
dy = [0,1,0,-1]
INF = 1000

cnt = 1
while True:
    n = int(input())
    if n == 0: break
    g = [list(map(int, input().split())) for _ in range(n)]
    # ! 각 칸에 도둑루피가 주어진다.
    dp = [[INF] * 200 for _ in range(200)]
    dp[0][0] = g[0][0]  # 시작점

    dq = deque()
    dq.append((0,0))
    res = 0
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<n and 0<=ny<n:
                if dp[x][y] + g[nx][ny] < dp[nx][ny]:
                    dp[nx][ny] = dp[x][y] + g[nx][ny]
                    dq.append((nx,ny))
    print(f"Problem {cnt}: {dp[n-1][n-1]}")
    cnt += 1