from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    data = rectangle
    MAX = 200
    g = [[-1] * MAX for _ in range(MAX)]
    
    for x1,y1,x2,y2 in data:
        for i in range(x1*2, x2*2 + 1):
            for j in range(y1*2, y2*2 + 1):
                if x1*2 < i < x2*2 and y1*2 <j< y2*2:
                    g[i][j] = 0
                elif g[i][j] != 0: #내부가 아닌 경우 (다른 사각형의 내부가 아니어야함 그리고)
                    g[i][j] = 1 #움직일 수 있는 테두리
    #맵은 다 만듬. 이제 최단거리
    dis = [[0] * MAX for _ in range(MAX)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    def BFS(a,b): #시작위치 받고
        dq = deque()
        dq.append((a,b))
        g[a][b] = 0
        
        while dq:
            x,y = dq.popleft()
            if x == itemX * 2 and y == itemY * 2:
                return dis[x][y] // 2 #최단거리 역시 //2 해줘야함 !!
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<MAX and 0<=ny<MAX:
                    if g[nx][ny] == 1: #방문 전
                        g[nx][ny] = 0
                        dis[nx][ny] = dis[x][y] + 1
                        dq.append((nx,ny))
        
        
    
    
    res = BFS(characterX * 2, characterY * 2)
    print(res)   
    return res
