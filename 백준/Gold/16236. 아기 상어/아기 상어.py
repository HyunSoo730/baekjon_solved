import sys

input = sys.stdin.readline
from collections import deque

#상어 크기보다 큰 칸 못지나감
#자신의 크기보다 큰 물고기만 먹을 수 있다
#크기 같은 곳은 갈 수 있다. 먹지는 못함
#거리 같은게 여러개면 조건에 따라 먹어야함 가장 위, 가장 왼쪽 순. 오름차순이네
#상어 크기만큼 물고기 먹으면 크기 + 1

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
#9는 아기상어 1~6은 물고기
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            a = i
            b = j
            break
#아기상어 위치 저장
#아기상어 위치에서 가장 가까운 물고기까지 최단거리.
dx = [-1,1,0,0]
dy = [0,0,1,-1]
size = 2 #아기상어 사이즈
def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    dis = [[0] * n for _ in range(n)]
    dis[a][b] = 1 #시작점을 1로 했기에, 나중에 최종거리는 1빼야함

    #같은 거리에 먹을 수 있는 물고기 여러마리 일수도 있으므로 일단 담아야함
    candidate = [] #후보군
    while dq:
        x,y = dq.popleft() #아기상어 현재 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n: 
                if dis[nx][ny] == 0: #아직 방문 전
                    if size > g[nx][ny] and g[nx][ny] != 0: #먹을 수 있는 물고기
                        dis[nx][ny] = dis[x][y] + 1
                        candidate.append((dis[nx][ny]-1, nx,ny)) #조건 우선순위로! 넣어줌 거리 짧은게 먼저, 위에 있는거 먼저, 그것도 같으면 왼쪽에 있는거!
                    elif size == g[nx][ny] or g[nx][ny] == 0:
                        dis[nx][ny] = dis[x][y] + 1 #물고기 크기 같거나, 빈칸이면 이동가능. 이동 후 다시 물고기 탐색해봐도 됨
                        dq.append((nx,ny))
    #모든 방문이 끝나면 먹을 수 있는 물고기들 들어가 있을테니 조건대로 정렬
    candidate = sorted(candidate, key = lambda x : (x[0], x[1], x[2]))
    return candidate


length = 0 #총 최단거리
cnt = 0 #먹을 물고기 개수
while True: #먹을 수 있는 물고기 다 먹을 때까지
    g[a][b] = size #현재 상어 위치 크기로 바꾼 후에
    res = BFS(a,b) #후보군 받아옴
    res = deque(res)
    if len(res) == 0:
        break #더이상 없으면.

    #맨 앞에 하나는 먹어야 하니까.
    step, x,y = res.popleft()
    length += step
    cnt += 1  #물고기 하나 먹었으니.

    if size == cnt:
        size += 1
        cnt = 0 #다시 초기화
    
    g[a][b] = 0 #기존 위치에서 움직였으니 이제 빈칸처리
    a,b = x,y #해당 위치로 다시 이동

print(length)






    