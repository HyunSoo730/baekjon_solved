import sys
input = sys.stdin.readline
from collections import deque

#그림 개수와 그 그림 중 넓이가 가장 넓은 것의 넓이
#상하좌우
n, m = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(n)]

#그림의 개수 = 연결요소
#그림의 넓이 = 1개수

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

max_cnt = 0
def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    g[a][b] = 0 #방문 처리
    result = 1 #시작점도 포함해야지.
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m: 
                if g[nx][ny] == 1:
                    g[nx][ny] = 0 #방문 처리
                    result += 1
                    dq.append((nx,ny))
    return result

res = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            temp = BFS(i,j)
            cnt += 1
            max_cnt = max(max_cnt, temp)

print(cnt)
print(max_cnt)





