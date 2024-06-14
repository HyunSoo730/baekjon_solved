
# 등산로. nxn 보드, 최대한 긴 등산로 만들기
# 각 셀의 값은 높이를 뜻함.
# 등산로 만들기 규칙
# 1. 가장 높은 봉우리에서 시작. 가장 높은 봉우리 여러개 가능
# 2. 반드시 높은 지형 -> 낮은 지형으로 이동 (상하좌우만 가능)
# 3. 긴 등산로를 만들기 위해 딱 한 곳 최대 K 깊이만큼 지형 깎는 공사 가능
# 가장 긴 등산로 길이 구하기

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def DFS(x,y,now,drill, prev): # 현재 위치, 현재 등산로 길이, 뚫었는지, 이전 값
    global res
    res = max(res, now)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): continue
        if visited[nx][ny]: continue
        if g[nx][ny] < prev: # 이전 높이보다 작다면 그냥 이동 가능
            visited[nx][ny] = True
            DFS(nx,ny,now + 1, drill, g[nx][ny])
            visited[nx][ny] = False
        else: # 깎을 수 있는지 판단
            if drill == 0 and g[nx][ny] - k < prev: # 최대로 깎았을 때 더 작다면 가능
                visited[nx][ny] = True
                DFS(nx,ny,now + 1, 1, prev-1)
                visited[nx][ny] = False

T = int(input())
for t in range(1,T+1):
    n,k = map(int, input().split()) # 한 변 길이, 최대 공사 가능 깊이 K
    g = [list(map(int, input().split())) for _ in range(n)]

    pos = [] # 시작 가능 위치
    MAX = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > MAX:
                MAX = g[i][j]
    for i in range(n):
        for j in range(n):
            if g[i][j] == MAX:
                pos.append((i,j)) # 시작 가능 위치 추가.

    res = 0
    for x,y in pos:
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        DFS(x,y,1,0,MAX) # 현재 위치, 뚫었는지 안 뚫었는지, 현재 등산로 높이를 파라미터로
    print(f"#{t} {res}")