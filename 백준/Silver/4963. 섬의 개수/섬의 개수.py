import sys
sys.setrecursionlimit(10000)

#가로 세로 대각선으로 걸어갈 수 있음. 
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1]  #총 8 가지 확인

def DFS(x,y):
    g[x][y] = 0 #방문 표시
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w:
            if g[nx][ny] == 1: #섬
                DFS(nx,ny)
    
while True:
    w,h = map(int ,input().split()) #가로 세로
    if w == 0 and h == 0:
        break
    #각 테스트 케이스에 대해 섬의 개수    
    cnt = 0
    g = []
    for i in range(h):
        g.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1: #섬
                cnt += 1
                DFS(i,j)
    print(cnt)
                
    
        
        
        
        