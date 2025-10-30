from collections import deque
res = int(1e9)
def solution(board):
    """
    nxn 보드, (0,0) -> (n-1,n-1) 최소비용
    # 0 : 빈칸, 1 : 벽
    상하, 좌우 연결 : 직선도로, 서로 직각 : 코너
    직선 : 100원, 코너 : 500원 추가비용
    """
    g = board
    n = len(g)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1] # 방향은 북 동 남 서
    INF = int(1e9)
    dis = [[[INF] * 4 for _ in range(n)] for _ in range(n)] # 4방향 다 체크했어야 했음 !!!
    def isInner(x,y):
        return 0<=x<n and 0<=y<n
    
    
    def bfs(startX,startY):
        global res
        dq = deque()
        # 시작 위치는 (0,1), (1,0) 넣어주고 시작
        if g[1][0] == 0: # 이동 가능
            dq.append((1,0,2, 100)) # 시작위치 (1,0) 방향 2, 해당 위치까지 가는데 비용
            dis[1][0][2] = 100
        if g[0][1] == 0: # 이동 가능
            dq.append((0,1,1,100)) # 시작위치 (0,1) 방향 1, 해당 위치까지 가는데 비용
            dis[0][1][1] = 100
        
        while dq:
            x,y,d,cost = dq.popleft() 
            if cost > dis[x][y][d]:
                continue
            if (x,y) == (n-1,n-1):
                res = min(res, dis[x][y][d])
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny): continue
                if g[nx][ny] == 0:
                    if d != i: # 다르다는 것은 코너가 생기는 것.
                        if cost + 600 < dis[nx][ny][i]:
                            dis[nx][ny][i] = cost + 600
                            dq.append((nx,ny,i,cost+600))
                    else: # 같은 경우.
                        if cost + 100 < dis[nx][ny][i]:
                            dis[nx][ny][i] = cost + 100
                            dq.append((nx,ny,i,cost+100))
        
    bfs(0,0)
    print(res)
    return res

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        