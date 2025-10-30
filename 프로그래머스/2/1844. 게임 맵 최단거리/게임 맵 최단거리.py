from collections import deque
def solution(maps):
    # 최단거리 -> BFS
    # 0 : 벽, 1 : 이동가능 
    g = maps
    n = len(g)
    m = len(g[0])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    INF = int(1e9)
    dis = [[INF] * m for _ in range(n)] # 최단거리 기록을 위해
    dis[0][0] = 1
    
    def isInner(x,y):
        return 0<=x<n and 0<=y<m
    
    def bfs(startX,startY):
        dq = deque()
        dq.append((startX,startY))
        g[0][0] = 0 # 초기값 방문 처리 
        
        while dq:
            x,y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny): continue
                
                if g[nx][ny] == 1: # 방문 가능. 
                    g[nx][ny] = 0
                    dis[nx][ny] = dis[x][y] + 1 # 애초에 방문 가능하다는 것은 최단으로 오기 때문에..
                    dq.append((nx,ny))
    
    bfs(0,0)
    res = INF
    if dis[n-1][m-1] == INF:
        return -1
    else:
        return dis[n-1][m-1]
    
    
                
                
                
                
                