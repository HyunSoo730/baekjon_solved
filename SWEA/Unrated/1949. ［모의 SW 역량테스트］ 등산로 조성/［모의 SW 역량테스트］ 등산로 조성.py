
# 최대한 긴 등산로 만들기
# nxn 보드, 각 칸은 지형 높이
# 시작점. 가장 높은 봉우리에서 시작. 등산로는 높은지형에서 낮은 지형으로
# 딱 한번 최대 K만큼 지형 깎을 수 있다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def DFS(x,y,L, drill, prev): # 이전 좌표, 현재까지의 길이, 현재 드릴을 뚫었는지, 이전높이
    global res
    global visited
    res = max(res, L) # 최댓값 매번 갱신
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isInner(nx,ny): # 벗어나면
            continue
        if visited[nx][ny]:
            continue
        if g[nx][ny] < prev: # 이동 가능
            visited[nx][ny] = True
            DFS(nx,ny,L+1, drill, g[nx][ny])
            visited[nx][ny] = False
        else: # 높 -> 낮이어야 하는데 낮 -> 높인 경우
            if drill == 0: # 아직 깎지 않은 경우에 시도 가능
                if g[nx][ny] - k < prev: # 현재 좌표를 깎아서 이전 좌표보다 작게 만들 수 있다면 이동 가능
                    visited[nx][ny] = True
                    DFS(nx,ny,L+1,1, prev-1) # 최대로 가기 위해서는 이전 좌표 -1로 만드는게 베스트. 또한 깎았다는 의미로 drill에 1을 줌
                    visited[nx][ny] = False

T = int(input())
for t in range(1,T+1):
    n,k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    MAX = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > MAX:
                MAX = g[i][j] # 최댓값 저장

    res = 0  # 가장 긴 등산로 길이
    for i in range(n):
        for j in range(n):
            if g[i][j] == MAX: # 최댓값 만나면 탐색 시작
                visited = [[False] * n for _ in range(n)]
                visited[i][j] = True # 방문처리 햇어야만!!
                DFS(i,j,1,0,g[i][j]) # 시작점 포함해서 진행.
    print(f"#{t} {res}")