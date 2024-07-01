from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<102 and 0<=y<102:
        return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 아이템 줍기
    # 다각형 모양 지형에서 캐릭터가 아이템 줍기 위해 이동해야 한다.
    # 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현, 캐릭터는 둘레를 따라서 이동
    # 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리 구하기 
    # 초기 캐릭터 위치 (cX,cY)
    # 아이템 위치 (itemX,itemY)
    # rectangle은 (좌하단좌표, 우상단좌표)가 주어진다.
    
    # 좌표 확장을 통해 애매한 경계선 처리 해결 가능
    
    # 좌표 확장(2배)
    g = [[0] * 102 for _ in range(102)]
    # 직사각형 테두리 표시
    for x1,y1,x2,y2 in rectangle: # 좌하단 좌표, 우상단 좌표
        x1,y1,x2,y2 = x1*2,y1*2,x2*2,y2*2 # 좌표 확장  -> 이 부분에서 시작 부분도 확장해줬어야 함
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2: # 내부
                    g[i][j] = 2 # 내부 처리
                elif g[i][j] != 2:
                    g[i][j] = 1 # 테두리 처리
    

    def BFS(startX,startY):
        dq = deque()
        dq.append((startX,startY,0))
        INF = int(1e9)
        dis = [[INF] * 102 for _ in range(102)]
        dis[startX][startY] = 0
        
        while dq:
            x,y,d = dq.popleft() # 현재 위치, 현재까지의 최단거리
            if (x,y) == (itemX*2,itemY*2):
                return d // 2
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny): continue
                if g[nx][ny] == 1: # 테두리
                    if d + 1 < dis[nx][ny]:
                        dis[nx][ny] = d + 1
                        dq.append((nx,ny,d+1))
    res = BFS(characterX * 2,characterY * 2)
    print(res)
    return res
        
        
        
        
        
        
        
        
        
        