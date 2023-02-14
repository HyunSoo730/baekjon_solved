import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
#먹을 수 있는 물고기가 1마리라면 그 물고기로
#먹을 수 있는 물고기 >1 거리 가장 가까운 물고기
#아기상어 시작크기 2 같은 크기는 못먹음 지나갈 수는 있음

a = b = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 9: #아기상어 위치
            a = i
            b = j
            break

def BFS(a,b):
    dq = deque()
    dq.append((a,b))
    dis = [[0] * n for _ in range(n)] #거리 리스트로 중복까지 체크 가능.
    dis[a][b] = 1 #시작점, 거리 리스트인데 중복체크 같이. 결국 최종 거리에서 -1 해줘야함.
    res = [] #물고기 먹을 수 있는 후보들 일단 담기.
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n: #경계선
                if dis[nx][ny] == 0: #방문 전
                    #상어의 움직임은 조건에 따라서.
                    if size > g[nx][ny] and g[nx][ny] != 0: #물고기 잡아먹을 수 있음
                        dis[nx][ny] = dis[x][y] + 1
                        res.append((dis[nx][ny] -1,nx,ny))
                    elif size == g[nx][ny]: #크기 동일
                        dis[nx][ny] = dis[x][y] + 1
                        dq.append((nx,ny))
                    elif g[nx][ny] == 0: #벽인 경우
                        dis[nx][ny] = dis[x][y] + 1
                        dq.append((nx,ny))
                    #현재위치에서 4방향 다 확인해야 하니. 각기 따로 계산.
    #후보 리스트는 우선순위가 있기 때문에 정렬로.
    res = sorted(res, key = lambda x : (x[0], x[1], x[2])) 
    #오름차순으로 거리 짧은거 먼저, 그다음이 위 좌표, 그다음이 좌우 좌표인데 왼쪽부터.
    return res

#a,b에 상어 위치 저장되어 있음
cnt = 0 #몇마리 먹었는지
length = 0 #최단거리 결과값
size = 2 #상어 초기 사이즈
#맨 앞의 후보만 먹고 위치 이동 후 다시 BFS로 찾아가야함.
while True:
    g[a][b] = size #그래프상의 위치에 크기 넣어둠.
    res = BFS(a,b) #현재 위치로부터 후보 하나 먹으러.
    if len(res) == 0: #없다면
        break
    res = deque(res)
    #후보 리스트가 나오면 맨 앞의 후보 먹이를 뽑아 그 위치로 이동
    step, x,y = res.popleft() 
    length += step #움직인 거리 더해줌
    cnt += 1
    # 몇개를 먹었는지 몇초간 이동했는지 체크
    if size == cnt:
        size += 1
        cnt = 0 #다시 초기화
    
    g[a][b] = 0 #움직였으니 이제 빈칸으로.
    a,b = x,y #위치 갱신

print(length)







    