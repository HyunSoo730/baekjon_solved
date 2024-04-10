from collections import deque


# 탈주범이 있을 수 있는 위치의 개수
# 탈주범은 시간당 1의 거리 이동
# 0초가 아닌 1초부터 진행
# 가장 중요한 건, 이동할 좌표가 현재 위치와 파이프가 연결되어야 한다! -> 이 처리가 중요!!

# 각 파이프별로 이동 가능한 방향 처리 -> 리스트로 따로 선언

dx = [-1,0,1,0]
dy = [0,1,0,-1]
types = [
    [0,0,0,0], # 0번 인덱스는 사용 안해
    [1,1,1,1], # 1번 파이프는 모든 방향 이동 가능
    [1,0,1,0], # 2번 파이프는 상 하
    [0,1,0,1], # 3번 파이프는 좌우
    [1,1,0,0], # 4번 파이프는 상 우
    [0,1,1,0], # 5번 파이프는 하 우
    [0,0,1,1], # 6번 파이프는 하 좌
    [1,0,0,1] # 7번 파이프는 상 좌
]

def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def BFS(r,c,tp):
    global visited
    dq = deque()
    dq.append((r,c,tp)) # 시작 좌표, 해당 좌표의 파이프
    visited[r][c] = True # 시작점 방문체크 필수 !!!!
    time = 1 # 1초부터 시작
    while dq:
        if time == L:
            break
        size = len(dq)  #매 초마다 현재 들어있던 것들만 돌려야함
        for _ in range(size):
            x,y,type = dq.popleft() # 현재 좌표, 현재 좌표의 파이프 번호
            directions = types[type] # 해당 타입의 리스트 받아와서
            for i in range(4):
                if directions[i] == 1:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if isInner(nx,ny) and not visited[nx][ny]: # 내부 좌표이면서 아직 방문 전
                        if g[nx][ny] != 0 and types[g[nx][ny]][(i+2) % 4] == 1: # 이동할 좌표가 길이면서, 현재 좌표와 연결 (방향 반대로 연결)
                            visited[nx][ny] = True
                            dq.append((nx,ny,g[nx][ny]))
        time += 1 # 다 끝나면 1초 추가

T = int(input())
for t in range(1,T+1):
    n,m,r,c,L = map(int, input().split()) # 터널 크기, 맨홀 뚜껑 시작 좌표, 탈출 후 소요 시간
    g = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)] # 가능한 방향 기록을 위해
    BFS(r,c,g[r][c])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                cnt += 1

    print(f"#{t} {cnt}")
