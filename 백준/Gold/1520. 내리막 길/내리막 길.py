import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#항상 내리막길로만 이동. + 오른쪽 또는 아래로만 이동.
m, n = map(int, input().split()) #m 세로 n 가로
g = [list(map(int, input().split())) for _ in range(m)]

#이전까지의 최솟값을 저장해놔야 할듯
#다음번으로 이동할수록 값이 더 작아야함
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
dp = [[-1] * n for _ in range(m)] #dp값을 통해 중복체크도 가능.
def DFS(x,y):
    if x == m-1 and y == n-1: #도착지점에 도달하면 1을 리턴
        return 1
    #이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0 #방문처리
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if g[nx][ny] < g[x][y]:
                cnt += DFS(nx,ny)
    dp[x][y] = cnt
    return dp[x][y]
            
res = DFS(0,0)
print(res)
            
