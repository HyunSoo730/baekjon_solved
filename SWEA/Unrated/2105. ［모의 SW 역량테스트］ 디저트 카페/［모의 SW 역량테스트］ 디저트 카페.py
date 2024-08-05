
# nxn 격자
# 각 칸의 값은 디저트 종류를 의미
# 특정 출발점에서 출발해서 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
# 같은 종류 (값이 같은) 먹으면 안됨
# 디저트 많이 먹기

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

# 시작은 무조건 0번 방향에서 진행. 3번 바뀌고 기존 위치로 돌아오면 끝
def DFS(startX,startY,x,y,dir,change, visited):
    global res
    if change > 3: # 가지치기
        return
    if (x,y) == (startX,startY) and change == 3:
        res = max(res, len(visited))
    else: # 현재 위치에서 기존 방향으로 계속 가냐 or 방향 바꾸냐 두가지
        for i in range(2):
            dir = (dir + i) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
            if not isInner(nx,ny): continue
            if g[nx][ny] in visited: # 이미 존재
                continue
            visited.append(g[nx][ny]) # 추가 후
            DFS(startX,startY,nx,ny,dir,change + i, visited)
            visited.pop()



T = int(input())
for t in range(1, T + 1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(n):
            visited = []
            DFS(i,j,i,j,0,0,visited)

    if res == 0:
        print(f"#{t} {-1}")
    else:
        print(f"#{t} {res}")
