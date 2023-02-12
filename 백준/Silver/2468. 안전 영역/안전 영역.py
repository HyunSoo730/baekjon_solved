import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

max_data = 0
for i in range(n):
    for j in range(n):
        max_data = max(max_data, g[i][j])
#그래프 최대 높이 확인

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(a,b, h):
    dq = deque()
    dq.append((a,b))
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n: #경계선
                if ch[nx][ny] == 0 and g[nx][ny] > h: #안전영역
                    ch[nx][ny] = 1
                    dq.append((nx,ny))

res = -1
for h in range(101):
    if h > max_data:
        break #최대높이보다 비 높이가 더 크면 안전영역 없음
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and ch[i][j] == 0: #탐색 시작.
                ch[i][j] = 1 #시작점 방문처리
                BFS(i,j,h)
                cnt += 1
    res = max(res,cnt)

print(res)



