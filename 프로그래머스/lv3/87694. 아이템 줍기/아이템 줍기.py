from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    data = rectangle
    MAX = 102 #최대 칸수 200으로 잡고
    g = [[-1] * MAX for _ in range(MAX)] #그래프
    
    #그래프 좌우 뒤집어도 동일 ! 행, 열 뒤집어도 된다는 뜻.
    
    for x1,y1,x2,y2 in data: #사각형 좌표
        for i in range(2*x1, 2*x2+1):  #좌표값 2배로 !!
            for j in range(2*y1, 2*y2 + 1):
                #x1,x2,y1,y2는 테두리 이므로 제외하고 내부만 0으로 채우기
                if x1*2 < i < x2*2 and y1*2 < j <y2*2:
                    g[i][j] = 0 #사각형 0로 채우기 (내부)
                elif g[i][j] != 0: #다른 직사각형의 내부가 아니면서 테두리일때 (테두리 중에도 다른 직사각형의 내부에 포함될 수도 있으니)
                    g[i][j] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    dis = [[0] * MAX for _ in range(MAX)] #최단거리
    def BFS(a,b):
        dq = deque()
        dq.append((a,b))
        g[a][b] = 0  #시작점 방문 표시. (테두리 -> 내부 표시로 바꿈)
        
        while dq:
            x,y = dq.popleft() #현재 좌표 가져와서
            if x == itemX * 2 and y == itemY * 2:
                res = dis[x][y] // 2
                return res
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # if g[nx][ny] == 1 and dis[nx][ny] == 0: #아직 방문 전이면서 테두리이면 갈 수 있고, 갱신!
                #     dis[nx][ny] = dis[x][y] + 1
                #     dq.append((nx,ny))
                if 0<=nx<MAX and 0<=ny<MAX:
                    if g[nx][ny] == 1: #아직 방문 안한 좌표. 
                        g[nx][ny] = 0
                        dis[nx][ny] = dis[x][y] + 1
                        dq.append((nx,ny))
    res = BFS(characterX * 2, characterY * 2)   #맵을 애초에 2배로 키웠기 때문에, 시작 좌표 도착 좌표 모두 2배로 키워줘야 한다.
    # print(res)
    return res

    # 좌표를 좀더 넉넉하게 주어도 되겠다.
    
                
    
    