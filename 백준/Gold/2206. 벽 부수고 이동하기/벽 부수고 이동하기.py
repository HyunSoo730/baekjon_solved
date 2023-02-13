import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

#0은 이동, 1은 벽
#최단경로
#벽 한개까지 부수고 이동 가능
n,m = map(int, input().split())
g = [list(map(int, input().rstrip())) for _ in range(n)]
# 체크할 때 x,y,z 총 3개가 필요했다.
dis = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 맨 안쪽의 0,1을 통해 벽을 부쉈는지 안부쉈는지를 체크
dis[0][0][0] = 1  #시작 지점
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(a,b,c):
    dq = deque()
    dq.append((a,b,c))

    while dq:
        x,y,z = dq.popleft()
        if x == n-1 and y == m-1:
            return dis[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m: #경계선
                #다음으로 이동할 곳이 벽이고 벽 파괴 기회를 사용하지 않은 경우
                if g[nx][ny] == 1 and z == 0:
                    dis[nx][ny][1] = dis[x][y][0] + 1 #벽 파괴 전에서 더해야지
                    dq.append((nx,ny,1))
                #다음 이동할 곳이 벽이 아니고, 아직 한번도 방문 하지 않음.
                elif g[nx][ny] == 0 and dis[nx][ny][z] == 0:
                    dis[nx][ny][z] = dis[x][y][z] + 1
                    dq.append((nx,ny,z))
    return -1 #만약 목적지 도달 못하면 -1 반환해야지

res = BFS(0,0,0)
print(res)