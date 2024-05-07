from collections import deque

# nxn 맵, 최대한 긴 등산로 만들기
# 각 칸의 값은 지형의 높이를 나타낸다.
# 등산로 규칙
# 1. 가장 높은 봉우리에서 시작
# 2. 높은 지형에서 낮은 지형으로 연결해야 함. 높이가 같은 곳, 낮은 곳 대각선 불가능
# 3. 긴 등산로 만들기 위해 딱 한 곳 정해서 최대 K깊이만큼 지형 깎는 공사 가능
# 같거나 큰 곳이 왔을 때 검사하면 되겠다.
# -> 현재 높이 -1로 만드는 것이 베스트 -> 그래야 더 깊이 갈 수 있음

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def DFS(L, x,y, drill, prev): # 현재 깊이, 현재 좌표, 뚫었는지 체크. 비교를 위한 마지막 값
    global res
    global visited
    res = max(res, L) # 매번 갱신
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue
        if visited[nx][ny]: continue
        if g[nx][ny] < prev: # 그냥 이동 가능
            visited[nx][ny] = True
            DFS(L+1, nx,ny,drill,g[nx][ny])
            visited[nx][ny] = False  # 백트랙킹 시 원상 복구
        elif g[nx][ny] >= prev: # 길을 뚫고 가야함
            if drill == 0 and g[nx][ny] - k < prev: # 아직 뚫은 적 없고 뚫을 수 있는 경우만
                visited[nx][ny] = True
                DFS(L+1, nx,ny,1,prev-1) # 최대로 길게 연결하기 위해서는 prev-1로 진행
                visited[nx][ny] = False

T = int(input())
for t in range(1,T+1):
    n,k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    MAX = 0
    startX,startY = 0,0
    for i in range(n):
        for j in range(n):
            if MAX < g[i][j]:
                MAX = g[i][j]
    dq = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == MAX:
                dq.append((i,j))
    for x,y in dq:
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        DFS(1,x,y,0,MAX)
    print(f"#{t} {res}")