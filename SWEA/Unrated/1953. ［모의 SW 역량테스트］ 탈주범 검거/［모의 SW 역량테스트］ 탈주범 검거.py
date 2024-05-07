from collections import deque


# 탈주범이 있을 수 있는 위치의 개수를 계산하기
# 7개의 터널
# 각 터널 별로 가능한 방향들을 따로 기록하고 사용하자
# 각 칸의 값 중 1~7은 터널 구조물 번호, 숫자 0은 빈칸(터널이 없는 장소)
# 1. 시작위치에서 탐색 진행
# 2. 이동하고자 하는 위치와 현재 위치 모두 터널이어야 하고, 각 터널 구멍이 서로 연결되어야만 가능
# 위 경우가 해당하면 큐에 넣고 해당 위치에서 재탐색 진행.

터널 = [
    [False, False, False, False],
    [True, True, True, True],  # ! 1번은 모든 인덱스 가능
    [True, False, True, False],  # !2번 터널은 상하
    [False, True, False, True],  # ! 3번은 좌우
    [True, True, False, False],  # ! 4번은 상우
    [False, True, True, False],  # ! 5번은 하 우
    [False, False, True, True],  # ! 6번은 하,좌 터널
    [True, False, False, True]  # ! 7번은 상 좌
]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
def BFS(startX,startY,tunnel_num): # 시작위치, 터널번호 주어지면 탐색 진행
    dq = deque()
    dq.append((startX,startY,tunnel_num))
    visited = [[False] * m for _ in range(n)]
    visited[startX][startY] = True # 시작위치 방문 처리

    time = 1 # 시작 1부터
    cnt = 1 # 시작위치 포함
    while dq:
        if time == L:
            break
        size = len(dq)
        for _ in range(size):
            x,y,num = dq.popleft() # 현재 위치, 현재 터널 번호
            for i in range(4):
                if not 터널[num][i]: continue # 해당 방향 이동 못하면 continue
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny): continue
                if visited[nx][ny]: continue
                # 이동하고자 하는 위치와 현재 위치 모두 터널, 연결 성 확인
                if g[nx][ny] > 0 and 터널[g[nx][ny]][(i+2) %4]:
                    dq.append((nx,ny,g[nx][ny]))
                    visited[nx][ny] = True
                    cnt += 1
        time += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    n, m, x, y, L = map(int, input().split())  # 터널 쿠기, 시작 위치(x,y) , 탈출 후 L시간 후 가능한 위치
    g = [list(map(int, input().split())) for _ in range(n)]
    cnt = BFS(x,y,g[x][y])

    print(f"#{t} {cnt}")
