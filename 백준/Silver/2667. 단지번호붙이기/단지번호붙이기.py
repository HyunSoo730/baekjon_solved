import sys

n = int(input())
g = []

for i in range(n):
    data = list(map(int, input()))
    g.append(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
cnt_list = []
res = 0
def DFS(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny] == 1:
                cnt += 1
                g[nx][ny] = 0
                DFS(nx,ny)

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            cnt = 1
            g[i][j] = 0
            DFS(i,j)
            res += 1
            cnt_list.append(cnt)

    
print(res)
cnt_list.sort()
for x in cnt_list:
    print(x)
    
    