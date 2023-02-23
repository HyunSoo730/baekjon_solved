from collections import deque
def solution(maps):
    g = maps
    n = len(maps) #세로
    m = len(maps[0]) #가로
    dis = [[0] * m for _ in range(n)]
    dis[0][0] = 1#시작점 1
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    #0은 벽 1은 이동 가능
    def BFS(a,b):
        dq = deque()
        dq.append((a,b))
        g[a][b] = 0 #방문 처리
        
        while dq:
            x,y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m: #경계선
                    if g[nx][ny] == 1: #방문 전
                        g[nx][ny] = 0
                        dis[nx][ny] = dis[x][y] + 1
                        dq.append((nx,ny))
    
    BFS(0,0)
    
    if dis[n-1][m-1] == 0: #갈 수 없음
        return -1
    else:
        return dis[n-1][m-1]