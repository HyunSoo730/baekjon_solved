
# nxn 보드, 각 칸의 값은 디저트 종류
# 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
# 최대한 많이 먹고 오려고 한다.
# 왔던 길 다시 못감
# 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다.
# 임의의 한 카페에서 출발해 대각선 방향으로 움직이고 서로 다른 디저트를 먹으면서 사각형 모양을 그리며 출발점으로 돌아오는 경우
# 디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 출력
# 그 경우 없으면 -1

dx = [1,1,-1,-1]
dy = [-1,1,1,-1] # 순서대로 방향

def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def DFS(L, dir,x,y,visited): # 현재 방향도 함께. 현재 방향 기준 직진(방향 유지), 좌회전을 해야하기 때문.
    global res
    if dir > 3: # 무조건 종료 방향은 3번 바꾸면 끝 가지치기 더 바꾸면 끝내야함.
        return
    if dir == 3 and (i,j) == (x,y): # 돌아온 경우
        res = max(res, L)
    else: # 아직 방향전환을 모두 이루지 못함.
        for d in range(2): # 방향 2개만 고려해도 됨
            direction = (dir + d) % 4 # 없을 수도 있으니 일단은 이렇게 진행.
            nx = x + dx[direction]
            ny = y + dy[direction]
            if isInner(nx,ny) and g[nx][ny] not in visited:
                visited.append(g[nx][ny])
                DFS(L+1, dir + d, nx,ny,visited)
                visited.pop() # 백트랙킹 시 원상복구




T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    res = -1 # 안되는 경우를 미리 넣어둠.
    for i in range(n):
        for j in range(n):
            DFS(0,0,i,j,[]) # 이 문제의 경우는 방문을 값을 통해 하기 때문에 리스트를 파라미터로 넘겨줌

    print(f"#{t} {res}")