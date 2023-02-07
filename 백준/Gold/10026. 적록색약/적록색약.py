import sys
sys.setrecursionlimit(10000)

#문자열 입력할 떄는 input().strip() 잊지말기

#r == g , 상하좌우
n = int(input())
g = []
for _ in range(n):
    temp = list(input().strip())
    g.append(temp)

    
ch = [[0] * n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<n:
            if ch[nx][ny] == 0: #아직 방문 전이어야.
            #여기서 생각해야 하는게 이전 값과 동일해야 이동가능!
                if g[x][y] == g[nx][ny]: 
                    DFS(nx,ny)
                
                
cntA = 0 #일반
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0: #방문하지 않은 곳으로 설정해줬어야.
            DFS(i,j)
            cntA +=1

# 적록색맹으로 바꿔주고 다시 !
for i in range(n):
    for j in range(n):
        if g[i][j] == "R":
            g[i][j] = "G"

cntB = 0
ch = [[0] * n for _ in range(n)] #다시 초기화 후에
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0: #방문 전
            cntB += 1
            DFS(i,j)

print(cntA, cntB)

        
        
        