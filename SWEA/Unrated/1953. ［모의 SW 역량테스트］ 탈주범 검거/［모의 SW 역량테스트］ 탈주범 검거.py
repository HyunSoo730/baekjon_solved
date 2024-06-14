from collections import deque

# 터널끼리 연결되어 있는 경우 이동 가능. 탈주범이 있을 수 있는 위치의 개수 구하기
# 터널 종류 7종류.
# 시간별로... BFS
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def BFS(startX,startY,type):
    dq = deque()
    dq.append((startX,startY,type))
    cnt = 1 # 시작위치 포함
    visited = [[False] * m for _ in range(n)]
    visited[startX][startY] = True
    time = 1
    while dq:
        if time == L:
            break
        size = len(dq)
        for _ in range(size):
            x,y,type = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not isInner(nx,ny): continue
                if visited[nx][ny]: continue

                if g[nx][ny] > 0: # 이동할 곳이 터널이면서
                    if 터널[g[nx][ny]][(i+2)%4] == 1 and 터널[type][i] == 1: # 둘이 이어져있다면
                        visited[nx][ny] = True
                        dq.append((nx,ny,g[nx][ny]))
                        cnt += 1 # 이동가능한 지역 추가
        time += 1

    return cnt


T = int(input())
for t in range(1,T+1):
    n,m,x,y,L = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    터널 = [
        [0,0,0,0], # 1번 인덱스부터 사용하기 위해
        [1,1,1,1], # 1번 : 전부
        [1,0,1,0], # 2번 : 상,하
        [0,1,0,1], # 3번 : 좌,우
        [1,1,0,0], # 4번 : 상,우
        [0,1,1,0], # 5번 : 하,우
        [0,0,1,1], # 6번 : 하,좌
        [1,0,0,1]  # 7번 : 상,좌
    ]

    res = BFS(x,y,g[x][y]) # 시작위치, 시작위치의 터널 넘버
    print(f"#{t} {res}")