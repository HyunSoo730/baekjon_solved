
# 디저트 카페, nxn 보드, 각 셀의 값은 디저트의 종류를 의미.
# 대각선 방향으로 움직일 수 있음
# 특정 칸에서 출발하여 대각선 방향으로 움직이고 사각형 모양을 그리며 출발위치로 돌아와야 함.
# 중복 안됨. 꼭 사각형으로 완성해서 와야함.
# 디저트를 가장 많이 먹을 수 있는 경로 찾기.
# 모든 위치에서 시작 가능. 방향은 고정적으로 가져가도 됨
# 현재 방향으로 가거나, 꺾거나 둘 중 하나.

dx = [1,1,-1,-1]
dy = [-1,1,1,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def DFS(L, x,y,dir,now,startX,startY, visited): # 방향전환 횟수,현재 위치, 현재 방향, 현재까지의 개수, 방문 종류
    global res
    if L > 3: return # 방향 바꾼 횟수가 3번 넘어가면 안된다.
    if L == 3 and (x,y) == (startX,startY):
        res = max(res, now)
    # 현재 방향으로 그대로 가거나, 방향을 꺾거나 2가지로 진행
    else:
        for i in range(2):
            direction = (dir + i) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            if isInner(nx,ny) and g[nx][ny] not in visited:
                visited.append(g[nx][ny])
                DFS(L+i, nx,ny,direction, now+1, startX,startY, visited)
                visited.pop()


T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    res = -1
    for x in range(n):
        for y in range(n): # 모든 위치에서 판단 진행
            DFS(0,x,y,0,0,x,y, []) # 매 경로마다 확인해야 하므로 파라미터로 존재해야함
    print(f"#{t} {res}")
