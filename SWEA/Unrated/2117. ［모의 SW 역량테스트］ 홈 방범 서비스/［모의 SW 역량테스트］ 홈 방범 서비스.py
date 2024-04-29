from collections import deque


# nxn 보드, 마름모 모양의 영역에서만 자공
# k가 커질수록 운영 비용 증가
# 운영 비용 : k**2 + (k-1) **2
# 운영 비용은 도시를 벗어난 영역에서도 똑같음.

# 홈방법 서비스 제공받는 집들은 각각 m의 비용 지불.
# 보안회사에서는 손해를 보지 않는 한 최대한 많은 집에 홈방법 서비스 제공
# 도시의 크기 n과 하나의 집이 지불할 수 있는 비용 m, 도시 정보가 주어진다.
# 손해를 보지 않으면서 홈방법 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고
# 그때의 서비스를 제공 받는 집들의 수 출력

# 보안 회사 이익 = m*포함된 집 수 - 운영비용

# 가장 중요한게 손해를 보지 않는 한 최대한 많은 집에 서비스 제공. -> 모두 다 따져봐야 함
# 범위 : 즉, n이 주어지면 중심으로부터 n만큼 퍼져나가야 함.

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def isInner(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False
def BFS(startX,startY):
    global maxCnt
    visited = [[False] * n for _ in range(n)]
    visited[startX][startY] = True
    dq = deque()
    dq.append((startX,startY))
    cnt = 0 # 현재의 탐색에서 발견된 집의 개수
    if g[startX][startY] == 1: cnt = 1
    dis = 1 # 중심좌표로부터 거리
    # 크기 1일떄도 검사. (본인 좌표만)
    if cnt * m - 운영비용[1] >= 0:
        maxCnt = max(maxCnt, cnt)

    while dis <= n: # 총 n번 퍼져나가야 함.
        size = len(dq)
        for _ in range(size):
            x,y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isInner(nx,ny):
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        dq.append((nx,ny))
                        if g[nx][ny] == 1:
                            cnt += 1
        # 보안회사의 이익이 0이상이면 갱신 가능
        if cnt * m >= 운영비용[dis+1]:
            maxCnt = max(maxCnt, cnt)
        dis += 1

T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split()) # n,m : 보드 n, 각 집 m만큼의 비용
    g = [list(map(int, input().split())) for _ in range(n)]
    # 각 좌표에서 n+1만큼 퍼져나가면서 확인
    운영비용 = [k**2 + (k-1)**2 for k in range(0,n+2)]
    maxCnt = 0

    for i in range(n):
        for j in range(n):
            BFS(i,j)
    print(f"#{t} {maxCnt}")