import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def DFS(x,y):
    #상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 1: #배추
                board[nx][ny] = 0 #초기화.
                DFS(nx,ny)

T = int(input())
for _ in range(T):
    cnt = 0
    m,n,k = map(int, input().split()) #가로 세로 배추 개수
    board = list([0] * m for _ in range(n))
    for _ in range(k):
        x,y = map(int, input().split()) #가로 세로
        board[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                DFS(i,j)
                cnt += 1
    
    print(cnt)