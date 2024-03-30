import sys
from collections import deque, defaultdict

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

island = defaultdict(int) # 각 좌표별 섬 번호 기록을 위해 딕셔너리(맵) 사용

def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def BFS(a,b,num): # 시작 좌표, 섬번호 -> 해당 연결요소들 모두 num으로
    global visited
    dq = deque()
    dq.append((a,b))
    visited[a][b] = True
    island[(a,b)] = num
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isInner(nx,ny) and g[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                island[(nx,ny)] = num
                dq.append((nx,ny))

def get_min_dis(x,y): # 해당 좌표 기준 상하좌우 돌면서 확인
    src = island[(x,y)] # 현재 섬 번호
    # 재방문은 안된다.
    visited = [[False] * m for _ in range(n)]

    for i in range(4):
        nx,ny = x,y
        while True:
            nx += dx[i]
            ny += dy[i]
            if not isInner(nx,ny): break # 만약 좌표 벗어나면 탈출
            des = island[(nx,ny)]
            if des == src: break # 도착점과 같으면 안돼
            if g[nx][ny] == 1:
                d = abs(x-nx) + abs(y-ny) - 1
                if d >= 2 and d < dis[src][des]: # 다리 길이가 2이상이면서, 기존 값보다 작은 경우에 갱신
                    # print(f"시작 섬번호 {src} 도착 섬번호 {des} 거리 {d}")
                    dis[src][des] = d # 최단거리는 섬a, 섬b의 거리이므로 src->des 거리
                    dis[des][src] = d # 무방향 그래프이므로 역시 적용
                break # 사실 처음 1을 만난 순간 그 뒤는 확인하면 안된다.


def step2(): # 섬별 최단거리 구하기
    global dis
    for i in range(1, num + 1):
        dis[i][i] = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                get_min_dis(i,j)

# 1. 섬 좌표별 몇번 섬인지 기록
num = 0 # 섬 개수 및 번호
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not visited[i][j]:
            num += 1
            BFS(i,j,num) # ! 1. step1 : 각 좌표 별 섬 번호 구하기

# 2. 좌표별 섬 번호 구했으니 섬 별 최단거리 구하기
INF = int(1e9)
dis = [[INF] * (num+1) for _ in range(num+1)] # 섬 개수만큼 만들어야한다.
step2() # step2 : 섬별 최단거리 구하기

# 3. 각 섬별 최단거리 구했으니 이제 각 간선에 섬1,섬2,비용. 이런 식으로 적용 : 간선 리스트 만들기
edge = []
def step3():
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i == j: continue
            if dis[i][j] != INF: # 값이 존재한다면
                edge.append((i,j,dis[i][j]))
    edge.sort(key = lambda x : x[2])

step3()

# 4. 크루스칼을 통해 계산하기
parent = [0] * (num+1)
for i in range(1,num+1):
    parent[i] = i
def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

res = 0
for i in range(len(edge)):
    a,b,cost = edge[i]
    if find_parent(a) != find_parent(b):
        res += cost
        union_parent(a,b)

connected = True
root = find_parent(1)
for i in range(2,num+1):
    if root != find_parent(i):
        connected = False
        break

if connected:
    print(res)
else:
    print(-1)