import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

r, c = map(int, input().split())
g = []
for _ in range(r):
    temp = list(input())
    g.append(temp)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ch = [False] * 26 #시간초과 떄문에 방문표시를 이렇게...
max_cnt = -2424242424
def DFS(x,y,cnt):
    global max_cnt
    max_cnt = max(max_cnt , cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c:
            if ch[ord(g[nx][ny]) - 65] == False: #아직 방문 전
                ch[ord(g[nx][ny]) - 65] = True
                DFS(nx,ny,cnt + 1)
                ch[ord(g[nx][ny]) - 65] = False
        

ch[ord(g[0][0]) - 65] = True #시작점은 방문표시하고 들어가야함
DFS(0,0,1)
print(max_cnt)
    
    
    
    